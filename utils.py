import sqlite3
from contextlib import closing
from pathlib import Path


DATABASE_PATH = Path(__file__).resolve().parent / "banco.db"


def _create_note_table(connection):
    connection.execute("""
        CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
    """)

def load_data(nome_arquivo):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            _create_note_table(connection)
            rows = connection.execute(
                "SELECT id, title, content FROM note ORDER BY id"
            ).fetchall()

    return [
        {"id": note_id, "titulo": title, "detalhes": content}
        for note_id, title, content in rows
    ]

def load_template(nome_template):
    template_dir = f"static/templates/{nome_template}"
    with open(template_dir, encoding="utf-8") as template_file:
        return template_file.read()

def add_note(nova_anotacao):
    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            _create_note_table(connection)
            connection.execute(
                "INSERT INTO note (title, content) VALUES (?, ?)",
                (nova_anotacao["titulo"], nova_anotacao["detalhes"]),
            )
