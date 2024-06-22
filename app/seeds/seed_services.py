import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from app import create_app
from app.utils.database import db
from app.models.service import Service

app = create_app()

with app.app_context():
    db.create_all()

    services = [
        Service(
            service_name="LLMHub",
            service_type="LLM",
            endpoint_url="http://127.0.0.1:5001/api/chat",
            authentication={},
            input_schema={
                "model": "string",
                "messages": [
                    {
                        "role": "string",
                        "content": "string"
                    }
                ],
                "options": {
                    "stream": "boolean"
                }
            },
            output_schema={
                "model": "string",
                "created_at": "datetime",
                "message": {
                    "role": "string",
                    "content": "string"
                },
                "done": "boolean"
            }
        )
    ]

    db.session.bulk_save_objects(services)
    db.session.commit()