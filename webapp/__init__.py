# webapp/__init__.py

# Import Packages
import os
from flask import Flask
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define create_app
"""
Primary Flask Create_App Function
"""


def create_app():
    app = Flask(__name__)
    return app


if __name__ == '__main__':
    my_app = create_app()
    my_app.run(debug=True)