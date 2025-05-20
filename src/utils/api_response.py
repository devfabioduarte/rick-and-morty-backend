from flask import jsonify

class ApiResponse:

    def success(self, data=None):
        response = {
            "success": True,
            "message" : "Success",
            "characters" : data,
            }
        return jsonify(response), 200
        
    def error(self, errors=None):
    
        response = {
        "success": False,
        "message": "Error",
        "errors": errors 
        }
        return jsonify(response), 500