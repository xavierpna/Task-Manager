from app.controllers.task_controller import TaskManager

from flask import Blueprint, jsonify, request

task_bp = Blueprint('task_bp', __name__)
task_manager = TaskManager()

@task_bp.route('/task', methods=['GET'])
def get_task():
    return jsonify(task_manager.show_tasks())

@task_bp.route('/task', methods=['POST'])
def create_task():
    data = request.get_json('tasks.json')
    task_manager.add_task(data['owner'], data['name'], data['status'], data['desc'], data['priority'], data['due_date'])
    task_manager.save()
    return "Task created successfully.", 201

@task_bp.route('/task/<int:index>', methods=['DELETE'])
def delete_task(index):
    result = task_manager.delete_task(index)
    task_manager.save()
    return result, 200

@task_bp.route('/task/notifications', methods=['GET'])
def get_notifications():
    return jsonify(task_manager.due_date_notification())