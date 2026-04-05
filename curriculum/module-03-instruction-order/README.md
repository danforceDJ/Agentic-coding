# Module 3 – Instruction Priority Order

**Duration:** ~30 minutes  
**Previous:** [Module 2 – How LLMs Work](../module-02-llm-basics/README.md) | **Next:** [Module 4 – Setting Up Instructions](../module-04-setup-instructions/README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- List every location where GitHub Copilot reads instructions.
- Explain the **priority order** in which those instructions are applied.
- Describe when to use each file type.
- Predict what happens when instructions conflict.

---

## 3.1 The Four Places GitHub Copilot Reads Instructions

When GitHub Copilot processes your request in Agent mode, it assembles its system prompt from multiple sources — in a specific order:

```
Priority (highest → lowest)
─────────────────────────────────────────────────
1. Inline prompt              ← what you type right now
2. Agent definition file      ← .github/agents/<name>.md
3. Repo instruction file      ← .github/copilot-instructions.md
4. User-level instructions    ← VS Code settings / copilot settings
─────────────────────────────────────────────────
```

> 💡 **Higher priority does not erase lower priority.** All sources are combined into one system prompt. However, when instructions conflict, the model tends to follow the **most recently / most prominently stated** rule.

---

## 3.2 Source 1 – The Inline Prompt

Whatever you type in the chat box is the **most immediate context**. The model pays the most attention to this because it appears closest to the generation point.

**Best used for:** one-off task-specific instructions, clarifications, overrides.

```
# Example inline override
Ignore the TypeScript style guidelines for this response only —
use plain JavaScript so a junior dev can read it more easily.
```

---

## 3.3 Source 2 – Agent Definition Files (`.github/agents/`)

Agent files live at `.github/agents/<agent-name>.md`. They define **specialised agents** with a specific persona, tools, and behaviour — similar to a job description.

```
.github/
└── agents/
    ├── backend-engineer.md   ← specialised for API & DB work
    ├── frontend-engineer.md  ← specialised for UI components
    ├── code-reviewer.md      ← focused on review and feedback
    └── docs-writer.md        ← documentation specialist
```

When you invoke a named agent (e.g. `@backend-engineer`), its file is inserted into the system prompt **above** the repo-level instructions.

**Structure of an agent file:**

```markdown
---
name: Backend Engineer
description: Expert in Node.js, Express, and PostgreSQL API development.
tools:
  - read_file
  - write_file
  - run_terminal_command
  - search_codebase
---

You are a senior backend engineer. You write clean, well-tested
Node.js code using Express and PostgreSQL. You follow REST best
practices and always include input validation and error handling.
When writing database queries, use parameterised queries to prevent SQL injection.
```

See [examples/agents/](../../examples/agents/) for ready-to-use examples.

---

## 3.4 Source 3 – Repo-Level Instruction File (`.github/copilot-instructions.md`)

This single file sets the **default behaviour for all Copilot interactions** in the repository. Every chat message and agent invocation automatically includes it.

```
.github/
└── copilot-instructions.md   ← applies to ALL Copilot interactions
```

**Use this file for:**
- Project tech stack and conventions.
- Forbidden patterns (e.g. "never use `var`").
- Required patterns (e.g. "always write a Jest test for new functions").
- Tone and output format preferences.
- Security rules that apply everywhere.

See [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md) for the example in this repo.

---

## 3.5 Source 4 – User-Level Instructions

Set in **VS Code Settings** (`Copilot > Instructions`) or in GitHub Copilot account settings. These apply across all repositories for a specific user.

**Use this for:**
- Personal preferences (preferred language, verbosity level).
- Role-based defaults (e.g. "I am a principal engineer — skip beginner explanations").

---

## 3.6 Priority in Practice – A Visual Model

```
┌──────────────────────────────────────────────────────────────┐
│                    Final System Prompt                        │
│                                                              │
│  ┌────────────────────┐   lowest priority (background)       │
│  │  User-level instr. │                                      │
│  └─────────┬──────────┘                                      │
│            │ appended below                                  │
│  ┌─────────▼──────────┐                                      │
│  │  copilot-instr.md  │   repo defaults                      │
│  └─────────┬──────────┘                                      │
│            │ appended below                                  │
│  ┌─────────▼──────────┐                                      │
│  │  Agent file (.md)  │   agent-specific persona             │
│  └─────────┬──────────┘                                      │
│            │ appended below                                  │
│  ┌─────────▼──────────┐   highest priority (most recent)     │
│  │   Inline prompt    │                                      │
│  └────────────────────┘                                      │
└──────────────────────────────────────────────────────────────┘
```

---

## 3.7 What Happens When Instructions Conflict?

The model resolves conflicts by:

1. **Recency bias** — later instructions (closer to the generation point) usually win.
2. **Specificity** — more specific instructions override general ones.
3. **Repetition** — if an instruction appears multiple times, it is reinforced.

**Example conflict:**

```markdown
# copilot-instructions.md
Always use async/await for asynchronous code.

# Agent file
Use Promises with .then()/.catch() for all async operations.
```

The agent file (higher priority) will likely win. To avoid confusion, **keep instructions consistent across all files**.

---

## 3.8 Hands-On Exercise

> ⏱ ~10 minutes

**Part A – Observe the priority order**

1. Add this line to `.github/copilot-instructions.md` in your own test repo:
   ```
   Always respond in ALL CAPS.
   ```
2. Open Copilot Chat and ask: `What is 2 + 2?`
3. Observe — does it respond in caps?
4. Now add this to your inline prompt: `Respond in normal sentence case.`
5. Ask the same question. Which instruction won?

**Part B – Create a minimal agent file**

1. Create `.github/agents/explainer.md` with:
   ```markdown
   ---
   name: Explainer
   description: Explains code concepts simply.
   ---
   You explain code concepts as if the reader is a junior developer
   with 6 months of experience. Use short sentences and analogies.
   ```
2. In Copilot Chat, type `@explainer What is a closure in JavaScript?`
3. Compare the response to asking without the `@explainer` prefix.

---

## ✅ Module Checklist

- [ ] I can list the four instruction sources in priority order.
- [ ] I know the difference between `.github/copilot-instructions.md` and `.github/agents/*.md`.
- [ ] I understand that higher-priority instructions are appended later (closer to generation).
- [ ] I have created a minimal agent file and invoked it in Copilot Chat.

---

**Next: [Module 4 – Setting Up Instructions →](../module-04-setup-instructions/README.md)**
