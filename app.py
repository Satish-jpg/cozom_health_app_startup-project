from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Vercel!"

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/contact')
def contact():
    return "Contact us at contact@cozom.in"

if __name__ == "__main__":
    app.run()
