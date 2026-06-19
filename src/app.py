from flask import Flask, jsonify

app = Flask(__name__)

todos = [
    {"id": 1, "title": "Learn Git", "done": False},
    {"id": 2, "title": "Start CI/CD plan", "done": False},
]


@app.route("/")
def home():
    return {"message": "To-do API is running"}


@app.route("/todos")
def get_todos():
    return jsonify(todos)


if __name__ == "__main__":
    app.run(debug=True)