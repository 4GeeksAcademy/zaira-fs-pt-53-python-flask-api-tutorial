from flask import Flask, jsonify, request
app = Flask(__name__)

# Suppose you have your data in the variable named some_data
todos = [
    { "label": "My first z task", "done": False },
    { "label": "My second z task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # converting that variable into a json string like this:
    json_text = jsonify(todos)
    # And then we return it to the front end in the response body like this:
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    todos.append(request_body)
    resp = jsonify (todos)
    resp.status_code = 200
    return resp

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position >= 0 and position < len(todos):
        todos.pop(position)
        return jsonify(todos)
    else:
        resp = jsonify ({"msg": "position does not exist"})
        resp.status_code = 400
        return resp

# These two lines should always be at the end of your app.py file
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)