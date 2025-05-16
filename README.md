# Flask Blog System

This project is a simple web application for creating and managing blog posts. It is built using Python, the Flask framework, and SQLAlchemy for database management (using SQLite).

## Features

* Create new blog posts via a web form
* View a list of all blog posts on the index page
* View individual blog posts
* Edit existing blog posts
* Delete blog posts
* Uses SQLite as the database
* Includes a database model for blog posts

## Technologies Used

* Python
* Flask
* SQLAlchemy
* SQLite
* `render_template` (Flask)
* `request` (Flask)
* `redirect` (Flask)
* `url_for` (Flask)
* `abort` (Werkzeug, used by Flask)
* `os` (Python standard library)
* HTML, CSS for templates

## Setup and Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/Tasfiul/Flask-blog
    ```
2.  Navigate to the project directory:
    ```bash
    cd Flask-blog
    ```
3.  Create a virtual environment (recommended) and activate it:
    ```bash
    python -m venv venv
    # On Windows: venv\Scripts\activate
    # On macOS/Linux: source venv/bin/activate
    ```
4.  Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5.  Set up the database:
   # The databaase and tables will be automatically created when run
## How to Run

1.  Make sure your virtual environment is activated.
2.  Set the `FLASK_APP` environment variable to point to your application instance :
    ```powershell
    # On Windows (PowerShell)
    $env:FLASK_APP = "hello_app.webapp:app"
    ```
3.  Run the Flask application:
    ```bash
    flask run
    ```
    The blog will be available at `http://127.0.0.1:5000/`.
## Routes

* **GET /** : Homepage displaying a list of blog posts.
* **GET /post/<int:post_id>** : View a single blog post.
* **GET /create** : Display the form to create a new blog post.
* **POST /create** : Handle form submission to create a new blog post.
* **GET /edit/<int:post_id>** : Display the form to edit an existing blog post.
* **POST /edit/<int:post_id>** : Handle form submission to update an existing blog post.
* **POST /delete/<int:post_id>** : Handle the request to delete a blog post.
* **/add-sample-data** : Creats 2 sample data. 
    
