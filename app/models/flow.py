from app.utils.database import db

class Flow(db.Model):
    flow_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    steps = db.relationship('Step', backref='flow', lazy=True)


    def to_dict(self):
        return {
            'flow_id': self.flow_id,
            'name': self.name,           
            'description': self.description,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }
