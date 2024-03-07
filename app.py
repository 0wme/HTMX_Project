from os import name

from flask import Flask, rendertemplate, request, redirect, urlfor, url_for

app = Flask(name)

todos = []  # Exemple: [{'content': 'Faire les courses', 'completed': False, 'favorite': False}]

@app.route('/')
def todolist():
    return rendertemplate('todo_list.html', todos=todos)


if __name__ == '__main':
    app.run(debug=True)