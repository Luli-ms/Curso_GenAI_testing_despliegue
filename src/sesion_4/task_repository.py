import sqlite3


def init_db(db_path="tasks.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def add_task(title: str, status: str = "pending", db_path="tasks.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tasks (title, status) VALUES (?, ?)",
        (title, status)
    )
    conn.commit()
    conn.close()


def get_all_tasks(db_path="tasks.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, status FROM tasks")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_tasks_by_status(status: str, db_path="tasks.db"):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, title, status FROM tasks WHERE status = ?",
        (status,)
    )
    rows = cursor.fetchall()
    conn.close()
    return rows