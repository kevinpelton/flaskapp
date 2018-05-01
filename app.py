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
    return 'Hello from a simple Flask app running on OpenShift!</br> <a href="/tasks">go here to see the API</a>'

@app.route('/tasks')
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/health')
def check_health():
    return jsonify({'status':'ok'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
