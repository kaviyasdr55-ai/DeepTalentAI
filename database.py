import sqlite3

def get_connection():
    connection = sqlite3.connect("deeptalent.db")
    connection.row_factory = sqlite3.Row
    return connection

def initialize_database():
    connection = get_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS candidates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            filename TEXT,
            selected_role TEXT,
            talent_score REAL,
            skills TEXT
        )
    """)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    initialize_database()
    print("DeepTalent database initialized.")
