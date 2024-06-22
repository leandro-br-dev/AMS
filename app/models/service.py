from app.utils.database import db

class Service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    service_name = db.Column(db.String(255), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    endpoint_url = db.Column(db.String(255), nullable=False)
    authentication = db.Column(db.JSON, nullable=True)
    input_schema = db.Column(db.JSON, nullable=False)
    output_schema = db.Column(db.JSON, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

    def to_dict(self):
        return {
            'service_id': self.service_id,
            'service_name': self.service_name,
            'service_type': self.service_type,
            'endpoint_url': self.endpoint_url,
            'authentication': self.authentication,
            'input_schema': self.input_schema,
            'output_schema': self.output_schema,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }    
