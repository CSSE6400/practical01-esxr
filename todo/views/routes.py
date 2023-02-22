from flask import Blueprint, jsonify, request

api = Blueprint('api', __name__, url_prefix='/api/v1')

@api.route('/health')
def health():
    return jsonify({
        "status": "ok"
    })

# Define the server state
todos = []

# Define CRUD endpoints for the api

# GET
@api.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

# GET
@api.route('/todos/<int:id>', methods=['GET'])
def get_todo(id):
    if id >= len(todos):
        return jsonify({
            "error": "Todo not found"
        })
    
    return jsonify(todos[id])

# POST
@api.route('/todos', methods=['POST'])
def create_todo():
    # get the data from the request
    data = request.get_json()
    # add the todo to the list
    todos.append(data)
    # return the new todo
    return jsonify(data)
    

# PUT
@api.route('/todos/<int:id>', methods=['PUT'])
def update_todo(id):
    # get the data from the request
    data = request.get_json()
    # update the todo
    todos[id] = data
    # return the new todo
    return jsonify(data)

# DELETE
@api.route('/todos/<int:id>', methods=['DELETE'])
def delete_todo(id):
    # delete the todo
    todos.pop(id)
    # return the new todo
    return jsonify({
        "status": "ok"
    })