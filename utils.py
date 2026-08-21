import sqlite3
from contextlib import closing

from createdb import DATABASE_PATH, create_database


def _ensure_database():
    if not DATABASE_PATH.exists():
        create_database()

def load_data(nome_arquivo):
    _ensure_database()

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
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
    _ensure_database()

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            connection.execute(
                "INSERT INTO note (title, content) VALUES (?, ?)",
                (nova_anotacao["titulo"], nova_anotacao["detalhes"]),
            )


def delete_note(note_id):
    _ensure_database()

    with closing(sqlite3.connect(DATABASE_PATH)) as connection:
        with connection:
            connection.execute("DELETE FROM note WHERE id = ?", (note_id,))
