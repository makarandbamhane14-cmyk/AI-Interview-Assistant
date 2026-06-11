import streamlit as st

st.set_page_config(
    page_title="AI Interview Assistant",
    page_icon="🎯"
)

st.title("🎯 AI Interview Preparation Assistant")

st.write(
    "Practice interviews and receive AI-powered feedback."
)

interview_type = st.selectbox(
    "Select Interview Type",
    [
        "HR",
        "AI/ML",
        "Electronics"
    ]
)

st.write("Selected:", interview_type)