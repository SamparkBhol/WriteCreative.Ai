from flask import Blueprint, request, jsonify
from nlp_model.story_generator import generate_story_with_error_handling
import logging

story_bp = Blueprint('story_bp', __name__)

@story_bp.route('/generate', methods=['POST'])
def generate_story_route():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            logging.warning("No prompt provided")
            return jsonify({'error': 'Prompt is required'}), 400
        story = generate_story_with_error_handling(prompt)
        return jsonify({'story': story})
    except Exception as e:
        logging.error(f"Error in story route: {e}")
        return jsonify({'error': 'An error occurred while generating the story.'}), 500
