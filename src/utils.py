from flask import request, jsonify
from src.constants import MANDATORY_FIELDS, AUTHORIZED_STATUSES, ERRORS

def get_json_body():
    '''Fonction utilitaire permettant de récupérer les données issues du formulaire du frontend.
    Après avoir vérifié la présence du contenu, retourne un dictionnaire ou *None* si le contenu est vide.'''
    body = request.get_json(silent=True)
    if not isinstance(body, dict):
        return None
    return body

def validate_course_body(body: dict | None):
    '''Fonction utilitaire permettant de vérifier la validité du body passé en paramètre. Renvoie une erreur 
    si une incohérence est trouvée.'''
    if not body:
        return "INVALID_BODY"
    
    for field in MANDATORY_FIELDS:
        if field not in body:
            return "MISSING_FIELD"
        
    if (not isinstance(body["name"], str) or not body["name"].strip() or len(body["name"].strip()) > 100):
            return "INVALID_VEHICLE_NAME"
    
    if (not isinstance(body["universe"], str) or not body["universe"].strip() or len(body["universe"].strip()) > 100):
            return "INVALID_UNIVERSE_NAME"

    if (not isinstance(body["main_character"], str) or not body["main_character"].strip() or len(body["main_character"].strip()) > 100):
                return "INVALID_CHARACTER_NAME"
    
    if not isinstance(body["position"], int) or body["position"] < 0:
        return "INVALID_POSITION"
    
    if not isinstance(body["status"], str) or body["status"] not in AUTHORIZED_STATUSES:
          return "INVALID_STATUS"

    if not isinstance(body["has_night_lighting"], bool):
          return "INVALID_LIGHTING_VALUE"
    
    return None

def get_error(code: str):
    '''Renvoie un JSON contenant le message d'erreur et le status code correspondant. Reçoit le
    code d'erreur en paramètre.'''
    message, http_status = ERRORS[code]
    return jsonify({
        "error": message,
        "code": code
    }), http_status