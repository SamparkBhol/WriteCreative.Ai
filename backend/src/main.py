from flask import Flask, request, jsonify
import logging
from nlp_model.story_generator import generate_story
from nlp_model.poetry_generator import generate_poetry
from nlp_model.character_generator import generate_character
from nlp_model.script_generator import generate_script

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

@app.route('/generate/story', methods=['POST'])
def generate_story_endpoint():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            raise ValueError("Prompt is required")
        story = generate_story(prompt)
        return jsonify({'story': story})
    except Exception as e:
        logging.error(f"Error generating story: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/generate/poetry', methods=['POST'])
def generate_poetry_endpoint():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            raise ValueError("Prompt is required")
        poetry = generate_poetry(prompt)
        return jsonify({'poetry': poetry})
    except Exception as e:
        logging.error(f"Error generating poetry: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/generate/character', methods=['POST'])
def generate_character_endpoint():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            raise ValueError("Prompt is required")
        character = generate_character(prompt)
        return jsonify({'character': character})
    except Exception as e:
        logging.error(f"Error generating character: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/generate/script', methods=['POST'])
def generate_script_endpoint():
    try:
        data = request.json
        prompt = data.get('prompt', '')
        if not prompt:
            raise ValueError("Prompt is required")
        script = generate_script(prompt)
        return jsonify({'script': script})
    except Exception as e:
        logging.error(f"Error generating script: {e}")
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
