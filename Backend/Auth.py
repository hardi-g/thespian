from flask import Blueprint, request, jsonify
import bcrypt, database
cur = database.connect()

login_bp = Blueprint('login', __name__)
signup_bp = Blueprint('signup', __name__)

def authenticate(username, password):
    cur.execute("SELECT password FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    if result and bcrypt.checkpw(password.encode('utf-8'), result[0].encode('utf-8')):
        return True
    return False

@login_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    if authenticate(username, password):
        return jsonify({'message': 'Logged In',
                        'username':username}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@signup_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    if not data or 'username' not in data or 'password' not in data:
        return jsonify({'message': 'Missing username or password'}), 400

    username = data['username']
    password = data['password']

    cur.execute("SELECT * FROM users WHERE username = %s", (username,))
    existing_user = cur.fetchone()

    if existing_user:
        return jsonify({'message': 'Username already exists'}), 400

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, hashed_password.decode('utf-8')))
    cur.execute("COMMIT")

    return jsonify({'message': 'User created successfully'}), 201
