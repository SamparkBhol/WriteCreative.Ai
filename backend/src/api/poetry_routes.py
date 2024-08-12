from flask import Blueprint, request, jsonify
from nlp_model.poetry_generator import generate_poetry_with_error_handling
import logging

poetry_bp = Blueprint('poetry_bp', __name__)

@poetry_bp.route('/generate', methods=['POST'])
def generate_poetry_route():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            logging.warning("No prompt provided")
            return jsonify({'error': 'Prompt is required'}), 400
        poetry = generate_poetry_with_error_handling(prompt)
        return jsonify({'poetry': poetry})
    except Exception as e:
        logging.error(f"Error in poetry route: {e}")
        return jsonify({'error': 'An error occurred while generating the poetry.'}), 500
