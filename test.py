# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, world!'

# if __name__ == '__main__':
#     app.run(debug=True)


import requests
response = requests.post(
    "http://127.0.0.1:5000/login",
    json={"email": "test@example.com", "password": "testpass"}
)
print(response.json())
