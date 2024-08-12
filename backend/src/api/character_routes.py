from flask import Blueprint, request, jsonify
from nlp_model.character_generator import generate_character_with_error_handling
import logging

character_bp = Blueprint('character_bp', __name__)

@character_bp.route('/generate', methods=['POST'])
def generate_character_route():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            logging.warning("No prompt provided")
            return jsonify({'error': 'Prompt is required'}), 400
        character = generate_character_with_error_handling(prompt)
        return jsonify({'character': character})
    except Exception as e:
        logging.error(f"Error in character route: {e}")
        return jsonify({'error': 'An error occurred while generating the character.'}), 500
