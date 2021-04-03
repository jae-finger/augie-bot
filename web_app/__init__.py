from flask import Flask

# Load Environmental Variables
from dotenv import load_dotenv

load_dotenv()


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        return "Arf!"

    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)
