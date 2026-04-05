# Module 1 – Introduction to Agentic Coding

**Duration:** ~20 minutes  
**Previous:** [Course Overview](../../README.md) | **Next:** [Module 2 – How LLMs Work](../module-02-llm-basics/README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- Explain what an "agent" is in the context of AI-assisted software development.
- Describe the difference between **autocomplete**, **chat**, and **agent** modes in GitHub Copilot.
- Identify real-world use cases where agentic coding saves significant developer time.
- Navigate the GitHub Copilot Chat interface and open an agent session.

---

## 1.1 What Is an Agent?

An **agent** is an AI system that can:

1. **Observe** its environment (your codebase, open files, terminal output).
2. **Reason** about a goal given to it by a user or another system.
3. **Act** by invoking tools — writing code, running commands, calling APIs, searching the web — and repeating this loop until the goal is achieved.

> 💡 **Key insight:** Unlike a one-shot chat response, an agent maintains a *plan* and keeps working until it succeeds or asks for clarification.

### Traditional Copilot vs. Agentic Copilot

| Feature | Autocomplete | Chat | Agent Mode |
|---------|-------------|------|------------|
| Scope | Single line / block | Single response | Multi-step task |
| Memory | None | Conversation history | Full workspace context |
| Tools | None | Limited | File system, terminal, web, APIs |
| Autonomy | Low | Medium | High |

---

## 1.2 Why Agentic Coding?

Modern software tasks are too complex for a single prompt:

- "Add authentication to my Express app" requires editing multiple files, installing packages, updating tests, and modifying configuration.
- "Find all places where we log PII and anonymise them" requires scanning the entire repo and making coordinated edits.
- "Write a feature end-to-end based on this issue" involves understanding context, writing code, writing tests, and updating documentation.

Agents tackle these multi-step tasks **autonomously**, surfacing questions to you only when genuinely blocked.

---

## 1.3 GitHub Copilot Modes

```
┌──────────────────────────────────────────────────────────┐
│                    GitHub Copilot                        │
│  ┌─────────────┐  ┌───────────────┐  ┌───────────────┐  │
│  │ Autocomplete│  │     Chat      │  │  Agent Mode   │  │
│  │  (inline)   │  │  (side panel) │  │  (agentic)    │  │
│  └─────────────┘  └───────────────┘  └───────────────┘  │
│  Tab to accept     Ask questions      Delegate tasks     │
└──────────────────────────────────────────────────────────┘
```

To open Agent Mode in VS Code:

1. Open the **Copilot Chat** panel (`Ctrl+Shift+I` / `Cmd+Shift+I`).
2. Click the mode selector and choose **Agent**.
3. Type your task — be specific about the outcome, not the steps.

---

## 1.4 Key Vocabulary

| Term | Definition |
|------|-----------|
| **Agent** | An AI that loops: observe → reason → act |
| **Tool** | A capability the agent can call (file read/write, terminal, search) |
| **Skill** | A packaged, reusable tool with a defined interface |
| **Instruction file** | A Markdown file that shapes how the agent behaves in a repo |
| **Context window** | The maximum amount of text an LLM can process in one go |
| **System prompt** | Instructions prepended before the user's message |

---

## 1.5 Hands-On Exercise

> ⏱ ~5 minutes

1. Open this repository in VS Code.
2. Open **Copilot Chat** and switch to **Agent** mode.
3. Type the following prompt and observe how the agent breaks the task into steps:

   ```
   List all the Markdown files in this repository and summarise what each one is about.
   ```

4. Notice: the agent *reads files* before answering. That's tool use in action.

---

## ✅ Module Checklist

- [ ] I can explain the difference between autocomplete, chat, and agent modes.
- [ ] I have opened Copilot in Agent mode in VS Code.
- [ ] I understand the terms: agent, tool, skill, instruction file, context window.

---

**Next: [Module 2 – How LLMs Work →](../module-02-llm-basics/README.md)**
