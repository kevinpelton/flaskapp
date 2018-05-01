from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'First Item',
        'description': u'This is the first item'
    },
    {
        'id': 2,
        'title': u'Second Item',
        'description': u'This is item #2'
    }
]

@app.route('/')
def hello_world():
    return 'Hello from a simple Flask app running on OpenShift'

@app.route('/tasks')
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
