from app.utils.database import db

class Agent(db.Model):
    agent_id = db.Column(db.Integer, primary_key=True)
    agent_name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'), nullable=False)
    input_format = db.Column(db.JSON, nullable=False)
    output_format = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    service = db.relationship('Service', backref='agents')


    def to_dict(self):
        return {
            'agent_id': self.agent_id,
            'agent_name': self.agent_name,
            'description': self.description,
            'service_id': self.service_id,
            'input_format': self.input_format,
            'output_format': self.output_format,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }