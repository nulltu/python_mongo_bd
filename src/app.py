from flask import Flask, request
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://nulltu:react2020@cluster0.reeqa.mongodb.net/pythondb?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/users', methods=['post'])
def create_user():


    username = request.json['username']
    firstName = request.json['firstName']
    password = request.json['password']
    if username and firstName and password:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert(
            {'username': username, 'firstName': firstName, 'password': hashed_password})

        response = {
            'id': str(id),
            'username': username,
            'firstName': firstName,
            'password': hashed_password
        }
        return response
    else:
         {'message': 'received'}   

if __name__ == "__main__":
    app.run(debug=True)
