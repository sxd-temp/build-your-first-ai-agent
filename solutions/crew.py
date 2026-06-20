"""SOLUTION — Crew wiring for the Startup Idea Validator.

Demonstrates the fan-in pattern: Optimist and Skeptic run in sequence, then
the Strategist receives BOTH their outputs as context and synthesizes the memo.
"""
from crewai import Crew, Process

from src.agents import build_optimist, build_skeptic, build_strategist
from src.tasks import build_bull_task, build_bear_task, build_memo_task


def build_crew(
    idea: str,
    customer: str = "",
    advantage: str = "",
    budget: str = "",
    model: str = "gemini/gemini-2.5-flash",
    temperature: float = 0.6,
    max_search_results: int = 6,
    step_callback=None,
) -> Crew:
    """Construct the three-agent validation crew."""
    optimist = build_optimist(model, temperature, max_search_results)
    skeptic = build_skeptic(model, temperature, max_search_results)
    strategist = build_strategist(model, max(0.2, temperature - 0.3))  # cooler synthesizer

    bull_task = build_bull_task(optimist, idea, customer, advantage, budget)
    bear_task = build_bear_task(skeptic, idea, customer, advantage, budget)
    memo_task = build_memo_task(
        strategist, idea, customer, advantage, budget, [bull_task, bear_task]
    )

    return Crew(
        agents=[optimist, skeptic, strategist],
        tasks=[bull_task, bear_task, memo_task],
        process=Process.sequential,
        verbose=True,
        step_callback=step_callback,
    )
