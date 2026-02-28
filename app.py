from flask import Flask, render_template, abort
import os

app = Flask(__name__)

# Temporary blog data (acts like database for now)
posts = [
    {
        "title": "My First Flask Blog",
        "slug": "first-fla",
        "content": "This is my first dynamic blog post built with Flask!"
    },
    {
        "title": "Learning Backend Development",
        "slug": "learning-backend",
        "content": "Understanding routing, templates and debugging."
    }
]

# ---------------- HOME ----------------
""" @app.route("/")
def home():
    return render_template("blog/home.html")  """ 

# ---------------- BLOG LIST ----------------
@app.route("/blog")
def blog():
    return render_template("blog/blog_list.html", posts=posts)

# ---------------- BLOG DETAIL ----------------
@app.route("/blog/<slug>")
def blog_detail(slug):
    post = next((p for p in posts if p["slug"] == slug), None)
    if post is None:
        abort(404)
    return render_template("blog/blog_detail.html", post=post)

# ---------------- OTHER PAGES ----------------

@app.route("/projects")
def projects():
    return render_template("blog/projects.html")

@app.route("/about")
def about():
    return render_template("blog/about.html")

@app.route("/contact")
def contact():
    return render_template("blog/contact.html")

@app.route("/")
def home():
    # Show latest 3 posts
    latest_posts = posts[:3]
    return render_template("blog/home.html", latest_posts=latest_posts)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 3000))
    app.run(host="0.0.0.0", port=port, debug=True)