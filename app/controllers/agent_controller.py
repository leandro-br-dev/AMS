# app/controllers/agent_controller.py
from flask import Blueprint, request, jsonify
from app.models.agent import Agent
from app.utils.database import db
from sqlalchemy.exc import SQLAlchemyError

agent_api_bp = Blueprint('agent_api_bp', __name__)

@agent_api_bp.route('/agents', methods=['POST'])
def create_agent():
    data = request.json
    try:
        new_agent = Agent(
            agent_name=data['agent_name'],
            description=data.get('description'),
            service_id=data.get('service_id'),
            input_format=data.get('input_format'),
            output_format=data.get('output_format')            
        )
        db.session.add(new_agent)
        db.session.commit()
        return jsonify({"message": "Agent created", "agent": new_agent.to_dict()}), 201
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@agent_api_bp.route('/agents', methods=['GET'])
def get_agents():
    try:
        agents = Agent.query.all()
        return jsonify([agent.to_dict() for agent in agents]), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@agent_api_bp.route('/agents/<int:agent_id>', methods=['GET'])
def get_agent(agent_id):
    try:
        agent = Agent.query.get_or_404(agent_id)
        return jsonify(agent.to_dict()), 200
    except SQLAlchemyError as e:
        return jsonify({"error": str(e)}), 500

@agent_api_bp.route('/agents/<int:agent_id>', methods=['PUT'])
def update_agent(agent_id):
    data = request.json
    try:
        agent = Agent.query.get_or_404(agent_id)
        agent.agent_name = data['agent_name']
        agent.description = data.get('description')
        agent.input_format = data.get('input_format')
        agent.output_format = data.get('output_format')
        db.session.commit()
        return jsonify({"message": "Agent updated", "agent": agent.to_dict()}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@agent_api_bp.route('/agents/<int:agent_id>', methods=['DELETE'])
def delete_agent(agent_id):
    try:
        agent = Agent.query.get_or_404(agent_id)
        db.session.delete(agent)
        db.session.commit()
        return jsonify({"message": "Agent deleted"}), 200
    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
