from app.utils.database import db

class Step(db.Model):
    step_id = db.Column(db.Integer, primary_key=True)
    flow_id = db.Column(db.Integer, db.ForeignKey('flow.flow_id'), nullable=False)
    agent_id = db.Column(db.Integer, db.ForeignKey('agent.agent_id'), nullable=False)
    step_number = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    agent = db.relationship('Agent', backref='steps')


    def to_dict(self):
        return {
            'step_id': self.step_id,
            'flow_id': self.flow_id,
            'agent_id': self.agent_id,
            'step_number': self.step_number,
            'instructions': self.instructions,           
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }