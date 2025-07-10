from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes import student_bp
    app.register_blueprint(student_bp)

    @app.route('/healthcheck')
    def healthcheck():
        return {"status": "healthy"}, 200

    return app

