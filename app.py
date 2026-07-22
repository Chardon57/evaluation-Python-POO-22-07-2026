from flask import Flask, jsonify
from src.database import db
from sqlalchemy import select
from src.models import Vehicle
from src.utils import get_json_body, validate_course_body, get_error
from src.constants import ERRORS
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///disney_dream_parade.db"

db.init_app(app)

with app.app_context():
    db.create_all()

# Récupérer tous les véhicules
@app.get("/parade-vehicles")
def list_vehicles():
    vehicle_list = db.session.scalars(select(Vehicle).order_by(Vehicle.position)).all()

    return jsonify([vehicle.to_dict() for vehicle in vehicle_list]), 200

# Récupérer un véhicule en particulier
@app.get("/parade-vehicles/<int:id>")
def get_vehicle(id: int):
    vehicle = db.session.get(Vehicle, id)

    if not vehicle:
        return jsonify({"error": "Parade vehicle not found"}), 404

    return jsonify(vehicle.to_dict()), 200

# Ajout d'un véhicule à la parade
@app.post("/parade-vehicles")
def add_vehicle():
    body = get_json_body()

    validation_error = validate_course_body(body)

    if validation_error:
        return get_error(validation_error)

    # Il faut vérifier que le véhicule à ajouter n'a pas la même position dans la parade qu'un véhicule déjà existant
    vehicles_positions = db.session.scalars(select(Vehicle.position)).all()
    if body["position"] in vehicles_positions:
        return get_error("POSITION_ERROR")

    vehicle = Vehicle()
    vehicle.from_body(body)

    db.session.add(vehicle)
    db.session.commit()

    return jsonify(vehicle.to_dict()), 201

# Modifier un véhicule
@app.put("/parade-vehicles/<int:id>")
def update_vehicle(id: int):
    vehicle = db.session.get(Vehicle, id)
    
    if not vehicle:
        return jsonify({"error": "Parade vehicle not found"}), 404

    body = get_json_body()
    
    validation_error = validate_course_body(body)
    
    if validation_error:
            return get_error(validation_error)
    
    # Là aussi, il faut vérifier que le véhicule à modifier ne va pas occuper la même position dans la parade qu'un véhicule déjà existant
    vehicles_positions = db.session.scalars(select(Vehicle.position)).all()
    if body["position"] in vehicles_positions:
        return get_error("POSITION_ERROR")

    vehicle.from_body(body)

    db.session.commit()

    return jsonify(vehicle.to_dict()), 200

# Supprimer un véhicule
@app.delete("/parade-vehicles/<int:id>")
def delete_vehicle(id: int):
    vehicle = db.session.get(Vehicle, id)

    if not vehicle:
        return jsonify({"error": "Parade vehicle not found"}), 404

    db.session.delete(vehicle)
    db.session.commit()

    return "", 204


if __name__ == "__main__":
    app.run(debug=True)