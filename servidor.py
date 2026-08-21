from flask import Flask, render_template_string, request, redirect
import views

app = Flask(__name__)

NOTE_TEMPLATE = '''  <li>
    <h3>{title}</h3>
    <p>{details}</p>
  </li>
'''

RESPONSE_TEMPLATE = '''<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Get-it</title>
</head>
<body>

<img src="{{{{ url_for('static', filename='img/logo-getit.png') }}}}">
<p>Como o Post-it, mas com outro verbo</p>

<ul>
{notes}
</ul>

</body>

</html>
'''

# Configurando a pasta de arquivos estáticos
app.static_folder = 'static'


@app.route('/')
def index():
  return render_template_string(views.index())

@app.route('/submit', methods=['GET', 'POST'])
def submit_form():
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        detalhes = request.form.get('detalhes')

        views.submit(titulo, detalhes)
    return redirect('/')


@app.route('/delete/<int:note_id>')
def delete_note(note_id):
    views.delete(note_id)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
