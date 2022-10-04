from flask import Flask, render_template, request, redirect, url_for
import random
# from flask_sqlalchemy import SQLAlchemy

# Creating a Flask app
app = Flask(__name__)

# Todo class
# Schema: 
#   Todo has attributes id (int), title (str), complete (bool), and priority (string, high|low|medium)
class Todo():
    def __init__(self, id, title, complete, priority):
        self.id = id
        self.title = title
        self.complete = complete
        self.priority = priority 

# Internal "database" for todos
todo_list = {}
ids = set()

# Defining base route
@app.route('/')
def home():
    # rendering HTML
    return render_template("base.html", todo_list=todo_list)

@app.route("/add", methods=["POST"])
def add():

    # Put together information for adding a new todo
    title = request.form.get("title")
    priority = request.form.get("priority")
    id = generateId()
    new_todo = Todo(id=id, title=title, complete=False, priority=priority)
    todo_list[id] = new_todo

    return redirect(url_for("home"))

# Generate a random ID recursively
def generateId():
    temp_id = random.randint(0,1000)
    if temp_id not in ids:
        ids.add(temp_id)
        return temp_id
    else:
        return generateId()


# Update a todo
@app.route("/update/<int:todo_id>")
def update(todo_id):
    todo = todo_list[todo_id]
    todo.complete = not todo.complete
    return redirect(url_for("home"))


# Delete specific todo
@app.route("/delete/<int:todo_id>")
def delete(todo_id):
    ids.remove(todo_id)
    del todo_list[todo_id]
    return redirect(url_for("home"))

# Delete completed todos
@app.route("/deleteall")
def deleteall():
    delete_indices = []
    for todo_id, todo in todo_list.items():
        if todo.complete == True:
            delete_indices.append(todo_id)
    
    for i in range(len(delete_indices)):
        curr_id = delete_indices[i]
        del todo_list[curr_id]
    return redirect(url_for("home"))

# Setting debug to true so that I don't have to reload the server to debug
if __name__ == "__main__": 
    app.run(debug=True, host="0.0.0.0", port=3000)
