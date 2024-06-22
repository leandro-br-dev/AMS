from flask import Blueprint, render_template

log_bp = Blueprint('log', __name__)

@log_bp.route('/')
def index():
    return render_template('logs.html', title='Logs')
