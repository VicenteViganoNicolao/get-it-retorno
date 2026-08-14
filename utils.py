import json

def load_data(nome_arquivo):
    json_dir = f"static/data/{nome_arquivo}"
    with open(json_dir, encoding="utf-8") as json_file:
        data = json.load(json_file)
    return data

def load_template(nome_template):
    template_dir = f"static/templates/{nome_template}"
    with open(template_dir, encoding="utf-8") as template_file:
        return template_file.read()

def add_note(nova_anotacao):
    notes = load_data("notes.json")
    notes.append(nova_anotacao)

    notes_dir = "static/data/notes.json"
    with open(notes_dir, "w", encoding="utf-8") as notes_file:
        json.dump(notes, notes_file, ensure_ascii=False, indent=2)
