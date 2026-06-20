"""Hour 1 — Your very first agent.

Run this to watch ONE AI agent take a goal, decide to search the web, and
write an answer. This is the whole idea of an "agent" in ~25 lines:
a role + a goal + a backstory + a tool + a task.

Run it:  python hello_agent.py
"""
import os

from dotenv import load_dotenv
from crewai import Agent, Task, Crew, LLM

from src.tools import DuckDuckGoSearchTool

load_dotenv()

# 👇 Change this question to anything you're curious about.
QUESTION = "What are the 3 biggest AI agent trends in 2026? Cite your sources."


# --- The agent: who it is + what it's for ---
researcher = Agent(
    role="Research Assistant",
    goal=(
        "Answer the user's question accurately using up-to-date web sources, "
        "and cite every claim with a URL."
    ),
    backstory=(
        "You are a meticulous research assistant who never makes things up. "
        "When you are unsure, you search the web before answering."
    ),
    tools=[DuckDuckGoSearchTool(max_results=5)],
    llm=LLM(model="gemini/gemini-2.5-flash", temperature=0.3),
    verbose=True,  # so you can WATCH it think and decide to search
)

# --- The task: what to do right now ---
task = Task(
    description=QUESTION,
    expected_output="A clear, well-structured answer with a short list of source URLs at the end.",
    agent=researcher,
)


if __name__ == "__main__":
    if not os.getenv("GEMINI_API_KEY"):
        raise SystemExit(
            "❌ Add your GEMINI_API_KEY to a .env file first (copy .env.example to .env)."
        )
    crew = Crew(agents=[researcher], tasks=[task], verbose=True)
    result = crew.kickoff()
    print("\n\n===== ANSWER =====\n")
    print(result)
