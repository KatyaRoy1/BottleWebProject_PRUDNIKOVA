"""
Routes and views for the bottle application.
"""

from bottle import route, view
from datetime import datetime

@route('/')
@route('/home')
@view('Home')
def home():
    """Renders the home page."""
    return dict(
        year=datetime.now().year
    )

@route('/user_review')
@view('user_review')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/Characters')
@view('Characters')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )

@route('/Short')
@view('Short')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/Current_novelties')
@view('Current_novelties')
def about():
    """Renders the about page."""
    return dict(
        title='About',
        message='Your application description page.',
        year=datetime.now().year
    )

@route('/Reviews')
@view('Reviews')
def contact():
    """Renders the contact page."""
    return dict(
        title='Contact',
        message='Your contact page.',
        year=datetime.now().year
    )
@route('/activeUsers')
@view('activeUsers')
def activeUsers():
    """Renders the contact page."""
    return dict(
        title='Activity users',
        message='Your contact page.',
        year=datetime.now().year
    )