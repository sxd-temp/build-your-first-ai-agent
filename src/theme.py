"""Custom CSS + reusable HTML snippets to make the Streamlit app look distinctive.

✅ PROVIDED — you don't need to edit this file. It's the styling for app.py.
"""
from __future__ import annotations

import streamlit as st


CUSTOM_CSS = """
<style>
/* ---------- App-wide tone ---------- */
:root {
  --accent: #7c5cff;
  --accent-2: #00d4a4;
  --accent-warn: #ffb547;
  --accent-bad: #ff6b9b;
  --panel: rgba(255,255,255,0.04);
  --panel-strong: rgba(255,255,255,0.08);
  --border: rgba(255,255,255,0.10);
  --text-muted: #9aa3b2;
}

html, body, [class*="css"] {
  font-family: -apple-system, BlinkMacSystemFont, "Inter", "Segoe UI", Roboto, sans-serif !important;
}

.stApp {
  background:
    radial-gradient(1200px 600px at 10% -10%, rgba(124,92,255,0.18), transparent 60%),
    radial-gradient(1000px 500px at 100% 0%, rgba(0,212,164,0.10), transparent 60%),
    #0b0d13 !important;
}

/* Hide default Streamlit chrome we don't need */
#MainMenu, footer { visibility: hidden; }
header[data-testid="stHeader"] { background: transparent; }

/* ---------- Hero ---------- */
.hero {
  padding: 26px 28px 20px;
  border-radius: 18px;
  border: 1px solid var(--border);
  background:
    linear-gradient(135deg, rgba(124,92,255,0.18), rgba(0,212,164,0.08)),
    rgba(255,255,255,0.02);
  margin-bottom: 18px;
  position: relative;
  overflow: hidden;
}
.hero::before {
  content: "";
  position: absolute;
  inset: -1px;
  border-radius: 18px;
  padding: 1px;
  background: linear-gradient(135deg, rgba(124,92,255,0.6), rgba(0,212,164,0.4), transparent 70%);
  -webkit-mask: linear-gradient(#000 0 0) content-box, linear-gradient(#000 0 0);
  -webkit-mask-composite: xor;
          mask-composite: exclude;
  pointer-events: none;
}
.hero h1 {
  font-size: 34px;
  margin: 0 0 6px 0;
  background: linear-gradient(90deg, #fff, #c9bdff 50%, #8be9d2);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
  font-weight: 700;
  letter-spacing: -0.5px;
}
.hero p {
  color: #c8cdd9;
  margin: 0;
  font-size: 15px;
  line-height: 1.55;
  max-width: 760px;
}
.hero .badges {
  margin-top: 12px;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
}
.badge {
  font-size: 11px;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  padding: 4px 10px;
  border-radius: 999px;
  background: rgba(124,92,255,0.15);
  color: #c9bdff;
  border: 1px solid rgba(124,92,255,0.35);
}
.badge.green { background: rgba(0,212,164,0.12); color: #8be9d2; border-color: rgba(0,212,164,0.35); }
.badge.warn  { background: rgba(255,181,71,0.12); color: #ffd99c; border-color: rgba(255,181,71,0.35); }

/* ---------- Agent cards ---------- */
.agent-row { display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 12px; margin: 8px 0 4px; }
.agent {
  position: relative;
  padding: 14px 16px;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: var(--panel);
  transition: all 0.3s ease;
}
.agent.active {
  background: linear-gradient(135deg, rgba(124,92,255,0.18), rgba(0,212,164,0.06));
  border-color: rgba(124,92,255,0.55);
  box-shadow: 0 0 0 1px rgba(124,92,255,0.25), 0 8px 24px -8px rgba(124,92,255,0.4);
  transform: translateY(-2px);
}
.agent.done {
  background: rgba(0,212,164,0.06);
  border-color: rgba(0,212,164,0.4);
}
.agent .role {
  font-size: 11px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
}
.agent .name {
  font-size: 17px;
  font-weight: 700;
  color: #fff;
  margin: 2px 0 6px;
  display: flex;
  align-items: center;
  gap: 8px;
}
.agent .desc {
  font-size: 13px;
  color: #bfc4d1;
  line-height: 1.45;
}
.agent .status {
  margin-top: 10px;
  font-size: 12px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}
.dot {
  width: 8px; height: 8px; border-radius: 50%;
  background: #555;
  display: inline-block;
}
.agent.active .dot {
  background: var(--accent);
  box-shadow: 0 0 0 0 rgba(124,92,255, 0.7);
  animation: pulse 1.6s infinite;
}
.agent.done .dot { background: var(--accent-2); }
@keyframes pulse {
  0%   { box-shadow: 0 0 0 0 rgba(124,92,255, 0.6); }
  70%  { box-shadow: 0 0 0 10px rgba(124,92,255, 0); }
  100% { box-shadow: 0 0 0 0 rgba(124,92,255, 0); }
}

/* ---------- Verdict pill in memo ---------- */
.verdict {
  display: inline-flex; align-items: center; gap: 8px;
  padding: 8px 14px;
  border-radius: 999px;
  font-weight: 700;
  font-size: 14px;
  margin: 4px 0 12px;
  border: 1px solid;
}
.verdict.go   { background: rgba(0,212,164,0.15); color: #8be9d2; border-color: rgba(0,212,164,0.45); }
.verdict.pivot{ background: rgba(255,181,71,0.15); color: #ffd99c; border-color: rgba(255,181,71,0.45); }
.verdict.pass { background: rgba(255,107,155,0.15); color: #ffb3cc; border-color: rgba(255,107,155,0.45); }

/* ---------- Buttons ---------- */
.stButton > button, .stDownloadButton > button, .stFormSubmitButton > button {
  border-radius: 10px !important;
  font-weight: 600 !important;
  transition: transform 0.1s ease, box-shadow 0.2s ease !important;
}
.stFormSubmitButton > button[kind="primary"] {
  background: linear-gradient(135deg, #7c5cff, #5a3fd6) !important;
  border: none !important;
  box-shadow: 0 6px 18px -4px rgba(124,92,255,0.5) !important;
}
.stFormSubmitButton > button[kind="primary"]:hover {
  transform: translateY(-1px);
  box-shadow: 0 10px 24px -4px rgba(124,92,255,0.7) !important;
}

/* ---------- Tabs ---------- */
.stTabs [data-baseweb="tab-list"] {
  gap: 6px;
  background: transparent;
}
.stTabs [data-baseweb="tab"] {
  background: var(--panel) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  padding: 8px 16px !important;
  color: #c8cdd9 !important;
  font-weight: 500;
}
.stTabs [aria-selected="true"] {
  background: linear-gradient(135deg, rgba(124,92,255,0.25), rgba(0,212,164,0.10)) !important;
  border-color: rgba(124,92,255,0.5) !important;
  color: #fff !important;
}

/* ---------- Inputs ---------- */
.stTextArea textarea, .stTextInput input, .stSelectbox div[data-baseweb="select"] > div {
  background: rgba(255,255,255,0.04) !important;
  border: 1px solid var(--border) !important;
  border-radius: 10px !important;
  color: #e6e9ef !important;
}
.stTextArea textarea:focus, .stTextInput input:focus {
  border-color: var(--accent) !important;
  box-shadow: 0 0 0 2px rgba(124,92,255,0.18) !important;
}

/* ---------- Sidebar polish ---------- */
section[data-testid="stSidebar"] {
  background: rgba(11,13,19,0.85) !important;
  border-right: 1px solid var(--border);
}

/* ---------- Status / code log ---------- */
.stCode, pre {
  border-radius: 10px !important;
  font-size: 12px !important;
}

/* ---------- Result card ---------- */
.result-card {
  padding: 18px 22px;
  border-radius: 14px;
  border: 1px solid var(--border);
  background: var(--panel);
  margin-bottom: 12px;
}
.result-card .title {
  font-size: 13px;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: var(--text-muted);
  margin-bottom: 4px;
}
.result-card .idea {
  font-size: 20px;
  font-weight: 700;
  color: #fff;
  line-height: 1.3;
}

/* Subtle scrollbars */
::-webkit-scrollbar { width: 10px; height: 10px; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.12); border-radius: 6px; }
::-webkit-scrollbar-thumb:hover { background: rgba(255,255,255,0.2); }
</style>
"""


def inject_css() -> None:
    st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def hero(gemini_ok: bool) -> None:
    key_badge = (
        '<span class="badge green">● Gemini connected</span>'
        if gemini_ok
        else '<span class="badge warn">! Add GEMINI_API_KEY</span>'
    )
    st.markdown(
        f"""
        <div class="hero">
          <h1>🎯 Startup Idea Validator</h1>
          <p>Three opinionated AI agents — <strong>🚀 Optimist</strong>,
          <strong>🔪 Skeptic</strong>, <strong>🎯 Strategist</strong> — debate
          your idea and deliver a decision-grade memo with a verdict, the riskiest
          assumption, a 90-day MVP scope, and kill criteria.</p>
          <div class="badges">
            <span class="badge">Powered by CrewAI</span>
            <span class="badge">DuckDuckGo Search · No key needed</span>
            {key_badge}
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def agent_cards(active: str | None = None, done: set[str] | None = None) -> None:
    """Render the three agent cards with active/done states.

    active: one of {"optimist","skeptic","strategist"} or None
    done:   set of agents that have finished
    """
    done = done or set()

    def state(name: str) -> str:
        if name in done:
            return "done"
        if name == active:
            return "active"
        return ""

    def status_text(name: str) -> str:
        if name in done:
            return "✓ Done"
        if name == active:
            return "● Working…"
        return "Idle"

    st.markdown(
        f"""
        <div class="agent-row">
          <div class="agent {state('optimist')}">
            <div class="role">Agent 1 · Bull Case</div>
            <div class="name">🚀 The Optimist</div>
            <div class="desc">Ex-VC who hunts tailwinds, market signals,
            customer demand evidence, and comparable winners.</div>
            <div class="status"><span class="dot"></span>{status_text('optimist')}</div>
          </div>
          <div class="agent {state('skeptic')}">
            <div class="role">Agent 2 · Bear Case</div>
            <div class="name">🔪 The Skeptic</div>
            <div class="desc">Serial founder with scars. Finds incumbents,
            failed predecessors, distribution traps, and apathy risks.</div>
            <div class="status"><span class="dot"></span>{status_text('skeptic')}</div>
          </div>
          <div class="agent {state('strategist')}">
            <div class="role">Agent 3 · Synthesis</div>
            <div class="name">🎯 The Strategist</div>
            <div class="desc">YC-style partner. Weighs evidence and writes the
            decision memo: verdict, riskiest assumption, MVP, kill criteria.</div>
            <div class="status"><span class="dot"></span>{status_text('strategist')}</div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def detect_verdict(memo_md: str) -> tuple[str, str] | None:
    """Return (css_class, label) tuple if a verdict is found in the memo."""
    lower = memo_md.lower()
    # Look in the first ~800 chars to avoid false positives
    head = lower[:800]
    if "🟢" in memo_md[:800] or "pursue" in head:
        return ("go", "🟢 PURSUE")
    if "🟡" in memo_md[:800] or "pivot" in head:
        return ("pivot", "🟡 PIVOT")
    if "🔴" in memo_md[:800] or "pass" in head:
        return ("pass", "🔴 PASS")
    return None


def verdict_pill(memo_md: str) -> None:
    v = detect_verdict(memo_md)
    if not v:
        return
    css_class, label = v
    st.markdown(
        f'<div class="verdict {css_class}">{label}</div>',
        unsafe_allow_html=True,
    )
