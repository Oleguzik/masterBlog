# Master Blog

A simple Flask-based blog application with CRUD operations and a like feature.

## Features

- View blog posts
- Add new posts
- Update existing posts
- Delete posts
- Like posts

## Installation

1. Clone the repository
2. Install Flask: `pip install flask`
3. Run the app: `python app.py`
4. Open `http://127.0.0.1:5000` in your browser

## Structure

- `app.py`: Main Flask application
- `data/articles.json`: Blog posts data
- `templates/`: HTML templates
- `static/`: CSS styles

## Routes

- `/`: Home page with all posts
- `/add`: Add new post (GET/POST)
- `/update/<id>`: Update post (GET/POST)
- `/delete/<id>`: Delete post
- `/like/<id>`: Like a post