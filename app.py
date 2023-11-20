from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data (for demonstration)
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]

# Read all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# Read a specific user by ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    new_user = request.json
    new_user['id'] = max(user['id'] for user in users) + 1
    users.append(new_user)
    return jsonify(new_user), 201

# Update a user by ID
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        user.update(request.json)
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}), 404

# Delete a user by ID
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        users.remove(user)
        return jsonify({"message": "User deleted"}), 200
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
