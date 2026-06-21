"""Lab 1 checkpoint — test your agent in a tiny web UI.

Same agent you edit in hello_agent.py, just wrapped in Streamlit so you can
type a question and watch YOUR version answer.

✅ PROVIDED — run this to check your filled-in Lab 1 work. You don't edit it.

   Run it (from the project root):  streamlit run test_apps/lab1_meet_your_agent.py
"""
import os
import sys
from pathlib import Path

# This app lives in test_apps/, but it imports project files from the root
# (hello_agent.py and the src/ package). Add the project root to the import path.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from dotenv import load_dotenv
from crewai import Task, Crew

from hello_agent import researcher  # the agent you customize in Lab 1

load_dotenv()

st.set_page_config(page_title="Lab 1 — Meet your agent", page_icon="🤖")
st.title("Lab 1 — Meet your agent")
st.caption(f"Current role:  {researcher.role}")

question = st.text_input(
    "Ask your agent a question",
    value="What are the 3 biggest AI agent trends in 2026?",
)

if st.button("Ask your agent", type="primary"):
    if not os.getenv("GEMINI_API_KEY"):
        st.error("Add your GEMINI_API_KEY to a .env file first (copy .env.example to .env).")
    elif not question.strip():
        st.warning("Type a question first.")
    else:
        with st.spinner("Your agent is thinking and searching the web…"):
            task = Task(
                description=question.strip(),
                expected_output="A clear answer with a short list of source URLs at the end.",
                agent=researcher,
            )
            result = Crew(agents=[researcher], tasks=[task], verbose=True).kickoff()
        st.markdown("### Answer")
        st.markdown(str(result))
