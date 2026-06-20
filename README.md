# Python CI/CD Learning Project

A simple To-do API built with Flask to practice CI/CD step by step.

## Features
- Check if the API is running
- Get all todos
- Get one todo by ID
- Create a new todo

## Tech stack
- Python
- Flask
- pytest
- Git
- GitHub

## Project structure
- `src/` — application code
- `tests/` — automated tests
- `docs/` — daily learning notes

## API routes

### `GET /`
Returns a simple message showing the API is running.

### `GET /todos`
Returns the list of todos.

### `GET /todos/<id>`
Returns one todo by ID.

### `POST /todos`
Creates a new todo.

Example request body:
```json
{
  "title": "Learn Docker"
}