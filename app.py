from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route('/')
def index():
    # Load articles from JSON file
    with open('articles.json', 'r') as f:
        posts = json.load(f)
    return render_template('index.html', posts=posts)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        # Load existing posts
        with open('articles.json', 'r') as f:
            posts = json.load(f)
        
        # Generate new ID
        if posts:
            new_id = max(post['id'] for post in posts) + 1
        else:
            new_id = 1
        
        # Get form data
        author = request.form.get('author')
        title = request.form.get('title')
        content = request.form.get('content')
        
        # Create new post
        new_post = {
            'id': new_id,
            'author': author,
            'title': title,
            'content': content
        }
        
        # Append to posts
        posts.append(new_post)
        
        # Save back to JSON
        with open('articles.json', 'w') as f:
            json.dump(posts, f, indent=4)
        
        # Redirect to home
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/delete/<int:post_id>')
def delete(post_id):
    # Load existing posts
    with open('articles.json', 'r') as f:
        posts = json.load(f)
    
    # Remove the post with the given id
    posts = [post for post in posts if post['id'] != post_id]
    
    # Save back to JSON
    with open('articles.json', 'w') as f:
        json.dump(posts, f, indent=4)
    
    # Redirect back to the home page
    return redirect(url_for('index'))




if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5015, debug=True)