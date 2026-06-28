import streamlit as st
import random
import re

from questions import questions
from evaluator import evaluate_answer

st.set_page_config(
    page_title="InterviewIQ",
    page_icon="🎯"
)

# Sidebar
st.sidebar.title("🎯 InterviewIQ")

st.sidebar.info(
    """
AI-Powered Interview Preparation Platform

Features:
✔ AI Question Generator
✔ Answer Evaluation
✔ Performance Scoring
"""
)

# Main UI
st.title("🎯 InterviewIQ")

st.caption(
    "AI-Powered Interview Preparation Platform"
)

st.write(
    "Practice interviews and receive AI-powered feedback."
)

# Role Selection
interview_type = st.selectbox(
    "Select Target Role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Python Developer",
        "Electronics Engineer",
        "Embedded Systems Engineer"
    ]
)

# Generate Question
if st.button("Generate Question"):

    st.session_state.question = random.choice(
        questions[interview_type]
    )

# Display Question
if "question" in st.session_state:

    st.subheader("📌 Interview Question")

    st.write(
        st.session_state.question
    )

    answer = st.text_area(
        "Your Answer"
    )

    # Evaluate Answer
    if st.button("Evaluate Answer"):

        if answer.strip():

            with st.spinner("Evaluating..."):

                feedback = evaluate_answer(
                    st.session_state.question,
                    answer
                )

            st.subheader("📊 AI Feedback")

            # Extract score
            score_match = re.search(
                r'(\d+(?:\.\d+)?)\s*/\s*10',
                feedback
            )

            if score_match:

                score = float(
                    score_match.group(1)
                )

                st.metric(
                    "Interview Score",
                    f"{score}/10"
                )

                st.progress(
                    score / 10
                )

            st.markdown(feedback)

        else:

            st.warning(
                "Please enter an answer before evaluation."
            )