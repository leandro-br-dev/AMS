# app/controllers/log_controller.py
from flask import Blueprint, request, jsonify
from app.models.log import Log
from app.utils.database import db
from sqlalchemy.exc import SQLAlchemyError

log_api_bp = Blueprint('log_api_bp', __name__)

@log_api_bp.route('/logs', methods=['POST'])
def create_log():
    data = request.json
    try:
        new_log = Log(
            flow_id=data['flow_id'],
            execution_status=data['execution_status'],
            input_data=data['input_data'],
            output_data=data['output_data'],
            error_message=data.get('error_message')
        )
        db.session.add(new_log)
        db.session.commit()
        return jsonify({"message": "Log created", "log": new_log.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@log_api_bp.route('/logs', methods=['GET'])
def get_logs():
    try:
        logs = Log.query.all()
        return jsonify([log.to_dict() for log in logs]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@log_api_bp.route('/logs/<int:log_id>', methods=['GET'])
def get_log(log_id):
    try:
        log = Log.query.get_or_404(log_id)
        return jsonify(log.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@log_api_bp.route('/logs/<int:log_id>', methods=['PUT'])
def update_log(log_id):
    data = request.json
    try:
        log = Log.query.get_or_404(log_id)
        log.execution_status = data['execution_status']
        log.input_data = data['input_data']
        log.output_data = data['output_data']
        log.error_message = data.get('error_message')
        db.session.commit()
        return jsonify({"message": "Log updated", "log": log.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@log_api_bp.route('/logs/<int:log_id>', methods=['DELETE'])
def delete_log(log_id):
    try:
        log = Log.query.get_or_404(log_id)
        db.session.delete(log)
        db.session.commit()
        return jsonify({"message": "Log deleted"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
