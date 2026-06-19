from flask import Flask, jsonify, request

app = Flask(__name__)

INITIAL_TODOS = [
    {"id": 1, "title": "Learn Git", "done": False},
    {"id": 2, "title": "Start CI/CD plan", "done": False},
]

todos = [todo.copy() for todo in INITIAL_TODOS]


@app.route("/")
def home():
    return {"message": "To-do API is running"}


@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)


@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo["id"] == todo_id), None)

    if todo is None:
        return jsonify({"error": "Todo not found"}), 404

    return jsonify(todo)


@app.route("/todos", methods=["POST"])
def create_todo():
    data = request.get_json()

    if not data or "title" not in data or not data["title"].strip():
        return jsonify({"error": "Title is required"}), 400

    new_todo = {
        "id": max((todo["id"] for todo in todos), default=0) + 1,
        "title": data["title"].strip(),
        "done": False,
    }

    todos.append(new_todo)
    return jsonify(new_todo), 201


if __name__ == "__main__":
    app.run(debug=True)