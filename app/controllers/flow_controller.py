# app/controllers/flow_controller.py
from flask import Blueprint, request, jsonify
from app.models import Flow, Step
from app.utils.database import db
from sqlalchemy.exc import SQLAlchemyError

flow_api_bp = Blueprint('flow_api_bp', __name__)

@flow_api_bp.route('/flows', methods=['POST'])
def create_flow():
    data = request.json
    try:
        new_flow = Flow(
            name=data['name'],
            description=data['description'],
        )
        db.session.add(new_flow)
        db.session.commit()
        return jsonify({"message": "Flow created", "flow": new_flow.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@flow_api_bp.route('/flows', methods=['GET'])
def get_flows():
    try:
        flows = Flow.query.all()
        return jsonify([flow.to_dict() for flow in flows]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@flow_api_bp.route('/flows/<int:flow_id>', methods=['GET'])
def get_flow(flow_id):
    try:
        flow = Flow.query.get_or_404(flow_id)
        return jsonify(flow.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@flow_api_bp.route('/flows/<int:flow_id>', methods=['PUT'])
def update_flow(flow_id):
    data = request.json
    try:
        flow = Flow.query.get_or_404(flow_id)
        flow.name = data['name']      
        flow.description = data['description']
        db.session.commit()
        return jsonify({"message": "Flow updated", "flow": flow.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@flow_api_bp.route('/flows/<int:flow_id>', methods=['DELETE'])
def delete_flow(flow_id):
    try:
        flow = Flow.query.get_or_404(flow_id)
        db.session.delete(flow)
        db.session.commit()
        return jsonify({"message": "Flow deleted"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@flow_api_bp.route('/flows/<int:flow_id>/steps', methods=['GET'])
def get_flow_steps(flow_id):
    steps = Step.query.filter_by(flow_id=flow_id).order_by(Step.step_number).all()
    return jsonify([step.to_dict() for step in steps])