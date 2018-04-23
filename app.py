from flask import Flask, jsonify
app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn OpenShift',
        'description': u'Need to find a good tutorial on the web', 
        'done': False
    }
]

@app.route('/')
def hello_world():
    return 'Flask in Docker'

@app.route('/tasks')
def get_tasks():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
