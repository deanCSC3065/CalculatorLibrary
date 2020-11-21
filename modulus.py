from flask import Flask, request, make_response
app = Flask(__name__)

# Import modulus function
import calculator

# Retrieve X and Y from URL
@app.route('/modulus/', methods=['GET'])
def calculate(): 

    x = request.args.get('x')   
    y = request.args.get('y')   
    result = str(calculator.modulus(int(x),int(y)))
    return make_response(result, 200)


if __name__ == '__main__':
    app.run(debug=True)