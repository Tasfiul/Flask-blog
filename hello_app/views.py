from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
import os

# Create the Flask application instance
from . import app

# Configure the database
# Use SQLite 
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'blog.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# Initialize the database
db = SQLAlchemy(app)

# --- Database Model Definition ---
class BlogPost(db.Model):
    # Define the columns for the blog_post table
    id = db.Column(db.Integer, primary_key=True) # Unique ID, automatically generated
    title = db.Column(db.String(100), nullable=False) # Title, max 100 chars, cannot be empty
    content = db.Column(db.Text, nullable=False) # Content, can be longer text

    def __repr__(self):
        return '<Post %r>' % self.title

# --- Routes ---
@app.route('/')
def index():
    # Query the database to get all blog posts
    all_posts = BlogPost.query.all()

    # Render the index.html template and pass the list of posts to it
    return render_template('index.html', posts=all_posts)

# Route to view a single blog post
@app.route('/post/<int:post_id>') # Define a URL parameter for the post ID
def get_post(post_id): 
    post = BlogPost.query.get(post_id)

    # If no post was found with that ID, return a 404 Not Found error
    if not post: #
        abort(404)

    # Render the post.html template and pass the single post object to it
    return render_template('post.html', post=post) # Pass the found post as a variable named 'post'

@app.route('/add-sample-data')
def add_sample_data():
    # Create new BlogPost objects
    new_post1 = BlogPost(title='First Post', content='This is the content of the first post.')
    new_post2 = BlogPost(title='Second Post', content='Here is the content for the second post.')

    # Add the new posts to the database session
    db.session.add(new_post1)
    db.session.add(new_post2)

    # Commit the session to save the changes to the database
    db.session.commit()

    return "Sample data added!"

# Route to display the create post form and handle form submission
@app.route('/create', methods=['GET', 'POST']) # This route handles both GET (display form) and POST (process form)
def create_post():
    if request.method == 'POST':
        # Get data from the submitted form
        post_title = request.form['title']
        post_content = request.form['content']

        # Create a new BlogPost object
        new_post = BlogPost(title=post_title, content=post_content)

        try:
            db.session.add(new_post)
            db.session.commit()
            # Redirect to the homepage after successful creation
            return redirect(url_for('index'))
        except:
            # Handle potential errors
            return "There was an issue adding your post"
    else:
        return render_template('create_post.html')

# Route to display the edit post form and handle update submission
@app.route('/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    # Find the post by ID first
    post_to_edit = BlogPost.query.get_or_404(post_id) 

    if request.method == 'POST':
        # Get updated data from the submitted form
        post_to_edit.title = request.form['title']
        post_to_edit.content = request.form['content']

        try:
            db.session.commit()
            # Redirect to the updated post's view page
            return redirect(url_for('get_post', post_id=post_to_edit.id))
        except:
            return "There was an issue updating your post"

    else: # If it's a GET request, render the edit form
        return render_template('edit_post.html', post=post_to_edit) # Pass the post object to the template

# Route to handle post deletion
@app.route('/delete/<int:post_id>', methods=['POST']) # Listens for POST requests to this URL
def delete_post(post_id):
    post_to_delete = BlogPost.query.get_or_404(post_id)

    try:
        db.session.delete(post_to_delete)
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the homepage after successful deletion
        return redirect(url_for('index'))
    except:
        return "There was a problem deleting that post"

if __name__ == '__main__':
    # Create the database tables if they don't exist yet
    with app.app_context():
        db.create_all()
    app.run(debug=True)