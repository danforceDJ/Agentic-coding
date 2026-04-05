# Module 4 – Setting Up Copilot Instructions

**Duration:** ~30 minutes  
**Previous:** [Module 3 – Instruction Priority Order](../module-03-instruction-order/README.md) | **Next:** [Module 5 – Skills](../module-05-skills/README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- Create a `.github/copilot-instructions.md` file from scratch.
- Write instructions that effectively constrain agent behaviour.
- Apply the CRAFT framework to write high-quality instructions.
- Avoid common instruction anti-patterns.

---

## 4.1 The Repository Instruction File

The file `.github/copilot-instructions.md` is the **single most impactful file** you can add to any repository. It is automatically included in every Copilot Chat and Agent session for that repo — no user action required.

**Create it now:**

```bash
mkdir -p .github
touch .github/copilot-instructions.md
```

---

## 4.2 What to Put in `copilot-instructions.md`

Think of this file as an onboarding document for an AI engineer joining your team. Cover:

### 4.2.1 Project Overview (1–3 sentences)

```markdown
## Project Overview
This is a Node.js REST API built with Express 4 and PostgreSQL.
The API serves a React frontend and a mobile app.
```

### 4.2.2 Tech Stack

```markdown
## Tech Stack
- Runtime: Node.js 20 LTS
- Framework: Express 4
- Database: PostgreSQL 15 (via `pg` driver — no ORM)
- Testing: Jest + Supertest
- Linting: ESLint (Airbnb config) + Prettier
- CI: GitHub Actions
```

### 4.2.3 Coding Conventions

```markdown
## Conventions
- Use TypeScript strict mode.
- Prefer `async`/`await` over Promises or callbacks.
- Use named exports — avoid default exports.
- File names: `kebab-case.ts`; class names: `PascalCase`; variables: `camelCase`.
- Maximum function length: 30 lines. Extract helpers if longer.
```

### 4.2.4 Testing Requirements

```markdown
## Testing
- Every new exported function MUST have a corresponding Jest unit test.
- Integration tests use Supertest and live in `tests/integration/`.
- Minimum test coverage threshold: 80%.
- Do NOT mock the database in integration tests — use the test DB.
```

### 4.2.5 Security Rules

```markdown
## Security
- Never log passwords, tokens, or PII.
- Always use parameterised queries — never string-concatenate SQL.
- Validate and sanitise all external input using `zod`.
- Do not commit `.env` files or secrets.
```

### 4.2.6 Output Preferences

```markdown
## Output Format
- Respond with code only unless explanation is specifically requested.
- Use JSDoc comments for all exported functions.
- Include `// TODO:` markers for follow-up work rather than leaving silent gaps.
```

---

## 4.3 The CRAFT Framework for Instructions

Use CRAFT to write instructions that are easy for the model to follow:

| Letter | Stands for | Question to ask |
|--------|-----------|-----------------|
| **C** | **Clear** | Would a new engineer understand this without asking? |
| **R** | **Relevant** | Is this specific to this repo, not generic advice? |
| **A** | **Actionable** | Can the model actually follow this instruction? |
| **F** | **Focused** | Does each instruction cover one thing only? |
| **T** | **Testable** | Can I verify the model is following this instruction? |

---

## 4.4 Anti-Patterns to Avoid

| Anti-pattern | Why it's bad | Better alternative |
|-------------|-------------|-------------------|
| `Write good code` | Vague — model doesn't know what "good" means here | `Use the Airbnb ESLint config. Max cyclomatic complexity: 5.` |
| `Be careful with security` | Unactionable | `Use parameterised queries. Validate input with zod.` |
| `Use best practices` | Every team defines this differently | List the specific practices |
| Instructions that contradict each other | Model behaviour becomes unpredictable | Audit all instruction files for conflicts |
| >2000 tokens of instructions | Crowds out code context | Keep instructions under 500 tokens |

---

## 4.5 Complete Example

See this repository's own instruction file: [`.github/copilot-instructions.md`](../../.github/copilot-instructions.md)

It demonstrates all best-practice sections and is annotated with comments explaining each choice.

---

## 4.6 Workspace-Level Instructions (VS Code)

For instructions that apply to all projects on your machine (not just one repo), use VS Code settings:

1. Open VS Code Settings (`Ctrl+,` / `Cmd+,`).
2. Search for `Copilot Instructions`.
3. Add instructions under **Copilot > Chat: Code Generation Instructions**.

Or add directly to `.vscode/settings.json`:

```json
{
  "github.copilot.chat.codeGeneration.instructions": [
    {
      "text": "I prefer TypeScript with strict null checks. Always add return type annotations."
    }
  ]
}
```

---

## 4.7 Verifying Your Instructions Work

After creating or updating `copilot-instructions.md`:

1. Open Copilot Chat.
2. Ask: `Describe how you would approach writing a new function for this project.`
3. The response should reflect your conventions (e.g. mention TypeScript, JSDoc, tests).
4. If it doesn't, check:
   - The file is saved at exactly `.github/copilot-instructions.md`.
   - The file is committed (not just saved locally).
   - Reload VS Code window (`Ctrl+Shift+P` → "Reload Window").

---

## 4.8 Hands-On Exercise

> ⏱ ~15 minutes

1. Create `.github/copilot-instructions.md` in a personal test repository (or this one).
2. Add at least four sections: overview, tech stack, conventions, and one security rule.
3. Use CRAFT to evaluate each instruction you write.
4. Ask Copilot: `Write a function that fetches a user by ID from the database.`
5. Does the response follow your conventions? If not, refine your instructions and ask again.

---

## ✅ Module Checklist

- [ ] I have created a `.github/copilot-instructions.md` file.
- [ ] My instructions cover: project overview, tech stack, conventions, testing, security.
- [ ] I applied the CRAFT framework to review each instruction.
- [ ] I verified that Copilot's responses reflect my instructions.

---

**Next: [Module 5 – Skills →](../module-05-skills/README.md)**
