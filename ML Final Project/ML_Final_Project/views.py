"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from ML_Final_Project import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Contact Page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='About Page.'
    )

@app.route('/HyperParameters')
def HyperParameters():
    """Renders the Hyper Parameters page."""
    return render_template(
        'HyperParameters.html',
        title='Hyper Parameters',
        year=datetime.now().year,
        message='Hyper Parameters Research Showcase'
    )

@app.route('/FirstBuild')
def FirstBuild():
    """Renders the First Build page."""
    return render_template(
        'FirstBuild.html',
        title='Hyper Parameters',
        year=datetime.now().year,
        message='Hyper Parameters Research Showcase'
    )

@app.route('/SecondBuild')
def SecondBuild():
    """Renders the Second Build page."""
    return render_template(
        'SecondBuild.html',
        title='Hyper Parameters',
        year=datetime.now().year,
        message='Hyper Parameters Research Showcase'
    )
@app.route('/ThirdBuild')
def ThirdBuild():
    """Renders the First Build page."""
    return render_template(
        'ThirdBuild.html',
        title='Hyper Parameters',
        year=datetime.now().year,
        message='Hyper Parameters Research Showcase'
    )
