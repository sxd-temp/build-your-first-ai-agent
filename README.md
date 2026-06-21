# 🎯 Build Your First AI Agent — Startup Idea Validator

Welcome! In this 4-hour workshop you'll build a **three-agent AI system** that
takes any startup idea, researches the open web, argues *both* sides, and writes
you a downloadable one-page decision memo.

Three agents share the **same** AI model but behave completely differently
because each has a different **role**:

| Agent | Role | What it does |
|------|------|--------------|
| 🚀 **The Optimist** | Bull-case builder | Searches the web for why this idea could WIN |
| 🔪 **The Skeptic** | Devil's advocate | Searches the web for why this idea will FAIL |
| 🎯 **The Strategist** | Synthesizer | Reads both, picks a verdict, writes the memo |

By the end you'll have it **running in your browser** and **deployed to a public URL**.

---

## Contents

- [What you'll do](#what-youll-do)
- [Setup](#setup)
- [How the labs work](#how-the-labs-work)
- [The labs](#the-labs)
- [Stuck?](#stuck)
- [Troubleshooting](#troubleshooting)
- [What you walk out with](#what-you-walk-out-with)

---

## What you'll do

Four short hours, each building on the last:

1. **Foundations** — what an AI agent actually is. You'll run your *first* agent (`hello_agent.py`).
2. **Tools & teamwork** — give an agent web search; build the 🔪 Skeptic and its task.
3. **Build the crew** — build the 🎯 Strategist and wire up the *fan-in*; run the whole thing.
4. **Ship it** — wrap it in a Streamlit app and deploy it to the web.

You are **not** typing everything from scratch. Most of the app is done for you —
you fill in the **3 files that teach the core ideas** (marked `🔨 TODO`):

| File | You write | When |
|------|-----------|------|
| `src/agents.py` | the 🔪 Skeptic, then the 🎯 Strategist | Labs 2 & 3 |
| `src/tasks.py`  | the Bear-case task (mirror the Bull-case example) | Lab 2 |
| `src/crew.py`   | the **fan-in** (one line!) | Lab 3 |

Everything else (`tools.py`, `pdf.py`, `theme.py`, `app.py`) is **done for you** —
read it, don't rewrite it. The small apps in `test_apps/` let you check your work
after each lab.

> **Heads up:** the app won't run until you've filled in the current lab's blanks —
> it stops with a friendly message telling you exactly which file to open. That's
> by design, so you always know what to do next.

---

## Setup

### 1. Open the project (no installs on your computer!)

1. Make sure you're signed in to **GitHub** (create a free account if needed).
2. Click **Fork** (top-right of this repo) → this makes *your own copy*.
3. On *your* fork, click the green **`< > Code`** button → **Codespaces** tab → **Create codespace on main**.
4. Wait ~2 minutes while it sets up (it auto-installs everything). You now have a
   full coding environment **in your browser** — nothing installed on your laptop.

### 2. Add your free AI key

1. Go to **https://aistudio.google.com/app/apikey** (sign in with Google) → **Create API key** → copy it.
2. In your Codespace, copy `.env.example` to a new file called `.env`.
3. Paste your key:  `GEMINI_API_KEY=your-key-here`  → save.

> Web search uses DuckDuckGo and needs **no key**.

### 3. Run your first agent

In the terminal at the bottom of the Codespace:

```bash
python hello_agent.py
```

Watch a single agent decide to search the web and answer. 🎉 That's an agent.
Now do the labs below — keep this page open next to your code.

---

## How the labs work

> - Room of ~7. **Code your own** Codespace; **think together**. Pair up if you like — one person shares their screen while everyone still codes their own copy.
> - Each lab is **time-boxed**; when it's up we **regroup** to share findings and lock in the approach before the next lab.
> - **Stuck?** Use Zoom **"Ask for Help"** and I'll join your room. No answer key — we crack it together at the regroup.

**Using AI to code (Copilot).** Your Codespace has GitHub Copilot built in. Use it as a *tutor, not an autopilot*:

- **Lean on it for:** explaining code/errors, looking up syntax, unblocking a bug.
- **Don't let it do everything:** you're here to learn how agents work — if it writes all the code, you leave with no understanding.
- **Rule of thumb:** write the agent logic yourself; use AI to debug, explain, and look things up.

**Two frameworks you'll reuse all day**

- **Design ONE agent →** Role (its one job) · Knowledge (backstory that shapes it) · Tools (what it needs to act) · Output (what it hands off).
- **Design a SYSTEM →** What are the distinct jobs? · What runs in sequence vs. depends on others? · Where is the decision made?

---

## The labs

### Lab 1 · Read it, then make it yours · ⏱ ~15 min → regroup

**Scenario:** Great engineers read working code, then improve it. You'll study a finished agent, learn the four pieces every agent has, then give it a personality. (You'll inherit lots of AI-generated code — reading and improving it well is the skill.)

- 🧠 **Think (room):** pick the agent a personality (skeptical journalist? hype-y futurist?); predict how the *same* question's answer changes.
- ✅ **Build it:**
  - **Read first** — open `hello_agent.py` and the provided `build_optimist` (`src/agents.py`) + `build_bull_task` (`src/tasks.py`). Spot the four parts: role, goal, backstory, tools. These are your **templates for Lab 2.**
  - **Then improve** — in `hello_agent.py`, find `TODO (Lab 1)` and rewrite the agent's `role` / `goal` / `backstory`.
  - *Hint: a strong persona names who they are, what they care about, and how they talk.*
- 🧪 **Test it:** `streamlit run test_apps/lab1_meet_your_agent.py` → ask a question → your agent answers in its **new voice** (the page shows its role).
- 🚀 **Bonus:** set `temperature` to `0.1`, then `0.9`, and rerun. What changes — and why?

### Lab 2 · Build the adversary · ⏱ ~25 min → regroup

**Scenario:** Real idea on the table — *"TutorVoice: retired teachers tutor kids over voice chat, paid by the minute."* The Optimist already loves it. Build the agent whose only job is to find why it dies.

- 🧠 **Think (room):** role (brutal but not mean)? same web tools as the Optimist, or different? what 4–5 things must the bear-case cover?
- ✅ **Build it:** fill `build_skeptic` (`src/agents.py`) and `build_bear_task` (`src/tasks.py`) — both marked `TODO (Lab 2)`.
  - *Hint: the Optimist & Bull task you read in Lab 1 are your templates — mirror them. A strong bear-case covers incumbents, failed predecessors, structural risks, and customer-apathy — each cited.*
- 🧪 **Test it:** `streamlit run test_apps/lab2_bear_case.py` → **Validate** TutorVoice → open the **Bear Case** tab to read your Skeptic's work next to the Optimist's Bull Case. *(Haven't finished Lab 2 yet? The app pauses and tells you exactly which file to open.)*
- 🚀 **Bonus:** require the Skeptic to name at least one *dead* competitor, or add a second angle (regulation, unit economics).

### Lab 3 · Wire the team & the decision · ⏱ ~25 min → regroup

**Scenario:** Two agents now disagree — but disagreement isn't a decision. Add a third that reads **both** sides and commits to a verdict. That's the **fan-in**.

- 🧠 **Think (room — sketch it!):** draw the 3 agents and the data flow. Defend: should the Strategist have web tools? why three agents instead of one big prompt?
- ✅ **Build it:** fill `build_strategist` (`src/agents.py`, `TODO (Lab 3)`, note `tools=[]`), then in `src/crew.py` make the fan-in real: change `[]` → `[bull_task, bear_task]`.
- 🧪 **Test it:** `streamlit run test_apps/lab3_full_crew.py` → validate TutorVoice → the **Memo** tab's verdict now draws on **both** the bull and bear cases (that's your fan-in working).
- 🚀 **Bonus:** add a 4th "Customer" agent that pushes back, slotted in before the memo.

### Lab 4 · Ship it to the world · ⏱ ~15 min → regroup + demos

**Scenario:** An agent system nobody can use isn't finished. Run your own idea through it, push your code, and deploy it free — walk out with a **live, shareable link**.

- ✅ **Build & ship it:**
  1. **Run it locally** — `streamlit run app.py`, validate an idea *you* care about, download the PDF. *(Codespaces pops up a preview; or use the **Ports** tab → port 8501.)*
  2. **Push to GitHub** — commit & push to your (public) fork. Source Control panel → Commit → Sync/Push  *(or `git add -A && git commit -m "my agent" && git push`)*.
  3. **Deploy free on Streamlit Cloud** — `share.streamlit.io` → sign in with GitHub → pick your repo + `app.py` → under **Secrets** add `GEMINI_API_KEY = "your-key"` → Deploy → public URL.
  - *Hint: deploy reads your code from GitHub — push step 2 before deploying, and push again whenever you change the code.*
- 🧠 **Think:** open `test_apps/lab4_minimal_app.py` — find the **4 lines** that make it an app (input · button · `build_crew()` · show result).
- 🧪 **Test it:** your local app **and** your deployed public URL both return a memo. Share the link in the demo round!
- 🚀 **Bonus:** use **Copilot Chat** to improve `app.py`'s design — review its suggestion, keep what you like, push again. (You decide, not the AI.)

---

## Stuck?

- **Ask in your breakout room** — hit **"Ask for Help"** in Zoom and the instructor will jump in. We also lock in the approach together at each regroup, so no one stays stuck.
- **Debug with AI:** when you hit a red error, select it and ask **Copilot Chat** (the chat icon in the sidebar) *"explain and fix this error."* Learning to debug with an AI assistant is part of the skill.

## Troubleshooting

| Problem | Fix |
|--------|-----|
| `GEMINI_API_KEY` not found | Make sure your file is named exactly `.env` and you saved it, then re-run. |
| "🔨 Lab isn't finished yet" message | Expected — you haven't filled in that lab's blank yet. Open the file named in the message and complete the `TODO`, then re-run. |
| App won't open | In the terminal, confirm Streamlit is running; click the "Open in Browser" popup or the **Ports** tab → port 8501. |
| Search returns errors / rate-limited | Lower **Max search results** in the sidebar; wait a few seconds and try again. |
| A run takes a while | Normal — three agents searching the web takes ~1–3 minutes. Watch the live log. |

---

## What you walk out with

A **deployed three-agent AI system** — running app, public link, downloadable PDF
memos. That's a portfolio project. Keep going: add a 4th agent, memory, or
evaluation; explore **LangGraph**, the **Anthropic Agent SDK**, **MCP**, and agent
evaluation.
