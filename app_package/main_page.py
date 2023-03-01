from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def first_page():

    return render_template('first_page.html')
