from flask import Flask, jsonify, request, make_response, redirect
app = Flask(__name__)

# Import modulus function
import modulus

class ErrorHander(Exception):
    def __init__(self,message,status=400, response=None):
        self.message = message
        self.status = status
        self.response = response

# Retrieve X and Y from URL
@app.route('/', methods=['GET'])
def calculate(): 

    x = request.args.get('x')   
    y = request.args.get('y')   

#Error Handling: Check if x,y values have been entered
    if not x and not y:
        raise ErrorHander('Both X param value and Y param value has not been entered.', 400)

    if not x:
        raise ErrorHander('X param value has not been entered.', 400)
    
    if not y:
        raise ErrorHander('Y param value has not been entered.', 400)


#Error Handling: Final Check - if string values x,y can be converted to an int 
    if (str.isdigit(x) and str.isdigit(y)):
        result = str(modulus.modulus(int(x),int(y)))

        response = make_response(
            jsonify(
                {"error":"false", "status": 200, "answer":result}
            ),
            200,
        )
        response.headers["Content-Type"] = "application/json"
        return response
    else:
        raise ErrorHander('Both X and Y param must be of integer type.', 400)

# Function to handle status codes != 200 OK
@app.errorhandler(ErrorHander)
def handle_bad_request(error):
    response = dict(error.response or ())
    response['status'] = error.status
    response['error'] = error.message
    return jsonify(response), error.status


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
