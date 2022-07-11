from curses import flash
from flask import Flask, render_template
from config import config

app = Flask(__name__, template_folder='template')

@app.route('/')
def index():
    return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()

