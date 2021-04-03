from flask import Flask

# Load Environmental Variables
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "Arf!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
