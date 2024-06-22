# app/orchestration/log_handler.py
from app.models import Log
from app.utils.database import db

class LogHandler:
    def log(self, log_entry):
        log = Log(
            flow_id=log_entry['flow_id'],
            execution_status=log_entry['execution_status'],
            input_data=log_entry['input_data'],
            output_data=log_entry['output_data'],
            error_message=log_entry.get('error_message', '')
        )
        db.session.add(log)
        db.session.commit()
