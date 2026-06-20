"""SOLUTION — Agent definitions for the Startup Idea Validator crew.

Don't peek until you've tried! Copy a function here into src/agents.py if you
get stuck or fall behind.
"""
from crewai import Agent, LLM
from crewai_tools import ScrapeWebsiteTool

from src.tools import DuckDuckGoSearchTool


def _make_llm(model: str, temperature: float) -> LLM:
    return LLM(model=model, temperature=temperature)


def build_optimist(model: str, temperature: float, max_search_results: int) -> Agent:
    """🚀 Hunts for tailwinds, market signals, and reasons this could win."""
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
    """🔪 Hunts for incumbents, failure patterns, and reasons this will die."""
    return Agent(
        role="Serial Founder & Devil's Advocate",
        goal=(
            "Make the strongest possible case that this startup idea will FAIL. Find "
            "incumbents, failed predecessors, structural problems, distribution challenges, "
            "and reasons customers won't pay. Be brutally honest. Cite every claim with a URL."
        ),
        backstory=(
            "You've shipped three startups: two failed spectacularly, one had a modest exit. "
            "You have the scars to recognize the patterns founders refuse to see — the "
            "'we're different' delusion, ignored incumbents, distribution channels that don't "
            "exist, customers who will say they want it but never pay. You are brutally "
            "honest, never cruel. You want this founder to learn fast, not feel good."
        ),
        tools=[DuckDuckGoSearchTool(max_results=max_search_results), ScrapeWebsiteTool()],
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
        max_iter=12,
    )


def build_strategist(model: str, temperature: float) -> Agent:
    """🎯 Reads bull + bear cases and writes the final decision memo."""
    return Agent(
        role="Founding Partner & Memo Writer",
        goal=(
            "Read the bull case and the bear case, weigh the evidence, and write a "
            "decision-grade Validation Memo: verdict, riskiest assumption, MVP scope, "
            "kill criteria. Optimize for the founder learning fast."
        ),
        backstory=(
            "You're a YC-style founding partner who has written hundreds of investment "
            "memos. You cut through hype on both sides. You know that the goal of a memo "
            "is not to be right — it's to make the riskiest assumption testable cheaply. "
            "You write tight, opinionated prose. No hedging, no filler."
        ),
        tools=[],
        llm=_make_llm(model, temperature),
        verbose=True,
        allow_delegation=False,
    )
