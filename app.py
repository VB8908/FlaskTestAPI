from flask import *
app = Flask(__name__)

# Dictionary to store tasks
tasks = {}

# Endpoint to create a new task
@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    task_id = len(tasks) + 1
    tasks[task_id] = data
    return jsonify({'message': 'Task created successfully', 'task_id': task_id}), 201

# Endpoint to get all tasks
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

# Endpoint to get a specific task
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    if task_id in tasks:
        return jsonify(tasks[task_id])
    else:
        return jsonify({'message': 'Task not found'}), 404

# Endpoint to update a task
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    if task_id in tasks:
        data = request.json
        tasks[task_id].update(data)
        return jsonify({'message': 'Task updated successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404

# Endpoint to delete a task
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_id in tasks:
        del tasks[task_id]
        return jsonify({'message': 'Task deleted successfully'})
    else:
        return jsonify({'message': 'Task not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
