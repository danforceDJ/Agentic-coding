# AGENTS.md

## Purpose and Scope
- This repo is a **course workspace**: most folders are Markdown curriculum, and the only runnable app is `curriculum/module-07-build-app/starter-app/`.
- Treat changes as either: (1) course content updates in `curriculum/module-XX-*/README.md`, or (2) starter API work in `starter-app`.

## Codebase Map (What Matters First)
- Global defaults for AI/code style live in `.github/copilot-instructions.md`.
- Specialized role behavior lives in `.github/agents/*.md` (`backend-engineer`, `test-engineer`, `docs-writer`, `code-reviewer`).
- **Presentation layer:** `index.html` at root — standalone slide deck deployed at https://llmbasicscopilot.netlify.app/.
- Starter API entrypoints are `starter-app/src/app.ts` (Express wiring) and `starter-app/src/server.ts` (listen).
- Existing route pattern is `starter-app/src/routes/health.ts` and corresponding integration test `starter-app/tests/health.test.ts`.

## Architecture and Data Flow (Starter App)
- Request flow is `server.ts -> app.ts -> route router`; `app.ts` mounts routers with `app.use('/health', healthRouter)`.
- `app.ts` already enables JSON parsing via `app.use(express.json())`.
- `app.ts` intentionally contains `// TODO: Register task routes here` to support Module 7 exercises.
- Current behavior contract is `GET /health -> 200 {"status":"ok"}` (see `tests/health.test.ts`).

## Working Style Expected in This Repo
- TypeScript strict mode is required (`starter-app/tsconfig.json` has `"strict": true`).
- Use named exports by default; default export is allowed for Express `app` (`src/app.ts`).
- Prefer `async`/`await`, keep functions <=30 lines, and add JSDoc on exported functions/types.
- Validate external input with Zod and avoid logging secrets/PII (`.github/copilot-instructions.md`).

## Build, Test, and Local Run
- Run from `curriculum/module-07-build-app/starter-app`.
- Install: `npm install`
- Dev server: `npm run dev` (module docs expect `http://localhost:3000`).
- Tests: `npm test` (Jest + Supertest integration style).
- Production compile/run: `npm run build` then `npm start`.

## Testing and Quality Gates
- Jest is configured for `tests/**/*.test.ts` (`starter-app/jest.config.js`).
- Coverage thresholds are enforced at 80% global branches/functions/lines/statements.
- Existing tests use HTTP-level assertions with Supertest against `app` (see `tests/health.test.ts`).

## Integration Points and Agent Handoffs
- Course workflow expects implementation -> tests -> docs -> review via `.github/agents/*.md` (see `curriculum/module-07-build-app/README.md`).
- If adding API features, follow this file pattern: routes in `src/routes/`, schemas in `src/schemas/`, tests in `tests/`, docs in `docs/api.md`.
- MCP/tooling examples are reference-only under `examples/skills/`; use `examples/skills/local-weather-mcp/copilot-mcp-settings.good.json` as the VS Code MCP config template.

## Presentation Layer (`index.html`)
- `index.html` is a **single-file, no-build slide deck** (990 lines, 23 slides, embedded CSS + JS). Do NOT split into separate files.
- Deployed on **Netlify** at https://llmbasicscopilot.netlify.app/ — auto-deploys on every push to the default branch.
- Slide structure: each slide is `<div class="slide">` inside `<div class="deck" id="deck">`. The active slide carries class `active`; the outgoing slide gets class `prev`.
- Module color badges use `<span class="module-badge m1">` through `m7` (colors defined in `:root` CSS variables at the top of the file).
- **Content sync rule:** slide content must mirror the matching `curriculum/module-XX-*/README.md`. When updating a module README, update the corresponding slides in `index.html` too — and vice versa.
- Navigation is keyboard (`←`/`→`/`Home`/`End`/`Space`), button, and swipe — driven by the inline `<script>` at the bottom of the file. No external JS dependencies.

## Instruction Priority (When Prompts Conflict)
- Repository teaching material defines this precedence: inline prompt > `.github/agents/<name>.md` > `.github/copilot-instructions.md` > user-level settings (`curriculum/module-03-instruction-order/README.md`).
- Keep new guidance consistent across these layers to avoid contradictory agent behavior.

