import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

def format_prompt(prompt):
    # Simple function to format prompts if needed
    return prompt.strip()

def save_to_file(text, filename):
    # Utility function to save text to a file
    try:
        with open(filename, 'w') as file:
            file.write(text)
        logging.info(f"Text successfully saved to {filename}")
    except Exception as e:
        logging.error(f"Error saving text to file: {e}")

def load_from_file(filename):
    # Utility function to load text from a file
    try:
        with open(filename, 'r') as file:
            content = file.read()
        logging.info(f"Text successfully loaded from {filename}")
        return content
    except Exception as e:
        logging.error(f"Error loading text from file: {e}")
        return None

def check_directory(directory):
    # Check if directory exists, if not, create it
    if not os.path.exists(directory):
        os.makedirs(directory)
        logging.info(f"Directory created: {directory}")
    else:
        logging.info(f"Directory already exists: {directory}")
