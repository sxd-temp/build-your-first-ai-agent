"""Custom CrewAI tools that don't require paid API keys.

- DuckDuckGoSearchTool: free web search via the `ddgs` package.

✅ PROVIDED — you don't need to edit this file. Read it to see what a CrewAI
   tool looks like: a name, a description the agent reads to decide when to use
   it, an input schema, and a `_run` method that does the work.
"""
from __future__ import annotations

from typing import Type

from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class DuckDuckGoSearchInput(BaseModel):
    query: str = Field(..., description="The search query to send to DuckDuckGo.")


class DuckDuckGoSearchTool(BaseTool):
    name: str = "web_search"
    description: str = (
        "Search the public web via DuckDuckGo. Returns a numbered list of results "
        "with title, URL, and a short snippet. Use this to find sources, evidence, "
        "competitors, news, and recent information. Input: a focused search query."
    )
    args_schema: Type[BaseModel] = DuckDuckGoSearchInput
    max_results: int = 6

    def _run(self, query: str) -> str:  # type: ignore[override]
        try:
            from ddgs import DDGS
        except ImportError:
            return "ERROR: the `ddgs` package is not installed."

        try:
            with DDGS() as ddg:
                results = list(ddg.text(query, max_results=self.max_results))
        except Exception as e:  # noqa: BLE001
            return f"ERROR running DuckDuckGo search: {type(e).__name__}: {e}"

        if not results:
            return f"No results found for query: {query}"

        lines = [f"Search results for: {query}\n"]
        for i, r in enumerate(results, start=1):
            title = (r.get("title") or "").strip()
            url = (r.get("href") or r.get("url") or "").strip()
            snippet = (r.get("body") or r.get("snippet") or "").strip()
            lines.append(f"{i}. {title}\n   URL: {url}\n   {snippet}\n")
        return "\n".join(lines)
