from flask import jsonify

class ApiResponse:

    def api_reponse(self, data=None, success=None, message=None):
        response = {
            "success": success,
            "message" : message,
            "characters" : data,
            }
        return jsonify(response)
        
    