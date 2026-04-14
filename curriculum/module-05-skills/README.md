# Module 5 – Skills: What They Are and How to Use Them

**Duration:** ~30 minutes  
**Previous:** [Module 4 – Setting Up Instructions](../module-04-setup-instructions/README.md) | **Next:** [Module 6 – Copilot CLI](../module-06-copilot-cli/README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- Define what a **skill** is in the context of GitHub Copilot agents.
- Distinguish between built-in skills and custom skills.
- Declare the skills (tools) an agent can use in its definition file.
- Choose the right skills for a given agent role.
- Explain the security implications of granting skills to agents.

---

## 5.1 What Is a Skill?

A **skill** (also called a **tool**) is a capability that an agent can invoke to interact with the world beyond the LLM's own knowledge. Without skills, an agent can only *read* the context it is given. With skills, it can *act*.

```
  ┌─────────────────────────────────┐
  │            Agent                │
  │                                 │
  │  ┌──────────────────────────┐   │
  │  │        LLM Core          │   │
  │  │  (reasoning + language)  │   │
  │  └──────────────────────────┘   │
  │           │ calls               │
  │  ┌────────▼─────────────────┐   │
  │  │         Skills           │   │
  │  │ read_file  write_file    │   │
  │  │ run_terminal  web_search │   │
  │  │ call_api   create_pr     │   │
  │  └──────────────────────────┘   │
  └─────────────────────────────────┘
```

---

## 5.2 Built-In Skills in GitHub Copilot

GitHub Copilot's agent mode ships with a set of built-in skills that map to common development tasks:

| Skill | What it does |
|-------|-------------|
| `read_file` | Reads the contents of a file in the workspace |
| `write_file` | Creates or overwrites a file |
| `list_directory` | Lists files in a directory |
| `run_terminal_command` | Executes a shell command and captures output |
| `search_codebase` | Semantic search across all files in the workspace |
| `search_web` | Searches the web (where enabled by policy) |
| `create_pull_request` | Opens a GitHub PR |
| `create_issue` | Creates a GitHub Issue |
| `get_file_diff` | Returns the diff for a file |

> ⚠️ **Not all skills are available in all environments.** Enterprise policies and network restrictions may limit which skills an agent can use.

---

## 5.3 Declaring Skills in an Agent File

When writing an agent definition file (`.github/agents/<name>.md`), you list the skills the agent is allowed to use. This serves two purposes:

1. **Scope** — the agent cannot accidentally use tools you have not granted.
2. **Documentation** — it is clear what the agent can do.

```markdown
---
name: Code Reviewer
description: Reviews pull request changes for quality and security issues.
tools:
  - read_file
  - get_file_diff
  - search_codebase
  - create_issue
---

You are a meticulous code reviewer. When given a diff or set of files,
you check for:
- Logic errors and edge cases
- Security vulnerabilities (OWASP Top 10)
- Missing or inadequate tests
- Violations of this project's coding conventions

Always create a GitHub Issue for each distinct problem you find,
with a clear title, description, and suggested fix.
```

---

## 5.4 Choosing the Right Skills for Each Agent

Use the **principle of least privilege**: grant only the skills the agent actually needs.

| Agent Role | Appropriate Skills | Avoid |
|-----------|-------------------|-------|
| **Read-only analyst** | `read_file`, `search_codebase` | `write_file`, `run_terminal_command` |
| **Code generator** | `read_file`, `write_file`, `search_codebase` | `run_terminal_command` (unless tests needed) |
| **Full-stack developer** | All file skills + `run_terminal_command` | `search_web` (unless research task) |
| **DevOps / CI agent** | `run_terminal_command`, `read_file`, `create_pr` | `write_file` (only if needed) |
| **Documentation writer** | `read_file`, `write_file`, `search_codebase` | `run_terminal_command`, `create_pr` |

---

## 5.5 Custom Skills (MCP – Model Context Protocol)

For advanced use cases, you can create **custom skills** using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/). MCP lets you expose any function — a database query, an internal API, a Jira ticket — as a skill that agents can call.

**MCP architecture:**

```
Agent ──► MCP Client ──► MCP Server ──► Your Tool/API
```

**Example: A custom "create_jira_ticket" skill**

```json
{
  "name": "create_jira_ticket",
  "description": "Creates a Jira ticket in the project backlog.",
  "parameters": {
    "title": { "type": "string", "description": "Ticket title" },
    "description": { "type": "string", "description": "Acceptance criteria" },
    "priority": { "type": "string", "enum": ["Low", "Medium", "High", "Critical"] }
  }
}
```

### 5.5.1 MCP tool limitations (important)

Before implementing custom MCP tools, be clear about practical limits:

- **Environment policy limits** — an MCP tool can still be blocked by enterprise/network policy.
- **Runtime dependency limits** — if Python/Node/runtime dependencies are missing, the tool will fail to start.
- **Latency and timeouts** — slow external APIs can make tools unreliable in chat flows.
- **Schema quality limits** — weak tool schemas produce ambiguous calls and poor outputs.
- **Security boundaries** — MCP does not automatically sanitize user input or protect secrets; your server must do this.
- **Local-only scope** — a local MCP server only works on the machine where it is running.

### 5.5.2 Build a local MCP server in Python (one skill: `check_weather`)

Use the runnable example in:

`examples/skills/local-weather-mcp/`

It exposes exactly one MCP tool:

- `check_weather(city: str, unit: c|f)` → returns a mocked local weather response.

This example uses mocked data so it runs offline and avoids API key management while learning.

### 5.5.3 Local MCP configuration

Use this **good pattern** config shape in your local `.vscode/settings.json`:

```json
{
  "github.copilot.chat.mcpServers": {
    "local-weather": {
      "command": "python",
      "args": ["${workspaceFolder}/examples/skills/local-weather-mcp/server.py"],
      "env": {}
    }
  }
}
```

Avoid this **bad pattern**:

```json
{
  "github.copilot.chat.mcpServers": {
    "weather": {
      "command": "python",
      "args": ["server.py"]
    }
  }
}
```

Why this is bad:
- relative path is fragile and depends on current working directory
- server name is vague
- no explicit environment block

### 5.5.4 Good vs bad prompting pattern for MCP tool usage

**Good pattern prompt (specific + constrained):**

> Use the `check_weather` MCP tool for city `Berlin` and unit `c`. Return only: city, temperature, condition.

**Bad pattern prompt (ambiguous + unconstrained):**

> Can you check weather maybe somewhere in Europe and tell me anything useful?

The good pattern improves tool selection, argument quality, and output consistency.

See [examples/skills/](../../examples/skills/) for complete local MCP files and runnable setup.

---

## 5.6 Security Considerations

> ⚠️ Skills that can execute code or write files are **powerful and potentially dangerous**.

Before granting a skill, ask:

- **What is the blast radius?** If the agent runs `rm -rf` by mistake, what is lost?
- **Is the agent's output reviewed before execution?** Human-in-the-loop is safer for destructive actions.
- **Is the skill idempotent?** Running it twice should produce the same result.
- **Are secrets accessible?** Agents with `run_terminal_command` can access environment variables — make sure secrets are scoped appropriately.

**Best practices:**
- Always review agent actions in the Copilot Chat panel before confirming.
- Use read-only agents for analysis tasks.
- Never grant `run_terminal_command` to agents that process untrusted external input.

---

## 5.7 Hands-On Exercise

> ⏱ ~15 minutes

**Part A – Create a read-only analysis agent**

Create `.github/agents/analyst.md`:

```markdown
---
name: Code Analyst
description: Analyses code quality without making changes.
tools:
  - read_file
  - list_directory
  - search_codebase
---

You are a code quality analyst. You read code and produce structured reports.
You NEVER modify files. Your output is always a numbered list of findings,
each with: a severity (Low/Medium/High), a description, and a file:line reference.
```

**Part B – Test the agent**

1. Open Copilot Chat and type:
   ```
   @analyst Review the JavaScript files in this repo for any potential issues.
   ```
2. Confirm the agent only reads files — it should not propose edits.
3. Ask it to create a file. It should refuse or be unable to (it lacks `write_file`).

---

## ✅ Module Checklist

- [ ] I can explain the difference between an agent's reasoning and its skills.
- [ ] I know the most common built-in Copilot skills.
- [ ] I can declare skills in an agent definition file.
- [ ] I applied the principle of least privilege when choosing skills.
- [ ] I understand the security risks of powerful skills like `run_terminal_command`.
- [ ] I can run a local Python MCP server with one custom skill and test good vs bad prompt patterns.

---

**Next: [Module 6 – Copilot CLI →](../module-06-copilot-cli/README.md)**
