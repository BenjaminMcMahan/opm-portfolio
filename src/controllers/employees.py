from flask import Blueprint, jsonify, render_template
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
    return render_template('employees.htm', title="Employees Listing", employees=employees)
