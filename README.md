# Phase-4-Code-Challenge-Late-Show

This project is a Flask application designed to manage episodes and guests of a late-night show. It provides a RESTful API for CRUD operations on episodes, guests, and their appearances. This README will guide you through the setup and usage of the application, as well as give you an understanding of the code structure and how to test the API.

## Table of Contents

- [Project Overview](#project-overview)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Contributing](#contributing)

## Project Overview

The Late Show API allows users to perform the following operations:

- Retrieve a list of episodes and guests.
- Get details for a specific episode, including its appearances.
- Create new appearances for guests in specific episodes.
- Validate ratings for appearances to ensure they fall within a specified range.

This project serves as a learning tool for understanding Flask, RESTful API design, SQLAlchemy for database interactions, Marshmallow for serialization, and how to structure a Python application.

## Technologies Used

- **Flask**: A micro web framework for Python.
- **Flask-SQLAlchemy**: An extension for SQLAlchemy that simplifies database operations in Flask.
- **Flask-Migrate**: An extension for handling database migrations.
- **Flask-Marshmallow**: An integration of Marshmallow for serialization/deserialization of complex data types.
- **Flask-RESTful**: An extension for building REST APIs easily.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/CGM123sherry/Phase-4-Code-Challenge-Late-Show.git
   cd server
   ```

2. **Create a virtual environment**:

   ```bash
   pyenv activate phase4env

   pipenv install

   pipenv shell
   ```

3. **Install required packages**:

```bash
-cd server

-export FLASK_APP=app.py

-export FLASK_RUN_PORT=5555
```

## Database Setup and Migration

The project uses Flask-Migrate for database migrations. Follow these steps to set up and apply migrations:

**Initialize the database migration environment:**

This will create the necessary migration directory and configuration files.

```bash
flask db init
```

Generate an initial migration:

This step will create a migration file based on your models.

```bash
flask db migrate -m "Initial migration"
```

Apply the migration:

This will apply the changes from the migration file to your database.

```bash
flask db upgrade
```

You should now have a fully set-up database with tables corresponding to the models (Episode, Guest, Appearance).

## Running the Application

To run the application, use the following command in your terminal:

```bash
python app.py
```

The application will start, and you can access the API at `http://127.0.0.1:5000`.

## API Endpoints

### Episodes

- **GET /episodes**: Retrieve a list of all episodes.

  - **Response**: JSON object containing a message and a list of episodes.
  - **HTTP Status Code**: 200 OK

- **GET /episodes/<int:id>**: Retrieve details of a specific episode by ID.
  - **Response**: JSON object containing a message and episode details.
  - **HTTP Status Code**: 200 OK, 404 Not Found

### Guests

- **GET /guests**: Retrieve a list of all guests.
  - **Response**: JSON object containing a message and a list of guests.
  - **HTTP Status Code**: 200 OK

### Appearances

- **POST /appearances**: Create a new appearance.
  - **Request Body**: JSON object containing `episode_id`, `guest_id`, and `rating`.
  - **Response**: JSON object containing a message and the created appearance.
  - **HTTP Status Code**: 201 Created, 400 Bad Request

## Testing with Postman

You can test the API using Postman. Here are the instructions for testing each endpoint:

1. **GET /episodes**

   - Method: GET
   - URL: `http://127.0.0.1:5000/episodes`
   - **Expected Response**: A JSON object with a list of all episodes.

2. **GET /episodes/<id>**

   - Method: GET
   - URL: `http://127.0.0.1:5000/episodes/1` (replace `1` with the episode ID you want to retrieve)
   - **Expected Response**: A JSON object with details of the specified episode.

3. **GET /guests**

   - Method: GET
   - URL: `http://127.0.0.1:5000/guests`
   - **Expected Response**: A JSON object with a list of all guests.

4. **POST /appearances**
   - Method: POST
   - URL: `http://127.0.0.1:5000/appearances`
   - **Request Body** (JSON):
     ```json
     {
       "episode_id": 1,
       "guest_id": 2,
       "rating": 4
     }
     ```
   - **Expected Response**: A JSON object with a success message and details of the created appearance.

## Contributing

If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit them (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a pull request.

Feel free to customize any section to better match your project's specifics or personal style!
