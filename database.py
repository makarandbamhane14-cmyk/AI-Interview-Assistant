import sqlite3

DATABASE_NAME = "interviewiq.db"


def create_database():
    """Create the InterviewIQ database and interviews table."""

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS interviews (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        candidate_name TEXT NOT NULL,

        role TEXT NOT NULL,

        question TEXT NOT NULL,

        answer TEXT NOT NULL,

        score REAL,

        feedback TEXT,

        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

    )
    """)

    conn.commit()
    conn.close()


def save_interview(candidate_name, role, question, answer, score, feedback):

    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO interviews (
        candidate_name,
        role,
        question,
        answer,
        score,
        feedback
    )

    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        candidate_name,
        role,
        question,
        answer,
        score,
        feedback
    ))

    conn.commit()
    conn.close()


def get_all_interviews():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT *
    FROM interviews
    ORDER BY created_at DESC
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows