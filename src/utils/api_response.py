from flask import jsonify

class ApiResponse:

    def success(data=None, message="Success"):
        response = {
            "sucess": True,
            "message" : message,
            "data" : data or {}
        }

        return jsonify(response), 200
        
    def error(message="Error", errors=None):
    
        response = {
        "success": False,
        "message": message,
        "errors": errors or []
        }
        return jsonify(response), 500