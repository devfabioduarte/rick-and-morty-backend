from flask import jsonify

class ApiResponse:

    def api_reponse(self, data=None, success=None, message=None, status_code=None):
        response = {
            "success": success,
            "message" : message,
            "characters" : data,
            }
        
        return jsonify(response), status_code 
        
    