from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# PostgreSQL Database Config
# तुमच्या actual username, password, host, आणि db_name इथे टाका
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost/todo_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Model
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(200), nullable=False)

    def to_dict(self):
        return {"id": self.id, "task": self.task}

# Create Tables
with app.app_context():
    db.create_all()

# Routes
@app.route('/todos', methods=['GET'])
def get_todos():
    todos = Todo.query.all()
    return jsonify([t.to_dict() for t in todos])

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    if not data or not data.get('task'):
        return jsonify({"error": "Task required"}), 400
    new_todo = Todo(task=data['task'])
    db.session.add(new_todo)
    db.session.commit()
    return jsonify(new_todo.to_dict()), 201

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    todo = Todo.query.get(todo_id)
    if not todo:
        return jsonify({"error": "Todo not found"}), 404
    db.session.delete(todo)
    db.session.commit()
    return jsonify({"message": "Todo deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
