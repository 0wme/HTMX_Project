from os import name

from flask import Flask, rendertemplate, request, redirect, urlfor, url_for

app = Flask(name)

todos = []  # Exemple: [{'content': 'Faire les courses', 'completed': False, 'favorite': False}]

@app.route('/')
def todolist():
    return rendertemplate('todo_list.html', todos=todos)
@app.route('/add', methods=['POST'])
def add_todo():
    todo_content = request.form.get('content')
    if todo_content:
        todos.append({'content': todo_content, 'completed': False, 'favorite': False})
    return redirect(url_for('todo_list'))

@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id]['completed'] = not todos[todo_id]['completed']
    return redirect(url_for('todo_list'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    if 0 <= todo_id < len(todos):
        del todos[todo_id]
    return redirect(url_for('todo_list'))

@app.route('/favorite/<int:todo_id>', methods=['POST'])
def favorite_todo(todo_id):
    if 0 <= todo_id < len(todos):
        todos[todo_id]['favorite'] = not todos[todo_id]['favorite']
        if todos[todo_id]['favorite']:
            todo = todos.pop(todo_id)
            todos.insert(0, todo)  # Déplace la tâche en haut de la liste
    return redirect(url_for('todo_list'))

@app.route('/reset', methods=['POST', 'GET'])
def reset_todos():
    global todos
    todos = []  # Réinitialiser la liste des tâches
    return redirect(url_for('todo_list'))

if __name__ == '__main':
    app.run(debug=True)