# Agentic Coding with GitHub Copilot

> A 4-hour practical course teaching developers how to use GitHub Copilot Agents, customise instructions, define skills, and build real applications with AI-driven development workflows.

---

## 🎯 Course Overview

This hands-on curriculum walks you through everything you need to know to become productive with **GitHub Copilot's agentic features** — from understanding how large language models reason about your instructions, all the way to shipping a complete application assisted by purpose-built agents.

| # | Module | Duration | Topics |
|---|--------|----------|--------|
| 1 | [Introduction to Agentic Coding](./curriculum/module-01-intro/README.md) | 20 min | What are agents? Why agentic coding? Key concepts |
| 2 | [How LLMs Work](./curriculum/module-02-llm-basics/README.md) | 30 min | Tokens, context windows, prompting, reasoning |
| 3 | [Instruction Priority Order](./curriculum/module-03-instruction-order/README.md) | 30 min | `agents.md` vs `copilot-instructions.md` vs inline prompts |
| 4 | [Setting Up Instructions](./curriculum/module-04-setup-instructions/README.md) | 30 min | Repo-level and workspace-level instruction files |
| 5 | [Skills – What They Are and How to Use Them](./curriculum/module-05-skills/README.md) | 30 min | Defining skills, attaching tools, best practices |
| 6 | [Using Copilot CLI](./curriculum/module-06-copilot-cli/README.md) | 30 min | `gh copilot`, shell commands, agent sessions |
| 7 | [Build an App with Pre-defined Agents](./curriculum/module-07-build-app/README.md) | 60 min | End-to-end project using custom agents |

**Total: ~4 hours** (including exercises and discussion breaks)

---

## 📁 Repository Structure

```
Agentic-coding/
├── curriculum/                   # One folder per module
│   ├── module-01-intro/
│   ├── module-02-llm-basics/
│   ├── module-03-instruction-order/
│   ├── module-04-setup-instructions/
│   ├── module-05-skills/
│   ├── module-06-copilot-cli/
│   └── module-07-build-app/
│       └── starter-app/          # Scaffold used in module 7
├── examples/
│   ├── agents/                   # Sample agent definition files
│   └── skills/                   # Sample skill definitions
└── .github/
    ├── copilot-instructions.md   # Repo-wide Copilot instructions (example)
    └── agents/                   # Agent files for this repo's own workflows
```

---

## 🚀 Prerequisites

| Tool | Version | Notes |
|------|---------|-------|
| [Visual Studio Code](https://code.visualstudio.com/) | Latest | With the GitHub Copilot extension |
| [GitHub Copilot](https://github.com/features/copilot) subscription | Individual or Business | Agent mode requires Copilot Chat |
| [GitHub CLI (`gh`)](https://cli.github.com/) | ≥ 2.40 | Required for Module 6 |
| Node.js | ≥ 18 LTS | Used in the Module 7 project |
| Git | ≥ 2.39 | |

---

## 🏁 Getting Started

```bash
# 1. Clone this repository
git clone https://github.com/danforceDJ/Agentic-coding.git
cd Agentic-coding

# 2. Open in VS Code
code .

# 3. Start with Module 1
open curriculum/module-01-intro/README.md
```

Begin with **[Module 1 →](./curriculum/module-01-intro/README.md)**

---

## 🤝 Contributing

Found a typo or want to add an exercise? Open a pull request — contributions are welcome!

---

## 📄 License

[MIT](./LICENSE)
