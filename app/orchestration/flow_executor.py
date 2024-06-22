from app.models import Flow, Step, Log
from app.orchestration.service_caller import ServiceCaller
from app.orchestration.log_handler import LogHandler
from app.utils.database import db
import json
import re

class FlowExecutor:
    def __init__(self, flow_id, initial_input):
        self.flow_id = flow_id
        self.input_data = initial_input
        self.current_step = 0
        self.flow_steps = self.get_flow_steps(flow_id)
        self.log_handler = LogHandler()

    def get_flow_steps(self, flow_id):
        return Step.query.filter_by(flow_id=flow_id).order_by(Step.step_number).all()

    def execute_step(self, step):
        agent = step.agent
        service = agent.service

        formatted_input = self.format_input(agent.input_format, self.input_data)
        service_result = ServiceCaller.call_service(service, formatted_input)

        formatted_output = self.format_output(agent.output_format, service_result)

        log_entry = {
            'flow_id': self.flow_id,
            'execution_status': 'success' if service_result else 'failure',
            'input_data': self.input_data,
            'output_data': formatted_output,
            'error_message': '' if service_result else 'Service call failed'
        }
        self.log_handler.log(log_entry)

        return formatted_output

    def format_input(self, input_format, data):
        return self.replace_placeholders_with_defaults(input_format, {"input": data})

    def format_output(self, output_format, data):
        return self.replace_placeholders_with_defaults(output_format, {"output": data})

    def replace_placeholders_with_defaults(self, model, data):
        def get_value_from_path(data, path):
            keys = re.split(r'\.|\[|\]\.?', path.strip('.'))
            for key in keys:
                if key.isdigit():
                    key = int(key)
                if key in data:
                    data = data[key]
                elif isinstance(key, int) and len(data) > key:
                    data = data[key]
                else:
                    return None
            return data

        def recursive_replace(model, data):
            if isinstance(model, dict):
                for key, value in model.items():
                    if isinstance(value, dict) or isinstance(value, list):
                        recursive_replace(value, data)
                    elif isinstance(value, str):
                        match = re.match(r'<(.+?)(?::(.+?))?>', value)
                        if match:
                            path, default = match.groups()
                            replacement_value = get_value_from_path(data, path)
                            if replacement_value is None and default is not None:
                                replacement_value = default
                            if replacement_value is not None:
                                model[key] = replacement_value
            elif isinstance(model, list):
                for i in range(len(model)):
                    recursive_replace(model[i], data)
            return model

        return recursive_replace(model, data)

    def execute_flow(self):
        try:
            for step in self.flow_steps:
                result = self.execute_step(step)
                if result is None:
                    raise Exception('Flow execution failed at step {}'.format(step.step_number))
                self.input_data = result
                self.current_step += 1
            return self.input_data
        except Exception as e:
            self.log_handler.log({
                'flow_id': self.flow_id,
                'execution_status': 'error',
                'input_data': self.input_data,
                'output_data': {},
                'error_message': str(e)
            })
            return {'error': str(e)}
