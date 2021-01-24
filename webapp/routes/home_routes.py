# web_app/routes/home_routes.py

# Import packages
from flask import Blueprint, render_template

# Define home_routes
home_routes = Blueprint("home_routes", __name__)

# Root route


@home_routes.route("/")
def index():
    return render_template('index.html')

# About me route


@home_routes.route("/about")
def about_me():
    return render_template('about.html')
