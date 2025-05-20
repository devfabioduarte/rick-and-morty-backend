from flask import jsonify

class ApiResponse:

    def success(self, data=None):
        response = {
            "success": True,
            "message" : "Success",
            "characters" : data,
            }
        return jsonify(response), 200
        
    def error(self, errors=None, message="An error occurred"):
    
        response = {
        "success": False,
        "message": message,
        "errors": errors 
        }
        return jsonify(response), 500