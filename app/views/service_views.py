from flask import Blueprint, render_template

service_bp = Blueprint('service', __name__)

@service_bp.route('/')
def index():
    return render_template('services.html', title='Services')
