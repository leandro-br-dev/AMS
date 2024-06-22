from flask import Blueprint, render_template

flow_bp = Blueprint('flow', __name__)

@flow_bp.route('/')
def index():
    return render_template('flows.html', title='Flows')
