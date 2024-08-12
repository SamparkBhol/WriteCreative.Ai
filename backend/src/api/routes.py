from flask import Flask, jsonify
from api.story_routes import story_bp
from api.poetry_routes import poetry_bp
from api.character_routes import character_bp
from api.script_routes import script_bp
import logging

# Initialize Flask app
app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Register Blueprints for different routes
app.register_blueprint(story_bp, url_prefix='/api/story')
app.register_blueprint(poetry_bp, url_prefix='/api/poetry')
app.register_blueprint(character_bp, url_prefix='/api/character')
app.register_blueprint(script_bp, url_prefix='/api/script')

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'OK'}), 200

@app.errorhandler(404)
def not_found_error(error):
    logging.error(f"404 Error: {error}")
    return jsonify({'error': 'Not Found'}), 404

@app.errorhandler(500)
def internal_error(error):
    logging.error(f"500 Error: {error}")
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
