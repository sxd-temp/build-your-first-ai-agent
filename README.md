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

## What you'll do, hour by hour

1. **Foundations** — what an AI agent actually is. You'll run your *first* agent (`hello_agent.py`).
2. **Tools & teamwork** — give an agent web search; build the 🔪 Skeptic and its task.
3. **Build the crew** — build the 🎯 Strategist and wire up the *fan-in*; run the whole thing.
4. **Ship it** — wrap it in a Streamlit app and deploy it to the web.

You are **not** typing everything from scratch. Most of the app is done for you.
You fill in the **3 files that teach the core ideas** — they're marked with 🔨 below.

---

## Step 1 — Open the project (no installs on your computer!)

1. Make sure you're signed in to **GitHub** (create a free account if needed).
2. Click **Fork** (top-right of this repo) → this makes *your own copy*.
3. On *your* fork, click the green **`< > Code`** button → **Codespaces** tab → **Create codespace on main**.
4. Wait ~2 minutes while it sets up (it auto-installs everything). You now have a
   full coding environment **in your browser** — nothing installed on your laptop.

## Step 2 — Add your free AI key

1. Go to **https://aistudio.google.com/app/apikey** (sign in with Google) → **Create API key** → copy it.
2. In your Codespace, copy `.env.example` to a new file called `.env`.
3. Paste your key:  `GEMINI_API_KEY=your-key-here`  → save.

> Web search uses DuckDuckGo and needs **no key**.

## Step 3 — Run your first agent

In the terminal at the bottom of the Codespace:

```bash
python hello_agent.py
```

Watch a single agent decide to search the web and answer. 🎉 That's an agent.

## Step 4 — Fill in the blanks (this is the workshop!)

Open these files and complete the parts marked `🔨 TODO`. The instructor walks
you through each one:

| File | You write | When |
|------|-----------|------|
| `src/agents.py` | the 🔪 Skeptic, then the 🎯 Strategist | Hours 2 & 3 |
| `src/tasks.py`  | the Bear-case task (mirror the Bull-case example) | Hour 2 |
| `src/crew.py`   | the **fan-in** (one line!) | Hour 3 |

Everything else (`tools.py`, `pdf.py`, `theme.py`, `app.py`) is **done for you** — read it, don't rewrite it.

## Step 5 — Run the full app

```bash
streamlit run app.py
```

Codespaces will pop up a preview of your app. Type a startup idea, hit
**Validate Idea**, and watch the three agents work. Download the memo as a PDF.

## Step 6 — Deploy it to the web 🚀

1. Commit & push your work (in the Source Control tab, or `git commit -am "my agent" && git push`).
2. Go to **https://share.streamlit.io**, sign in with GitHub, and pick your fork + `app.py`.
3. In the app's **Settings → Secrets**, add: `GEMINI_API_KEY = "your-key"`.
4. Deploy → you get a public link you can share and put in your portfolio.

---

## Stuck or fell behind?

- Every file you edit has a complete answer in the **`solutions/`** folder — copy from there to catch up.
- **Debug with AI:** when you hit a red error, select it and ask **Copilot Chat** (the chat icon in the sidebar) *"explain and fix this error."* Learning to debug with an AI assistant is part of the skill.

## Troubleshooting

| Problem | Fix |
|--------|-----|
| `GEMINI_API_KEY` not found | Make sure your file is named exactly `.env` and you saved it, then re-run. |
| App won't open | In the terminal, confirm Streamlit is running; click the "Open in Browser" popup or the **Ports** tab → port 8501. |
| Search returns errors / rate-limited | Lower **Max search results** in the sidebar; wait a few seconds and try again. |
| A run takes a while | Normal — three agents searching the web takes ~1–3 minutes. Watch the live log. |
