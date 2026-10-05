# Student CRUD API

A simple Student CRUD REST API built using FastAPI. Student records are stored in an in-memory list.

## Features

* Create a student
* Get all students
* Get a student by ID
* Update a student
* Delete a student

## Technologies

* Python
* FastAPI
* Uvicorn
* Pydantic

## Requirements

* Python installed on your system

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

## How to Run

Start the application using:

```bash
uvicorn main:app --reload
```

Open the interactive API documentation at:

http://127.0.0.1:8000/docs

**Note:** Student data is stored in memory and resets when the application restarts.
