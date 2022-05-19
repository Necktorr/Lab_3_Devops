from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.args
    name = data.get('name')
    age = data.get('age')
    return jsonify({"result": f"Hello, {name}! Age is {age}."})

if __name__== '__main__':
    app.run(debug=True) 
