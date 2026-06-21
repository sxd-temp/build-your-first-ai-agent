"""Lab 3 checkpoint — run the full three-agent crew.

Builds the whole crew (Optimist → Skeptic → Strategist, wired by your fan-in) and
shows the Bull case, Bear case, and final Memo — so you can confirm the Strategist
really reads BOTH cases.

✅ PROVIDED — run this to check your filled-in Lab 3 work. You don't edit it.

   Run it (from the project root):  streamlit run test_apps/lab3_full_crew.py
"""
import os
import sys
from pathlib import Path

# This app lives in test_apps/, but it imports the root-level src/ package.
# Add the project root to the import path so `src` resolves.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import streamlit as st
from dotenv import load_dotenv

from src import LabTODO
from src.crew import build_crew

load_dotenv()

st.set_page_config(page_title="Lab 3 — Full crew", page_icon="🎯")
st.title("Lab 3 — Full crew")
st.caption("Runs the whole pipeline and shows all three outputs, so you can confirm the fan-in works.")

DEFAULT_IDEA = "TutorVoice: retired teachers tutor kids over voice chat, paid by the minute."
idea = st.text_area("Startup idea", value=DEFAULT_IDEA)

if st.button("Run the full crew", type="primary"):
    if not os.getenv("GEMINI_API_KEY"):
        st.error("Add your GEMINI_API_KEY to a .env file first (see .env.example).")
    elif not idea.strip():
        st.warning("Type an idea first.")
    else:
        try:
            with st.spinner("Three agents are researching and debating… (about 1–3 minutes)"):
                crew = build_crew(idea=idea.strip())
                result = crew.kickoff()
            outs = [str(t.raw) for t in result.tasks_output]
            tab_memo, tab_bull, tab_bear = st.tabs(["🎯 Memo", "🚀 Bull Case", "🔪 Bear Case"])
            with tab_memo:
                st.markdown(outs[2] if len(outs) > 2 else str(result))
            with tab_bull:
                st.markdown(outs[0] if len(outs) > 0 else "No bull case.")
            with tab_bear:
                st.markdown(outs[1] if len(outs) > 1 else "No bear case.")
        except LabTODO as e:
            # Lab 3 (or Lab 2) isn't finished yet — show the prompt instead of a crash.
            st.warning(str(e))
