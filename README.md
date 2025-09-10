Task Manager

A full-stack Task Manager application with Flask, MySQL, and PyQt5. Users can register, log in, manage tasks, and delete their accounts via a secure API, while the desktop client provides a friendly interface to interact with tasks.

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Features

User registration and login with JWT authentication

Password hashing with Flask-Bcrypt for security

CRUD operations for tasks (create, read, update, delete)

Mark tasks as completed

Account deletion

Desktop client using PyQt5 to manage tasks easily

RESTful API design with Flask

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Tech Stack

Backend: Flask, SQLAlchemy, Flask-Migrate, Flask-JWT-Extended, Flask-Bcrypt

Database: MySQL

Frontend / Client: PyQt5 desktop application

Environment Management: Python venv, .env for configuration

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

API Endpoints

POST /auth/register – Register a new user

POST /auth/login – Log in and receive JWT

GET /auth/profile – Get current user profile

DELETE /auth/delete – Delete your account

GET /tasks/ – Get all tasks

POST /tasks/ – Add a new task

PUT /tasks/<task_id> – Update a task

DELETE /tasks/<task_id> – Delete a task

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

License

This project is licensed under the MIT License.
