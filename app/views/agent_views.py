from flask import Blueprint, render_template

agent_bp = Blueprint('agent', __name__)

@agent_bp.route('/')
def index():
    return render_template('agents.html', title='Agents')
