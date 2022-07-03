from flask import Blueprint, jsonify, abort, request
from ..models import Employee, db

bp = Blueprint('employees', __name__, url_prefix='/employees')


@bp.route('', methods=['GET'])
def index():
    """
    Index
    Returns all Employees in the employees table
    :return: List of Employees in JSON
    """
    employees = Employee.query.all()
    result = []
    for employee in employees:
        result.append(employee.serialize())

    return jsonify(result)
