from app.utils.database import db

class Log(db.Model):
    log_id = db.Column(db.Integer, primary_key=True)
    flow_id = db.Column(db.Integer, db.ForeignKey('flow.flow_id'), nullable=False)
    execution_status = db.Column(db.String(50), nullable=False)
    input_data = db.Column(db.JSON, nullable=False)
    output_data = db.Column(db.JSON, nullable=False)
    error_message = db.Column(db.Text, nullable=True)
    executed_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    flow = db.relationship('Flow', backref='logs')

    def to_dict(self):
        return {
            'log_id': self.log_id,
            'flow_id': self.flow_id,
            'execution_status': self.execution_status,
            'input_data': self.input_data,
            'output_data': self.output_data,
            'error_message': self.error_message,
            'executed_at': self.executed_at
        }
