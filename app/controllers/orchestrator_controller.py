# app/controllers/orchestrator_controller.py
from flask import Blueprint, request, jsonify
from app.orchestration.flow_executor import FlowExecutor

orchestrator_bp = Blueprint('orchestrator', __name__)

@orchestrator_bp.route('/orchestrator/start-flow', methods=['POST'])
def start_flow():
    data = request.json
    flow_id = data.get('flow_id')
    initial_input = data.get('initial_input', {})
    
    executor = FlowExecutor(flow_id, initial_input)
    result = executor.execute_flow()
    
    return jsonify(result)
