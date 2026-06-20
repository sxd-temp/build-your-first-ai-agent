"""Agent definitions for the Startup Idea Validator crew.

🔨 YOU BUILD THIS FILE (with the instructor).

Three agents share the SAME LLM but produce very different output because their
role / goal / backstory differ. That difference IS the lesson of this workshop.

  • build_optimist   → ✅ DONE for you (your worked example — read it closely)
  • build_skeptic    → 🔨 TODO (Hour 2): mirror the Optimist, but make it pessimistic
  • build_strategist → 🔨 TODO (Hour 3): the synthesizer — note it has NO tools

Stuck or behind? The full answer is in  solutions/agents.py
"""
from crewai import Agent, LLM
from crewai_tools import ScrapeWebsiteTool

from .tools import DuckDuckGoSearchTool


def _make_llm(model: str, temperature: float) -> LLM:
    return LLM(model=model, temperature=temperature)


def build_optimist(model: str, temperature: float, max_search_results: int) -> Agent:
    """🚀  ✅ WORKED EXAMPLE — hunts for tailwinds and reasons this could win."""
    return Agent(
        role="Ex-VC Associate & Bull Case Builder",
        goal=(
            "Find the strongest possible evidence that this startup idea could become a "
            "real, venture-scale business. Surface market signals, customer demand, recent "
            "funding in adjacent spaces, and comparable winners. Cite every claim with a URL."
        ),
        backstory=(
            "You spent five years as an associate at a top-tier seed fund, where you saw "
            "unicorns that everyone laughed at in their first pitch. You believe most great "
            "businesses look like bad ideas at first. Your superpower is spotting tailwinds — "
            "demographic shifts, regulatory changes, new infrastructure — that make this the "
            "right time for an idea. You are optimistic but evidence-driven, never naive."
        ),
        tools=[DuckDuckGoSearchTool(max_results=max_search_results), ScrapeWebsiteTool()],
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
        max_iter=12,
    )


def build_skeptic(model: str, temperature: float, max_search_results: int) -> Agent:
    """🔪  🔨 TODO (Hour 2) — the mirror image of the Optimist: find why it FAILS.

    Fill in role / goal / backstory below. Keep tools and everything else the
    same as the Optimist — the Skeptic also needs to search the web.

    💡 Suggested role text (this keeps the live agent-card animation working):
        "Serial Founder & Devil's Advocate"
    """
    return Agent(
        role="TODO: who is this agent?  (suggested: 'Serial Founder & Devil's Advocate')",
        goal="TODO: prove this idea will FAIL — incumbents, failed predecessors, why customers won't pay. Cite every claim with a URL.",
        backstory="TODO: 2-3 sentences. A founder with scars who spots the patterns others refuse to see. Brutally honest, never cruel.",
        tools=[DuckDuckGoSearchTool(max_results=max_search_results), ScrapeWebsiteTool()],
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
        max_iter=12,
    )


def build_strategist(model: str, temperature: float) -> Agent:
    """🎯  🔨 TODO (Hour 3) — reads BOTH cases and writes the final memo.

    Notice the difference: this agent has NO tools. It doesn't search — it
    THINKS, using what the other two agents already found. That is the
    "synthesis" role in a multi-agent system.

    💡 Suggested role text (keeps the live agent-card animation working):
        "Founding Partner & Memo Writer"
    """
    return Agent(
        role="TODO: who is this agent?  (suggested: 'Founding Partner & Memo Writer')",
        goal="TODO: read the bull + bear cases, weigh the evidence, and write a decision-grade memo.",
        backstory="TODO: 2-3 sentences. A YC-style partner who has written hundreds of memos and cuts through hype on both sides.",
        tools=[],  # ← the synthesizer has NO tools. Leave this list empty.
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
    )
