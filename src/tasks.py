"""Task definitions for the Startup Idea Validator crew.

🔨 YOU BUILD THIS FILE (with the instructor).

A Task = a `description` (what to do) + an `expected_output` (the shape of the
answer) + the `agent` that owns it.

  • build_bull_task → ✅ DONE for you (your worked example)
  • build_bear_task → 🔨 TODO (Hour 2): mirror the bull task, but argue the opposite
  • build_memo_task → ✅ PROVIDED (the memo's structure is long, so it's given)

Stuck or behind? The full answer is in  solutions/tasks.py
"""
from crewai import Task, Agent


def _idea_block(idea: str, customer: str, advantage: str, budget: str) -> str:
    lines = [f"**Idea:** {idea}"]
    if customer.strip():
        lines.append(f"**Target customer:** {customer}")
    if advantage.strip():
        lines.append(f"**Founder's unfair advantage:** {advantage}")
    if budget.strip():
        lines.append(f"**Budget tier:** {budget}")
    return "\n".join(lines)


def build_bull_task(
    agent: Agent, idea: str, customer: str, advantage: str, budget: str
) -> Task:
    """✅ WORKED EXAMPLE — research the strongest evidence-backed case FOR the idea."""
    return Task(
        description=(
            f"Build the strongest evidence-backed BULL CASE for this startup idea.\n\n"
            f"{_idea_block(idea, customer, advantage, budget)}\n\n"
            f"Use the search and scrape tools to research:\n"
            f"1. Market size signals (any data you can find — even rough proxies).\n"
            f"2. Recent funding rounds or acquisitions in adjacent spaces (last 18 months).\n"
            f"3. Evidence of unmet customer demand (forum complaints, Reddit threads, "
            f"product reviews, search trends).\n"
            f"4. Comparable winners — companies in adjacent niches that prove the business "
            f"model can work.\n"
            f"5. Tailwinds — tech, regulatory, demographic, or cultural shifts that make NOW "
            f"the right time.\n\n"
            f"Be optimistic but rigorous. Cite every claim with a URL. If you cannot find "
            f"evidence for something, say so — do not fabricate."
        ),
        expected_output=(
            "A structured Markdown brief titled `# 🚀 Bull Case` with these sections:\n"
            "- **Top Reasons to Pursue** (3-5 bullets, each ending with a source link)\n"
            "- **Market Signals** (bulleted evidence with URLs)\n"
            "- **Tailwinds** (why now)\n"
            "- **Comparable Winners** (companies that prove the model)\n"
            "- **Customer Demand Evidence** (quotes/links from forums, reviews, search trends)\n"
            "- **Sources** (numbered list of all URLs)"
        ),
        agent=agent,
    )


def build_bear_task(
    agent: Agent, idea: str, customer: str, advantage: str, budget: str
) -> Task:
    """🔪 🔨 TODO (Hour 2) — the mirror of the bull task: the strongest case AGAINST.

    Write a `description` that tells the Skeptic to research:
      1. Existing incumbents / well-funded competitors
      2. Failed predecessors (find post-mortems if possible)
      3. Structural risks: distribution, unit economics, CAC, regulation
      4. Why customers might say they want it but never actually pay
      5. Why the founder's stated 'advantage' might not matter at scale

    And an `expected_output` shaped like a `# 🔪 Bear Case` brief with a Sources list.
    (Tip: open build_bull_task above and mirror its shape.)
    """
    return Task(
        description=(
            f"TODO (Hour 2): write the BEAR CASE instructions here. "
            f"Mirror build_bull_task, but argue the opposite. "
            f"Remember to include:\n{_idea_block(idea, customer, advantage, budget)}"
        ),
        expected_output="TODO: a Markdown brief titled '# 🔪 Bear Case' with sections + a numbered Sources list.",
        agent=agent,
    )


def build_memo_task(
    agent: Agent,
    idea: str,
    customer: str,
    advantage: str,
    budget: str,
    context_tasks: list[Task],
) -> Task:
    """✅ PROVIDED — synthesize the bull + bear cases into the final memo.

    Note the `context=context_tasks` at the bottom: that's how this task RECEIVES
    the outputs of the bull and bear tasks. You wire those up in crew.py (Hour 3).
    """
    return Task(
        description=(
            f"Read the bull case and bear case in your context. Weigh the evidence. "
            f"Write the final Validation Memo for this founder.\n\n"
            f"{_idea_block(idea, customer, advantage, budget)}\n\n"
            f"The memo must be DECISION-GRADE — short, opinionated, and actionable. "
            f"Do not hedge. Pick a verdict. The goal is to help the founder learn fast, "
            f"not feel good. Preserve the most important source links from the briefs.\n\n"
            f"Required structure (use this exact Markdown skeleton):\n\n"
            f"# 🎯 Validation Memo: <one-line idea summary>\n\n"
            f"## Verdict\n"
            f"🟢 **Pursue** / 🟡 **Pivot** / 🔴 **Pass** — one-sentence reason.\n\n"
            f"## The Riskiest Assumption\n"
            f"The single belief that, if wrong, kills this. One paragraph.\n\n"
            f"## Top 3 Reasons to Pursue\n"
            f"1. ... [source](url)\n"
            f"2. ...\n"
            f"3. ...\n\n"
            f"## Top 3 Reasons It'll Fail\n"
            f"1. ... [source](url)\n"
            f"2. ...\n"
            f"3. ...\n\n"
            f"## 90-Day MVP Scope\n"
            f"The smallest, cheapest experiment that tests the riskiest assumption. "
            f"Bullet what to build, what to skip, what success looks like.\n\n"
            f"## Kill Criteria\n"
            f"Specific, measurable signals that should make the founder stop. "
            f"e.g. '<5% of waitlist converts to paid in 30 days'.\n\n"
            f"## Key Sources\n"
            f"Numbered list of the 5-8 most important URLs from both briefs."
        ),
        expected_output=(
            "A complete Markdown memo following the exact skeleton above. "
            "Output the Markdown directly — no surrounding code fences, no preamble, "
            "no 'Here is the memo:' intro."
        ),
        agent=agent,
        context=context_tasks,
    )
