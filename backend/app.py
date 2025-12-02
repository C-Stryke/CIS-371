from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
from dotenv import load_dotenv
import os
import uuid
import hashlib
import requests

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Allows backend to communicate with frontend since they're different origins
CORS(app,
     supports_credentials=True,
     origins=['http://localhost:5173', 'http://127.0.0.1:5173'],
     allow_headers=['Content-Type', 'Authorization'],
     methods=['GET', 'POST', 'PUT', 'DELETE', 'OPTIONS'])

# Firebase configuration
FIREBASE_PROJECT_ID = os.getenv('FIREBASE_PROJECT_ID')
FIREBASE_API_KEY = os.getenv('FIREBASE_API_KEY')
FIRESTORE_URL = f'https://firestore.googleapis.com/v1/projects/{FIREBASE_PROJECT_ID}/databases/(default)/documents'

# Hash password before storing in DB
def hash_password(password):
    """Hash password using SHA-256"""
    return hashlib.sha256(password.encode()).hexdigest()

# Generate session ID when user logs in (this is how we identify the user)
def generate_session_id():
    """Generate a unique session ID"""
    return str(uuid.uuid4())

# How we add data to the DB
def firestore_add_document(collection, data):
    """Add a document to Firestore collection"""
    url = f'{FIRESTORE_URL}/{collection}'

    # Convert data to Firestore format
    fields = {}
    for key, value in data.items():
        if isinstance(value, str):
            fields[key] = {"stringValue": value}
        elif isinstance(value, int):
            fields[key] = {"integerValue": value}
        elif isinstance(value, bool):
            fields[key] = {"booleanValue": value}

    payload = {"fields": fields}

    response = requests.post(url, json=payload)
    return response.json() if response.status_code == 200 else None

# How we retrieve data from the DB
def firestore_query_documents(collection, field, value):
    """Query documents in Firestore collection"""
    url = f'{FIRESTORE_URL}:runQuery'

    query = {
        "structuredQuery": {
            "from": [{"collectionId": collection}],
            "where": {
                "fieldFilter": {
                    "field": {"fieldPath": field},
                    "op": "EQUAL",
                    "value": {"stringValue": value}
                }
            },
            "limit": 1
        }
    }

    response = requests.post(url, json=query)

    if response.status_code == 200:
        results = response.json()
        # Check if results contains actual documents
        # Firestore returns an array where each item has a "document" field if found
        if results and isinstance(results, list):
            # Filter out results that don't have a "document" field
            actual_docs = [r for r in results if 'document' in r]
            return actual_docs
        return []
    return []

# Delete data from the DB
def firestore_delete_document(document_path):
    """Delete a document from Firestore using its full path"""
    url = f'https://firestore.googleapis.com/v1/{document_path}'
    response = requests.delete(url)
    return response.status_code == 200

@app.route('/api/signup', methods=['POST'])
def signup():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        if len(username) < 3:
            return jsonify({'error': 'Username must be at least 3 characters'}), 400

        if len(password) < 5:
            return jsonify({'error': 'Password must be at least 5 characters'}), 400

        # Check if user already exists
        existing_users = firestore_query_documents('users', 'username', username)

        if existing_users and len(existing_users) > 0:
            return jsonify({'error': 'Username already exists'}), 409

        # Hash password
        hashed_password = hash_password(password)

        # Create user in Firestore
        user_data = {
            'username': username,
            'password': hashed_password
        }

        firestore_add_document('users', user_data)

        # Return success response
        return jsonify({
            'message': 'User created successfully',
            'username': username
        }), 201

    except Exception as e:
        print(f"Signup error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()

        # Validate input
        if not username or not password:
            return jsonify({'error': 'Username and password are required'}), 400

        # Find user
        users = firestore_query_documents('users', 'username', username)

        if not users or len(users) == 0:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Get user data from Firestore response
        user_doc = users[0]['document']
        stored_password = user_doc['fields']['password']['stringValue']

        # Check password
        hashed_password = hash_password(password)
        if stored_password != hashed_password:
            return jsonify({'error': 'Invalid username or password'}), 401

        # Generate session ID
        session_id = generate_session_id()

        # Store session in Firestore
        session_data = {
            'username': username,
            'sessionID': session_id
        }
        
        firestore_add_document('sessions', session_data)

        # Create response with cookie
        response = make_response(jsonify({
            'message': 'Login successful',
            'username': username
        }), 200)

        # Set cookie (expires in 30 days)
        print(f"[LOGIN] Setting cookie with sessionID: {session_id}")
        response.set_cookie(
            'sessionID',
            session_id,
            max_age=30*24*60*60,  # 30 days in seconds
            httponly=False,  # Set to False for debugging
            samesite='Lax',
            path='/',
            domain=None  # Let browser handle domain
        )
        print(f"[LOGIN] Response headers: {dict(response.headers)}")

        return response

    except Exception as e:
        print(f"Login error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/logout', methods=['POST'])
def logout():
    try:
        session_id = request.cookies.get('sessionID')

        # Delete session from Firestore if it exists
        if session_id:
            sessions = firestore_query_documents('sessions', 'sessionID', session_id)
            if sessions and len(sessions) > 0:
                # Get the document path from the query result
                session_doc = sessions[0]['document']
                document_path = session_doc['name']
                firestore_delete_document(document_path)

        # Create response
        response = make_response(jsonify({
            'message': 'Logged out successfully'
        }), 200)

        # Clear cookie
        response.set_cookie(
            'sessionID',
            '',
            max_age=0,
            httponly=False,
            samesite='Lax',
            path='/'
        )

        return response

    except Exception as e:
        print(f"Logout error: {e}")
        return jsonify({'error': 'Internal server error'}), 500


@app.route('/api/auth/check', methods=['GET'])
def check_auth():
    try:
        session_id = request.cookies.get('sessionID')

        if not session_id:
            return jsonify({'authenticated': False}), 200

        # Check if session exists in Firestore
        sessions = firestore_query_documents('sessions', 'sessionID', session_id)

        if sessions and len(sessions) > 0:
            # Get username from session
            session_doc = sessions[0]['document']
            username = session_doc['fields']['username']['stringValue']

            return jsonify({
                'authenticated': True,
                'username': username
            }), 200
        else:
            return jsonify({'authenticated': False}), 200

    except Exception as e:
        print(f"Auth check error: {e}")
        return jsonify({'authenticated': False}), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
