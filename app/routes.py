from flask import Blueprint, request, jsonify
from .models import Student
from . import db

student_bp = Blueprint('student_bp', __name__, url_prefix='/api/v1')

@student_bp.route('/student', methods=['GET'])
def get_all_students():
    students = Student.query.all()
    return jsonify([s.to_dict() for s in students])

@student_bp.route('/student/<int:id>', methods=['GET'])
def get_student(id):
    student = Student.query.get_or_404(id)
    return jsonify(student.to_dict())

@student_bp.route('/student', methods=['POST'])
def add_student():
    data = request.get_json()
    new_student = Student(name=data['name'], age=data['age'], grade=data['grade'])
    db.session.add(new_student)
    db.session.commit()
    return jsonify(new_student.to_dict()), 201

@student_bp.route('/student/<int:id>', methods=['PUT'])
def update_student(id):
    student = Student.query.get_or_404(id)
    data = request.get_json()
    student.name = data['name']
    student.age = data['age']
    student.grade = data['grade']
    db.session.commit()
    return jsonify(student.to_dict())

@student_bp.route('/student/<int:id>', methods=['DELETE'])
def delete_student(id):
    student = Student.query.get_or_404(id)
    db.session.delete(student)
    db.session.commit()
    return '', 204

