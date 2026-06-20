"""Crew wiring for the Startup Idea Validator.

🔨 YOU BUILD THIS FILE (Hour 3).

This is the "fan-in" pattern — the big idea of the workshop:
  1. The Optimist runs and builds the bull case.
  2. The Skeptic runs and builds the bear case.
  3. The Strategist receives BOTH of their outputs as `context` and writes the memo.

There is ONE blank to fill (look for 🔨 TODO below).

Stuck or behind? The full answer is in  solutions/crew.py
"""
from crewai import Crew, Process

from .agents import build_optimist, build_skeptic, build_strategist
from .tasks import build_bull_task, build_bear_task, build_memo_task


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
    # 1) Build the three agents (the Strategist runs cooler — less random).
    optimist = build_optimist(model, temperature, max_search_results)
    skeptic = build_skeptic(model, temperature, max_search_results)
    strategist = build_strategist(model, max(0.2, temperature - 0.3))

    # 2) Build the bull and bear tasks.
    bull_task = build_bull_task(optimist, idea, customer, advantage, budget)
    bear_task = build_bear_task(skeptic, idea, customer, advantage, budget)

    # 3) 🔨 TODO (Hour 3) — THE FAN-IN.
    #    The memo task needs BOTH earlier tasks as its `context`, so the Strategist
    #    can read what the Optimist and Skeptic found.
    #    👉 Replace the empty list  []  with  [bull_task, bear_task]
    memo_task = build_memo_task(
        strategist, idea, customer, advantage, budget,
        [],  # ← TODO: put [bull_task, bear_task] here
    )

    # 4) Assemble the crew: three agents, three tasks, run one after another.
    return Crew(
        agents=[optimist, skeptic, strategist],
        tasks=[bull_task, bear_task, memo_task],
        process=Process.sequential,
        verbose=True,
        step_callback=step_callback,
    )
