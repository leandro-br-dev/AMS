# app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO
from app.utils.database import db, init_db

migrate = Migrate()
socketio = SocketIO()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__)
    app.config.from_object(config_class)

    init_db(app)
    migrate.init_app(app, db)
    socketio.init_app(app)
    
    # Importando e registrando blueprints das APIs
    from app.controllers.agent_controller import agent_api_bp
    from app.controllers.flow_controller import flow_api_bp
    from app.controllers.step_controller import step_api_bp
    from app.controllers.service_controller import service_api_bp
    from app.controllers.log_controller import log_api_bp
    from app.controllers.orchestrator_controller import orchestrator_bp
    
    app.register_blueprint(agent_api_bp, url_prefix='/api')
    app.register_blueprint(flow_api_bp, url_prefix='/api')
    app.register_blueprint(step_api_bp, url_prefix='/api')
    app.register_blueprint(service_api_bp, url_prefix='/api')
    app.register_blueprint(log_api_bp, url_prefix='/api')
    app.register_blueprint(orchestrator_bp, url_prefix='/api')    


    # Importando e registrando blueprints das views
    from app.views.agent_views import agent_bp
    from app.views.flow_views import flow_bp    
    from app.views.service_views import service_bp
    from app.views.log_views import log_bp
    
    app.register_blueprint(agent_bp, url_prefix='/agents')
    app.register_blueprint(flow_bp, url_prefix='/flows')
    app.register_blueprint(service_bp, url_prefix='/services')
    app.register_blueprint(log_bp, url_prefix='/logs')
    
    return app
