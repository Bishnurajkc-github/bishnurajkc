from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculator')
def calculator_page():
    return render_template('calculator.html')

@app.route('/blog')
def blog_page():
    return render_template('blog.html')

if __name__ == "__main__":
    app.run(debug=True)
