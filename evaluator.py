from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

print("KEY FOUND:", os.getenv("GROQ_API_KEY") is not None)

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def evaluate_answer(question, answer):

 prompt = f"""
You are a professional technical interviewer.

Question:
{question}

Candidate Answer:
{answer}

Provide feedback in EXACTLY this format:

Score: X/10

Strengths:
- point 1
- point 2

Weaknesses:
- point 1
- point 2

Improvement Tips:
- point 1
- point 2
"""