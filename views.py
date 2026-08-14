from utils import add_note, load_data, load_template

def index():
  # Cria uma lista de <li>'s para cada anotação
  # Se tiver curiosidade: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions
  notes_li = []
  for dados in load_data('notes.json'):
    note_li = load_template('components/note.html').format(title=dados['titulo'], details=dados['detalhes'])
    notes_li.append(note_li)
  notes = '\n'.join(notes_li)

  response = load_template('index.html').format(notes=notes)

  return response

def submit(titulo, detalhes):
  params = {
    'titulo': titulo,
    'detalhes': detalhes,
  }
  add_note(params)
