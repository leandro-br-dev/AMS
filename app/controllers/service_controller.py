from flask import Blueprint, request, jsonify
from app.models import Service
from app.utils.database import db
from sqlalchemy.exc import SQLAlchemyError

service_api_bp = Blueprint('service_api_bp', __name__)

# Create a new service
@service_api_bp.route('/services', methods=['POST'])
def create_service():
    data = request.json
    try:
        new_service = Service(
            service_name=data['service_name'],
            service_type=data['service_type'],
            endpoint_url=data['endpoint_url'],
            authentication=data.get('authentication'),
            input_schema=data['input_schema'],
            output_schema=data['output_schema']
        )
        db.session.add(new_service)
        db.session.commit()
        return jsonify({"message": "Service created", "service": new_service.service_id}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Retrieve all services
@service_api_bp.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        return jsonify([service.to_dict() for service in services]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Retrieve a single service by ID
@service_api_bp.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        return jsonify(service.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

# Update a service by ID
@service_api_bp.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    data = request.json
    try:
        service = Service.query.get_or_404(service_id)
        service.service_name = data['service_name']
        service.service_type = data['service_type']
        service.endpoint_url = data['endpoint_url']
        service.authentication = data.get('authentication')
        service.input_schema = data['input_schema']
        service.output_schema = data['output_schema']
        db.session.commit()
        return jsonify({"message": "Service updated", "service": service.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

# Delete a service by ID
@service_api_bp.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        return jsonify({"message": "Service deleted"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
