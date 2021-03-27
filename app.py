import os
from dotenv import load_dotenv
from flask import Flask, render_template


load_dotenv()


app = Flask(__name__)


@app.route('/')
def index():
    key = os.environ.get("GOOGLE_MAPS_KEY")

    return render_template('index.html', mapsKey=key)


if __name__ == "__main__":

    app.run(debug=True, use_reloader=True)
