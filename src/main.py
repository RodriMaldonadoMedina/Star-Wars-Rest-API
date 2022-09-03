"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_migrate import Migrate
from flask_swagger import swagger
from flask_cors import CORS
from utils import APIException, generate_sitemap
from admin import setup_admin
from models import db, User
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DB_CONNECTION_STRING')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
MIGRATE = Migrate(app, db)
db.init_app(app)
CORS(app)
setup_admin(app)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

####          METODOS GET            ####

@app.route('/users', methods=['GET'])
def get_users():
    #user_list = User.query.all()
    queryset = User.query.all()
    #user_list = list(map(lambda user: user.serialize(),user_list))
    user_list =[user.serialize() for user in queryset]
    return jsonify(user_list), 200

@app.route('/users/favorites', methods=['GET'])
def get_users_favorite():
    return jsonify('Lista de favoritos')

@app.route('/people', methods=['GET'])
def get_people():
    return jsonify('people')

@app.route('/people/<int:people_id>', methods=['GET'])
def get_people_id(people_id):
    return jsonify(people_id)

@app.route('/planet', methods=['GET'])
def get_planet():
    return jsonify('planet')

@app.route('/planet/<int:planet_id>', methods=['GET'])
def get_planet_id(planet_id):
    return jsonify(planet_id)

####          METODOS POST            ####

@app.route('/users', methods=['POST'])
def post_users():
    return jsonify('Se crea el user')

@app.route('/people', methods=['POST'])
def post_people():
    return jsonify('people creado')

@app.route('/planet', methods=['POST'])
def post_planet():
    return jsonify('planet creado')

@app.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def post_favorite_planet(planet_id):
    return jsonify(planet_id)

@app.route('/favorite/people/<int:people_id>', methods=['POST'])
def post_favorite_people(people_id):
    return jsonify(people_id)

####          METODOS PUT            ####

@app.route('/users/<int:user_id>', methods=['PUT'])
def put_users(user_id):
    return jsonify('modificar el user con id: ' + str(user_id))

@app.route('/people/<int:people_id>', methods=['PUT'])
def put_people(people_id):
    return jsonify('modificar people con id: ' + str(people_id))

@app.route('/planet/<int:planet_id>', methods=['PUT'])
def put_planet(planet_id):
    return jsonify('modificar planeta con id: '+ str(planet_id))

####          METODOS DELETE            ####

@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_users(user_id):
    return jsonify('eliminar el user con id: ' + str(user_id))

@app.route('/people/<int:people_id>', methods=['DELETE'])
def delete_people(people_id):
    return jsonify('eliminar people con id: ' + str(people_id))

@app.route('/planet/<int:planet_id>', methods=['DELETE'])
def delete_planet(planet_id):
    return jsonify('eliminar planeta con id: '+ str(planet_id))

@app.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    return jsonify(planet_id)

@app.route('/favorite/people/<int:people_id>', methods=['DELETE'])
def delete_favorite_people(people_id):
    return jsonify(people_id)


# this only runs if `$ python src/main.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=False)
