import os
import requests
from dotenv import load_dotenv
from flask import Flask, render_template

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get('SECRET_KEY')
app.config["API_HOST"] = os.environ.get('API_HOST')


@app.route('/', methods=['GET'])
def index():
    response = requests.get(
        app.config["API_HOST"],
        headers={'content-type': 'application/json'}
    )
    return render_template('index.html', response=response.json())


if __name__ == '__main__':
    app.run()
