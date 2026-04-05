# Module 7 – Build an App with Pre-defined Agents

**Duration:** ~60 minutes  
**Previous:** [Module 6 – Copilot CLI](../module-06-copilot-cli/README.md) | **Back to:** [Course Overview](../../README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- Set up a repository with a complete multi-agent configuration.
- Coordinate multiple specialised agents to build a feature end-to-end.
- Use agents for code generation, testing, documentation, and review.
- Recognise when to hand off between agents.
- Ship a working REST API feature from requirements to pull request using only agents.

---

## 7.1 Project Overview

You will build **Task Tracker API** — a simple Node.js/Express REST API for managing tasks. The project already has a starter scaffold (see [`starter-app/`](./starter-app/)).

You will use **four pre-defined agents** that are ready in this repository:

| Agent | File | Role |
|-------|------|------|
| `@backend-engineer` | `.github/agents/backend-engineer.md` | Implements API routes and DB logic |
| `@test-engineer` | `.github/agents/test-engineer.md` | Writes unit and integration tests |
| `@docs-writer` | `.github/agents/docs-writer.md` | Writes README and API documentation |
| `@code-reviewer` | `.github/agents/code-reviewer.md` | Reviews code and raises issues |

---

## 7.2 Project Setup

### Step 1 – Install dependencies

```bash
cd curriculum/module-07-build-app/starter-app
npm install
```

### Step 2 – Start the development server

```bash
npm run dev
# Server running at http://localhost:3000
```

### Step 3 – Verify the health endpoint

```bash
curl http://localhost:3000/health
# Expected: {"status":"ok"}
```

---

## 7.3 Feature Requirements

You will implement the **Tasks CRUD API** with these endpoints:

| Method | Path | Description |
|--------|------|-------------|
| `GET` | `/tasks` | List all tasks |
| `POST` | `/tasks` | Create a new task |
| `GET` | `/tasks/:id` | Get a single task |
| `PUT` | `/tasks/:id` | Update a task |
| `DELETE` | `/tasks/:id` | Delete a task |

**Task data model:**

```json
{
  "id": "uuid",
  "title": "string (required, max 200 chars)",
  "description": "string (optional)",
  "status": "todo | in_progress | done",
  "createdAt": "ISO 8601 timestamp",
  "updatedAt": "ISO 8601 timestamp"
}
```

---

## 7.4 Step-by-Step Build (Using Agents)

### Step 1 – Implement the routes with `@backend-engineer`

Open Copilot Chat and type:

```
@backend-engineer Implement the Tasks CRUD API described in
curriculum/module-07-build-app/README.md (the table in section 7.3).
Use in-memory storage for now (a Map). Add input validation using zod.
Place routes in src/routes/tasks.ts and register them in src/app.ts.
```

> 👀 **Watch the agent:** It will read `src/app.ts`, create `src/routes/tasks.ts`, and potentially create a `src/schemas/task.ts` for Zod schemas. This may take 2–3 minutes.

**After the agent finishes:**
- Review the generated files.
- Run `npm run dev` and test with `curl` or a REST client.

---

### Step 2 – Write tests with `@test-engineer`

```
@test-engineer Write Jest unit tests for all the new task routes
in src/routes/tasks.ts. Use supertest to make HTTP requests.
Cover: happy paths, validation errors (invalid input), and 404 cases.
Place tests in tests/tasks.test.ts.
```

**Verify tests pass:**

```bash
npm test
```

---

### Step 3 – Document the API with `@docs-writer`

```
@docs-writer Read the task routes in src/routes/tasks.ts and write
API documentation in docs/api.md. Include for each endpoint:
the method, path, request body schema, response schema,
and at least one curl example.
```

---

### Step 4 – Review the code with `@code-reviewer`

```
@code-reviewer Review all files modified in this session:
src/routes/tasks.ts, src/schemas/task.ts (if it exists), and tests/tasks.test.ts.
Check for: missing error handling, security issues, test coverage gaps,
and any violations of the project conventions in .github/copilot-instructions.md.
```

**Address any issues the reviewer raises** — ask `@backend-engineer` to fix them:

```
@backend-engineer The code reviewer found these issues: [paste issues].
Please fix them.
```

---

### Step 5 – Prepare a pull request

Using Copilot CLI:

```bash
# Stage all changes
git add .

# Ask Copilot to write the commit message
gh copilot suggest --target git "write a conventional commit message for adding a Tasks CRUD API with in-memory storage, zod validation, Jest tests, and API documentation"
```

Then commit and push:

```bash
git commit -m "<suggested message>"
git push origin feature/tasks-crud-api
```

---

## 7.5 Starter App Structure

```
starter-app/
├── src/
│   ├── app.ts            ← Express app setup (already created)
│   ├── server.ts         ← HTTP server entry point (already created)
│   └── routes/
│       └── health.ts     ← Health check route (already created)
├── tests/
│   └── health.test.ts    ← Example test (already created)
├── docs/                 ← Created by @docs-writer in step 3
├── package.json
├── tsconfig.json
└── jest.config.js
```

---

## 7.6 Reflection: What Just Happened?

In under an hour you:

1. Defined a feature as a natural-language requirement.
2. Delegated implementation to a specialised `@backend-engineer` agent.
3. Delegated testing to a `@test-engineer` agent.
4. Delegated documentation to a `@docs-writer` agent.
5. Ran a code review via a `@code-reviewer` agent.
6. Used Copilot CLI to generate a meaningful commit message.

Each agent knew **exactly** what to do because of:
- Its agent definition file (persona + tools).
- The repo-level `copilot-instructions.md` (conventions + stack).
- Your precise, outcome-focused prompt.

---

## 7.7 Extension Challenges

> ⏱ If you finish early, try one of these:

**Challenge A:** Add persistence with a SQLite database. Ask `@backend-engineer` to replace the in-memory Map with `better-sqlite3`.

**Challenge B:** Add authentication. Ask `@backend-engineer` to protect routes with a Bearer token middleware.

**Challenge C:** Set up a GitHub Actions CI workflow. Ask the agents to create `.github/workflows/ci.yml` that runs `npm test` on every push.

---

## ✅ Module Checklist

- [ ] I installed dependencies and verified the starter app runs.
- [ ] I used `@backend-engineer` to implement all five CRUD endpoints.
- [ ] I used `@test-engineer` to write tests, and they all pass.
- [ ] I used `@docs-writer` to generate API documentation.
- [ ] I used `@code-reviewer` to review the code and addressed any issues.
- [ ] I used Copilot CLI to generate a commit message and pushed the changes.

---

## 🎓 Course Complete!

Congratulations — you have completed the **Agentic Coding with GitHub Copilot** course.

You now know how to:
- Explain how LLMs process instructions (Module 2).
- Set up instruction files that improve every Copilot interaction (Modules 3 & 4).
- Define specialised agents with the right skills and personas (Modules 3 & 5).
- Use Copilot from the terminal with the CLI (Module 6).
- Coordinate multiple agents to build real features end-to-end (Module 7).

**[← Back to Course Overview](../../README.md)**
