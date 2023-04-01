# app.py
from flask import Flask, render_template
from urls import get_urls

app = Flask(__name__)

@app.route('/')
def index():
    urls = get_urls()
    return render_template('index.html', urls=urls)

if __name__ == '__main__':
    app.run()
