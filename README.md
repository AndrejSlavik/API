## Python RESTful API Service

Used for managing posts by users.

Basic **CRUD** operations.

**Swagger** as API documentation.

## Installation

The whole project was coded in Intellij IDEA IDE using high performance web framework **FAST API** running on ASGI Python web server **Uvicorn**.

1) Install **Intellij IDEA**
2) Download and install **Python Community Edition** plugin and connect it to your project
3) Download Python libraries: **fastapi, pydantic, uvicorn and typing**

## First start

To start the project, simply type in Intellij terminal the following script:

`uvicorn {name of python file without extention}:{name of FAST API variable} --reload`

Example: `uvicorn main:app --reload`

This script starts a server process running on **localhost** (http://127.0.0.1:8000 or http://localhost:8000) to view in web browser using **Swagger**.

`--reload` ensures that server is keep refreshing after every change.


Using `/docs` extention in URL you can view all the API documentation available. (http://127.0.0.1:8000/docs)