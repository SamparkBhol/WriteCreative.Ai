from flask import Blueprint, request, jsonify
from nlp_model.script_generator import generate_script_with_error_handling
import logging

script_bp = Blueprint('script_bp', __name__)

@script_bp.route('/generate', methods=['POST'])
def generate_script_route():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            logging.warning("No prompt provided")
            return jsonify({'error': 'Prompt is required'}), 400
        script = generate_script_with_error_handling(prompt)
        return jsonify({'script': script})
    except Exception as e:
        logging.error(f"Error in script route: {e}")
        return jsonify({'error': 'An error occurred while generating the script.'}), 500
