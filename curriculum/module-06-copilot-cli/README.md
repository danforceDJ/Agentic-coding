# Module 6 – Using Copilot CLI

**Duration:** ~30 minutes  
**Previous:** [Module 5 – Skills](../module-05-skills/README.md) | **Next:** [Module 7 – Build an App with Agents](../module-07-build-app/README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- Install and authenticate the GitHub CLI (`gh`) with Copilot.
- Use `gh copilot suggest` to generate shell commands from natural language.
- Use `gh copilot explain` to understand unfamiliar commands.
- Combine Copilot CLI with scripts and automation.
- Know when to reach for the CLI versus the VS Code chat interface.

---

## 6.1 What Is Copilot CLI?

**Copilot CLI** is a plugin for the [GitHub CLI (`gh`)](https://cli.github.com/) that brings AI assistance directly to your terminal. It is particularly useful when:

- You are already working in the terminal and don't want to switch to VS Code.
- You need to generate, understand, or fix shell commands.
- You are writing automation scripts and want AI help inline.
- You are on a server with no GUI.

---

## 6.2 Installation and Setup

### Step 1 – Install GitHub CLI

```bash
# macOS (Homebrew)
brew install gh

# Windows (winget)
winget install --id GitHub.cli

# Linux (Debian/Ubuntu)
curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg \
  | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] \
  https://cli.github.com/packages stable main" \
  | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
sudo apt update && sudo apt install gh
```

### Step 2 – Authenticate

```bash
gh auth login
# Follow the prompts — choose GitHub.com and HTTPS or SSH
```

### Step 3 – Install the Copilot Extension

```bash
gh extension install github/gh-copilot
```

### Step 4 – Verify

```bash
gh copilot --version
# Expected: gh-copilot version 1.x.x
```

---

## 6.3 Core Commands

### `gh copilot suggest`

Converts a natural-language description into a shell command.

```bash
gh copilot suggest "find all TypeScript files modified in the last 7 days"
```

**Example output:**
```bash
? Command type: shell command
  find . -name "*.ts" -mtime -7
```

You can choose to:
- **Copy** the command to your clipboard.
- **Execute** it immediately.
- **Revise** — provide more detail and regenerate.

### `gh copilot explain`

Explains an existing shell command in plain language.

```bash
gh copilot explain "find . -name '*.ts' -mtime -7 -not -path '*/node_modules/*'"
```

**Example output:**
```
This command searches the current directory recursively for files
ending in .ts that were modified within the last 7 days,
excluding anything inside a node_modules folder.
```

---

## 6.4 Command Types

When using `suggest`, Copilot asks which type of command you want:

| Type | When to use |
|------|-------------|
| `shell` | General shell commands, file operations, pipelines |
| `git` | Git operations (branches, commits, rebases, worktrees) |
| `gh` | GitHub CLI commands (PRs, issues, releases, workflows) |

**Examples:**

```bash
# Git command
gh copilot suggest --target git "undo the last 3 commits but keep the changes staged"

# gh CLI command
gh copilot suggest --target gh "list all open PRs that have been waiting more than 5 days"
```

---

## 6.5 Practical Patterns

### Pattern 1 – Quick command lookup

Instead of Googling `tar` flags every time:
```bash
gh copilot suggest "extract a .tar.gz file to a specific directory"
```

### Pattern 2 – Debug a failing command

```bash
# First, explain what went wrong
gh copilot explain "git rebase --onto main feature/old feature/new"

# Then, suggest a fix
gh copilot suggest "I want to move the last 4 commits from feature/old onto main"
```

### Pattern 3 – Script generation

```bash
gh copilot suggest "bash script that reads a list of repos from repos.txt and clones each one"
```

### Pattern 4 – `gh` automation

```bash
gh copilot suggest --target gh \
  "close all issues with the label 'duplicate' and add a comment saying see #42"
```

---

## 6.6 Using Copilot CLI in CI/CD (Advanced)

You can call Copilot CLI in GitHub Actions for documentation generation or automated summaries — though this requires the CLI to be authenticated with a token that has Copilot access.

```yaml
# .github/workflows/summarise-pr.yml  (concept — not for production use)
- name: Generate PR summary
  env:
    GH_TOKEN: ${{ secrets.COPILOT_ENABLED_TOKEN }}
  run: |
    gh copilot explain "$(git diff origin/main...HEAD --stat)"
```

> ⚠️ Always validate AI-generated commands in CI pipelines before execution.

---

## 6.7 Keyboard Shortcut (Shell Integration)

Add this function to your shell config (`~/.zshrc` or `~/.bashrc`) for instant access:

```bash
# Ask Copilot directly from any terminal prompt
copilot() {
  gh copilot suggest "$*"
}
```

Then use it anywhere:
```bash
copilot "delete all local git branches that have been merged into main"
```

---

## 6.8 Hands-On Exercise

> ⏱ ~15 minutes

Work through these tasks using only Copilot CLI — do not search online.

**Task 1:** Find all `.json` files in the current repo that contain the string `"version"`.
```bash
gh copilot suggest "find json files containing the word version in this repo"
```

**Task 2:** Create a git commit that groups only the changes in `src/` (not `tests/`).
```bash
gh copilot suggest --target git "stage only files in the src directory and commit with message 'feat: update core logic'"
```

**Task 3:** List all GitHub Issues in this repo that are open and labelled `bug`.
```bash
gh copilot suggest --target gh "list open issues with the label bug in this repo"
```

**Task 4:** Explain this command:
```bash
gh copilot explain "git log --oneline --graph --all --decorate"
```

---

## ✅ Module Checklist

- [ ] I have installed `gh` and the `gh-copilot` extension.
- [ ] I can use `gh copilot suggest` to generate shell, git, and gh commands.
- [ ] I can use `gh copilot explain` to understand commands.
- [ ] I completed all four hands-on tasks above.

---

**Next: [Module 7 – Build an App with Pre-defined Agents →](../module-07-build-app/README.md)**
