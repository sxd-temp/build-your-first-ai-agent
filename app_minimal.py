"""The smallest possible Streamlit wrapper around your crew.

✅ PROVIDED (teaching aid). We read this together in Hour 4 to see how a UI
   wraps your agents: an input, a button, call build_crew(), show the result.
   The full, polished version lives in app.py — run that one for the real app.

   Run it:  streamlit run app_minimal.py
"""
import os

import streamlit as st
from dotenv import load_dotenv

from src.crew import build_crew

load_dotenv()

st.title("🎯 Startup Idea Validator (minimal)")
st.caption("Three agents research, debate, and write a decision memo.")

idea = st.text_area("Describe your startup idea")

if st.button("Validate Idea", type="primary"):
    if not os.getenv("GEMINI_API_KEY"):
        st.error("Add your GEMINI_API_KEY to a .env file first (see .env.example).")
    elif not idea.strip():
        st.warning("Type an idea first.")
    else:
        with st.spinner("Three agents are researching and debating… (about 1–3 minutes)"):
            crew = build_crew(idea=idea.strip())
            result = crew.kickoff()
        st.markdown("## 🎯 Validation Memo")
        st.markdown(str(result))
