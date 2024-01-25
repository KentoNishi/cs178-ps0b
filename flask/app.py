from flask import Flask, request, render_template, redirect, url_for

# concept: flask app. this is the main object that represents the flask application.
app = Flask(__name__)

todos = []

# concept: routes.
@app.route('/')
def index():
    # concept: templates. these are html files which have placeholders for dynamic content.
    return render_template('base.html', todos=todos)

# concept: routes with form parameters through POST.
@app.route('/add', methods=['POST'])
def add_todo():
    todo_item = request.form.get('todo_item')
    if todo_item:
        todos.append({'task': todo_item, 'completed': False})
    # concept: redirects. this refreshes the data displayed on the page by redirecting to the index route.
    return redirect(url_for('index'))

# concept: routes with parameters through GET (with variables in the url path).
@app.route('/remove/<int:index>')
def remove_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return redirect(url_for('index'))

@app.route('/complete/<int:index>')
def complete_todo(index):
    if 0 <= index < len(todos):
        todos[index]['completed'] = not todos[index]['completed']
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
