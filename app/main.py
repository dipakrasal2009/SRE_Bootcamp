from flask import Flask, jsonify, request
from app.db import get_db_connection
from app.models import init_db

app = Flask(__name__)

@app.route("/api/v1/healthcheck")
def healthcheck():
    return jsonify({"status": "ok"}), 200

@app.route("/api/v1/students", methods=["GET"])
def get_students():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students').fetchall()
    conn.close()
    return jsonify([dict(s) for s in students]), 200

@app.route("/api/v1/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()
    if student is None:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(dict(student)), 200

@app.route("/api/v1/students", methods=["POST"])
def add_student():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO students (name, age, email) VALUES (?, ?, ?)',
                   (data['name'], data['age'], data['email']))
    conn.commit()
    student_id = cursor.lastrowid
    conn.close()
    return jsonify({"id": student_id, **data}), 201

@app.route("/api/v1/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()
    conn = get_db_connection()
    conn.execute('UPDATE students SET name = ?, age = ?, email = ? WHERE id = ?',
                 (data['name'], data['age'], data['email'], id))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student updated"}), 200

@app.route("/api/v1/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return jsonify({"message": "Student deleted"}), 200

if __name__ == "__main__":
    init_db()
    app.run(host='0.0.0.0', port=5000)

