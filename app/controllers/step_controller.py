from flask import Blueprint, request, jsonify
from app.models import Step
from app.utils.database import db

step_api_bp = Blueprint('step_api_bp', __name__)

@step_api_bp.route('/steps', methods=['POST'])
def create_step():
    data = request.get_json()
    new_step = Step(
        flow_id=data['flow_id'],
        agent_id=data['agent_id'],
        step_number=data['step_number'],
        instructions=data['instructions']
    )
    db.session.add(new_step)
    db.session.commit()
    return jsonify(new_step.to_dict()), 201

@step_api_bp.route('/steps/<int:step_id>', methods=['GET'])
def get_step(step_id):
    step = Step.query.get_or_404(step_id)
    return jsonify(step.to_dict())

@step_api_bp.route('/steps/<int:step_id>', methods=['PUT'])
def update_step(step_id):
    step = Step.query.get_or_404(step_id)
    data = request.get_json()
    step.agent_id = data['agent_id']
    step.step_number = data['step_number']
    step.instructions = data['instructions']
    db.session.commit()
    return jsonify(step.to_dict())

@step_api_bp.route('/steps/<int:step_id>', methods=['DELETE'])
def delete_step(step_id):
    step = Step.query.get_or_404(step_id)
    db.session.delete(step)
    db.session.commit()
    return '', 204

@step_api_bp.route('/steps', methods=['GET'])
def get_steps():
    flow_id = request.args.get('flow_id')
    if flow_id:
        steps = Step.query.filter_by(flow_id=flow_id).order_by(Step.step_number).all()
    else:
        steps = Step.query.all()
    return jsonify([step.to_dict() for step in steps])
