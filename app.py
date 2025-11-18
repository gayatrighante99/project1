# from flask import Flask, request, jsonify
# import pymysql
# from werkzeug.security import check_password_hash
# from flask_cors import CORS   # <-- Import CORS

# app = Flask(__name__)
# CORS(app)                     # <-- Enable CORS

# def get_db_connection():
#     return pymysql.connect(
#         host='localhost',
#         user='root',                # put your MySQL username here
#         password='Gayatri@25',      # put your password here
#         database='shose_website_1'
#     )

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')
    
#     conn = get_db_connection()
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute("SELECT username, password FROM users WHERE email=%s", (email,))
#             result = cursor.fetchone()
#             if result:
#                 username, password_hash = result
#                 if check_password_hash(password_hash, password):
#                     return jsonify({"message": "Login successful!", "username": username})
#                 else:
#                     return jsonify({"error": "Incorrect password."}), 401
#             else:
#                 return jsonify({"error": "Email not found."}), 404
#     finally:
#         conn.close()

# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, request, jsonify
# import pymysql
# from werkzeug.security import generate_password_hash, check_password_hash
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)  # Enable Cross-Origin requests

# def get_db_connection():
#     return pymysql.connect(
#         host='localhost',
#         user='root',            # Your MySQL username
#         password='Gayatri@25',  # Your MySQL password
#         database='shose_website_1'  # Your database name
#     )

# @app.route('/signup', methods=['POST'])
# def signup():
#     data = request.get_json()
#     username = data.get('username')
#     email = data.get('email')
#     password = data.get('password')

#     if not username or not email or not password:
#         return jsonify({"error": "Please provide username, email, and password."}), 400

#     password_hash = generate_password_hash(password)

#     conn = get_db_connection()
#     try:
#         with conn.cursor() as cursor:
#             # Check if email already exists
#             cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
#             if cursor.fetchone():
#                 return jsonify({"error": "Email already registered."}), 409

#             # Insert new user
#             cursor.execute(
#                 "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
#                 (username, email, password_hash)
#             )
#             conn.commit()
#         return jsonify({"message": "Signup successful! You can now log in."}), 201
#     finally:
#         conn.close()

# @app.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     email = data.get('email')
#     password = data.get('password')

#     conn = get_db_connection()
#     try:
#         with conn.cursor() as cursor:
#             cursor.execute("SELECT username, password FROM users WHERE email=%s", (email,))
#             result = cursor.fetchone()
#             if not result:
#                 return jsonify({"error": "Email not found."}), 404
#             username, password_hash = result
#             if check_password_hash(password_hash, password):
#                 return jsonify({"message": "Login successful!", "username": username}), 200
#             else:
#                 return jsonify({"error": "Incorrect password."}), 401
#     finally:
#         conn.close()

# if __name__ == '__main__':
#     app.run(debug=True)
















from flask import Flask, request, jsonify
import pymysql
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})  # Allow frontend JS calls

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',               # Replace with your MySQL username
        password='Gayatri@25',     # Replace with your MySQL password
        database='shose_website_1' # Your database name
    )

@app.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({"error": "Please provide username, email, and password."}), 400

    password_hash = generate_password_hash(password)

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT id FROM users WHERE email=%s", (email,))
            if cursor.fetchone():
                return jsonify({"error": "Email already registered."}), 409

            # Insert user and commit!
            cursor.execute(
                "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                (username, email, password_hash)
            )
            conn.commit()
            print("User committed to database:", username, email)
        return jsonify({"message": "Signup successful! You can now log in."}), 201
    except Exception as e:
        print("Error during signup:", e)
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    conn = get_db_connection()
    try:
        with conn.cursor() as cursor:
            cursor.execute("SELECT username, password FROM users WHERE email=%s", (email,))
            result = cursor.fetchone()
            if not result:
                return jsonify({"error": "Email not found."}), 404
            username, password_hash = result
            if check_password_hash(password_hash, password):
                return jsonify({"message": "Login successful!", "username": username}), 200
            else:
                return jsonify({"error": "Incorrect password."}), 401
    except Exception as e:
        print("Error during login:", e)
        return jsonify({"error": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    app.run(debug=True)

