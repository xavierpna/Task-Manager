from flask import Flask
from app.routes.task_routes import task_bp
from app.controllers.task_controller import TaskManager

app = Flask(__name__)
app.register_blueprint(task_bp)

if __name__ == "__main__":
    task_manager = TaskManager()
    task_manager.load()
    app.run(debug=True)
