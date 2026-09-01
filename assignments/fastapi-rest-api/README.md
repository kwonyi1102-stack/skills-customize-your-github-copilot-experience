# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API with the FastAPI framework. Practice creating HTTP endpoints, validating request data with Pydantic, and returning structured JSON responses.

## 📝 Tasks

### 🛠️ Create the FastAPI Application

#### Description

Complete the application setup in `starter-code.py` and run it with Uvicorn. Explore the automatic interactive documentation that FastAPI generates for the API.

#### Requirements

Completed program should:

- Create a FastAPI application instance.
- Start successfully with `uvicorn starter-code:app --reload`.
- Provide a `GET /docs` page with interactive API documentation.

### 🛠️ Add Read Endpoints

#### Description

Create endpoints that allow clients to retrieve all tasks and retrieve one task by its ID from the in-memory task list.

#### Requirements

Completed program should:

- Return all tasks as JSON from `GET /tasks`.
- Return one task from `GET /tasks/{task_id}` when the ID exists.
- Return an appropriate `404` response when a task ID does not exist.

### 🛠️ Add and Validate Tasks

#### Description

Use a Pydantic model to validate new task data, then add a `POST` endpoint that stores valid tasks and returns the created task.

#### Requirements

Completed program should:

- Define a request model with a required non-empty `title` and a `completed` value that defaults to `False`.
- Add a new task through `POST /tasks` and assign it a unique integer ID.
- Return the created task as JSON with a successful `201` response.
- Reject invalid request data through FastAPI validation.
