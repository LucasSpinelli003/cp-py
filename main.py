from flask import Flask, request, jsonify

app = Flask(__name__)

users = []

#POST

@app.route('/api/user', methods=['POST'])
def create_user():
    data = request.get_json()
    username = data.get('username')
    if username:
        new_user = {'username': username}
        users.append(new_user)
        return jsonify({'message': 'Usuário criado com sucesso', 'user': new_user}), 201
    else:
        return jsonify({'message': 'Dados inválidos'}), 400

#GET

@app.route('/api/users', methods=['GET'])
def get_users():
    return jsonify({'users': users})

#PUT

@app.route('/api/user/<string:username>', methods=['PUT'])
def update_user(username):
    user_to_update = None
    for user in users:
        if user['username'] == username:
            user_to_update = user
            break
    if user_to_update:
        data = request.get_json()
        new_username = data.get('new_username')
        if new_username:
            user_to_update['username'] = new_username
            return jsonify({'message': f'Usuário {username} atualizado com sucesso', 'user': user_to_update}), 200
        else:
            return jsonify({'message': 'Dados inválidos'}), 400
    else:
        return jsonify({'message': f'Usuário {username} não encontrado'}), 404

# Delete

@app.route('/api/user/<string:username>', methods=['DELETE'])
def delete_user(username):
    user_to_remove = None
    for user in users:
        if user['username'] == username:
            user_to_remove = user
            break
    if user_to_remove:
        users.remove(user_to_remove)
        return jsonify({'message': f'Usuário {username} removido com sucesso'}), 200
    else:
        return jsonify({'message': f'Usuário {username} não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
