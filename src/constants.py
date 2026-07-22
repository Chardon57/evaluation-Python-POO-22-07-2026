MANDATORY_FIELDS = ("name", "universe", "main_character", "position", "status", "has_night_lighting")

AUTHORIZED_STATUSES = ("preparing", "ready", "maintenance")

ERRORS = {
    "INVALID_BODY": ("Invalid body", 400),
    "INVALID_CHARACTER_NAME": ("Character name must be a string and can not be empty", 400),
    "INVALID_LIGHTING_VALUE": ("Night lighting property must be a boolean", 400),
    "INVALID_POSITION": ("Position must be a positive integer", 400),
    "INVALID_STATUS": ("Status must be a string and can not be other than authorized statuses", 400),
    "INVALID_UNIVERSE_NAME": ("Universe name must be a string and can not be empty", 400),
    "INVALID_VEHICLE_NAME": ("Vehicle name must be a string and can not be empty", 400),
    "POSITION_ERROR": ("A vehicle is already in this position", 400)
}