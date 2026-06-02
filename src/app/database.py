import sqlite3
from . models import Transcation


DB_FIlE = 'budget.db'


def get_db_connection():
    """Establish the connection to the SQLite database."""
    conn = sqlite3.connect(DB_FIlE)
    # Returns rows as objects that behave like dictionaries
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Initializes the database and create the transcation table if it doesn't exist"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transcations(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   type TEXT NOT NULL CHECK(type IN('revenue','expense')),
                   description TEXT NOT NULL,
                   amount REAL NOT NULL,
                   date TEXT NOT NULL
                   )

    """)

    conn.commit()
    conn.close()
    print("Datbase initialize")


def add_transcation(transcation: Transcation):
    """Add a new transcationm to the database"""
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO transcations (type,description,amount,date)
                    VALUES(?,?,?,?)  """,
                   (transcation.type, transcation.description,
                    transcation.amount, transcation.date)
                   )

    conn.commit()
    conn.close()
    print(f"{transcation.type.capitalize()} added sucessfully")


def get_all_transactions():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transcations ORDER BY date DESC")
    rows = cursor.fetchall()
    conn.commit()
    conn.close()

    transcations = [
        Transcation(id=row['id'], type=row['type'], description=row['description'],
                    amount=row['amount'], date=row['date'])
        for row in rows
    ]
    return transcations
