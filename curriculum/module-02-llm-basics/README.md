# Module 2 – How LLMs Work

**Duration:** ~30 minutes  
**Previous:** [Module 1 – Introduction](../module-01-intro/README.md) | **Next:** [Module 3 – Instruction Order](../module-03-instruction-order/README.md)

---

## 🎯 Learning Objectives

By the end of this module you will be able to:

- Describe what a **token** is and why it matters.
- Explain the role of **context windows** in LLM behaviour.
- Understand how **temperature** and **sampling** affect output.
- Write better prompts by understanding how the model "reads" your input.
- Explain why instruction order and placement affect agent behaviour.

---

## 2.1 From Text to Tokens

LLMs do not read words — they read **tokens**. A token is roughly 3–4 characters of English text.

```
"GitHub Copilot is amazing!"
 ↓ tokenised ↓
["Git", "Hub", " Cop", "ilot", " is", " amazing", "!"]
  1      2      3       4      5      6             7   ← 7 tokens
```

**Why this matters:**
- Every token costs money and time to process.
- The model has a fixed **context window** (e.g. 128 000 tokens for GPT-4o). Once exceeded, older content is dropped.
- Large files, long histories, and verbose instructions consume your context budget.

> 💡 **Rule of thumb:** 1 000 tokens ≈ 750 words ≈ ~40 lines of code.

---

## 2.2 The Context Window

Think of the context window as a **sliding whiteboard** — the model can only see what fits on it right now.

```
┌─────────────────────────────────────────────────────────┐
│                    Context Window                        │
│  ┌───────────────┐ ┌─────────────┐ ┌─────────────────┐  │
│  │ System Prompt │ │  Chat Hist. │ │  Current Query  │  │
│  │ (instructions)│ │  + files    │ │  (your message) │  │
│  └───────────────┘ └─────────────┘ └─────────────────┘  │
│                                                          │
│  ← Everything here influences the model's next token →  │
└─────────────────────────────────────────────────────────┘
```

GitHub Copilot **automatically fills** your context with:

1. The currently open file.
2. Recently opened and related files.
3. Your instruction files (see Module 3).
4. Conversation history.
5. Your current message.

---

## 2.3 How the Model Generates Text

LLMs are **next-token predictors**. Given all the tokens so far, the model outputs a probability distribution over the entire vocabulary and picks the most likely next token (with some randomness controlled by **temperature**).

```
Input:  "def add(a, b):\n    return"
Model:  P("a+b") = 72%, P("a + b") = 18%, P("sum(a,b)") = 6%, ...
Output: "a + b"   ← sampled token
```

**Temperature:**
- `0.0` → deterministic (always picks the highest probability token) — great for code.
- `0.7` → some creativity — good for explanations.
- `1.5` → high randomness — useful for brainstorming.

GitHub Copilot uses a **low temperature for code** so completions are predictable and correct.

---

## 2.4 Attention and "Understanding"

The model uses **attention mechanisms** to decide which earlier tokens are relevant when generating the next one. This is why:

- Placing important context **near the end** of your prompt often helps.
- **Specific, concrete language** performs better than vague abstractions.
- Repeating key constraints in different parts of the prompt reinforces them.

---

## 2.5 Prompt Structure That Works Well

```
[Role / persona]          ← who the model should act as
[Background context]      ← what it needs to know
[The task]                ← what you want it to do
[Constraints]             ← what it must or must not do
[Output format]           ← how you want the result presented
[Examples] (optional)     ← show a sample input/output pair
```

**Example — good prompt:**

```
You are a senior TypeScript engineer.
This project uses Express 4 and Jest for testing.
Refactor the `getUserById` function in src/users.ts to:
- Use async/await instead of callbacks
- Return null instead of throwing when the user is not found
- Keep existing JSDoc comments
Return only the refactored function, no explanation.
```

**Example — poor prompt:**

```
Fix the user function.
```

---

## 2.6 Why Instructions Matter for Agents

An agent makes **multiple LLM calls in a loop**. Each call re-reads the same instruction files. This means:

- Good instructions have a **compounding benefit** — they improve every step.
- Conflicting instructions create unpredictable behaviour across steps.
- Concise instructions leave more context budget for actual code.

---

## 2.7 Hands-On Exercise

> ⏱ ~10 minutes

**Part A – Token counting**

1. Visit [platform.openai.com/tokenizer](https://platform.openai.com/tokenizer) (or use the VS Code Copilot Token count extension).
2. Paste a 50-line function from a project you know.
3. Count the tokens. How many functions could fit in a 128 000-token context?

**Part B – Temperature experiment**

1. Open Copilot Chat (regular chat mode, not agent).
2. Ask: `Write a one-sentence description of what a software agent is.`
3. Regenerate the response 3 times. Notice the variation.
4. Ask the same question prefixed with `Answer in exactly one factual sentence:`. Compare variation.

---

## ✅ Module Checklist

- [ ] I can explain what a token is.
- [ ] I understand what a context window is and why it fills up.
- [ ] I know that LLMs predict the next token using probabilities.
- [ ] I can write a structured prompt using role / context / task / constraints / format.
- [ ] I understand why instructions placed in files benefit every agent step.

---

**Next: [Module 3 – Instruction Priority Order →](../module-03-instruction-order/README.md)**
