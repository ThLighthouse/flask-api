from flask import Blueprint, request, jsonify
from .models import Result
from . import db

bp = Blueprint('main', __name__)

@bp.route('/submit', methods=['POST'])
def submit():
    data = request.get_json()
    new_result = Result(name=data['name'], score=data['score'])
    db.session.add(new_result)
    db.session.commit()
    return jsonify({'message': 'Data saved'}), 201

@bp.route('/results', methods=['GET'])
def results():
    all_results = Result.query.all()
    return jsonify([
        {
            'id': r.id,
            'name': r.name,
            'score': r.score,
            'timestamp': r.timestamp.isoformat()
        } for r in all_results
    ])

@bp.route('/ping', methods=['GET'])
def ping():
    return jsonify({'status': 'ok'})

