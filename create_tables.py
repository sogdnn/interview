import sqlite3

# Connect to database (creates the file if it doesn't exist)
conn = sqlite3.connect("interview_app.db")
cursor = conn.cursor()


# USERS

cursor.execute("""
    CREATE TABLE IF NOT EXISTS USERS (
        user_id   INTEGER PRIMARY KEY,
        name      VARCHAR(100),
        email     VARCHAR(100),
        password  VARCHAR,
        level     VARCHAR(50)
    )
""")


# JOB_ROLES

cursor.execute("""
    CREATE TABLE IF NOT EXISTS JOB_ROLES (
        role_id     INTEGER PRIMARY KEY,
        role_name   VARCHAR(100),
        category    VARCHAR(100),
        description TEXT
    )
""")


# QUESTIONS

cursor.execute("""
    CREATE TABLE IF NOT EXISTS QUESTIONS (
        question_id INTEGER PRIMARY KEY,
        role_id     INTEGER,
        difficulty  VARCHAR,
        question    TEXT,
        FOREIGN KEY (role_id) REFERENCES JOB_ROLES(role_id)
    )
""")


# INTERVIEWS

cursor.execute("""
    CREATE TABLE IF NOT EXISTS INTERVIEWS (
        interview_id   INTEGER PRIMARY KEY,
        user_id        INTEGER,
        role_id        INTEGER,
        score          INTEGER,
        interview_date DATE,
        difficulty     VARCHAR,
        FOREIGN KEY (user_id)  REFERENCES USERS(user_id),
        FOREIGN KEY (role_id)  REFERENCES JOB_ROLES(role_id)
    )
""")


# ANSWER_ANALYSIS

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ANSWER_ANALYSIS (
        analysis_id    INTEGER PRIMARY KEY,
        interview_id   INTEGER,
        confidence     INTEGER,
        grammar_score  INTEGER,
        ai_feedback    TEXT,
        FOREIGN KEY (interview_id) REFERENCES INTERVIEWS(interview_id)
    )
""")

# ADAPTIVE_ENGINE

cursor.execute("""
    CREATE TABLE IF NOT EXISTS ADAPTIVE_ENGINE (
        engine_id       INTEGER PRIMARY KEY,
        interview_id    INTEGER,
        current_level   INTEGER,
        next_difficulty VARCHAR,
        FOREIGN KEY (interview_id) REFERENCES INTERVIEWS(interview_id)
    )
""")


# SKILL_PROGRESS

cursor.execute("""
    CREATE TABLE IF NOT EXISTS SKILL_PROGRESS (
        progress_id   INTEGER PRIMARY KEY,
        user_id       INTEGER,
        communication INTEGER,
        technical     INTEGER,
        confidence    INTEGER,
        FOREIGN KEY (user_id) REFERENCES USERS(user_id)
    )
""")

# Save changes and close
conn.commit()
conn.close()

print("All tables created successfully in interview_app.db")
