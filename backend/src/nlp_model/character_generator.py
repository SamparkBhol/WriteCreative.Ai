from transformers import GPT3LMHeadModel, GPT3Tokenizer
import logging

# Load pre-trained model and tokenizer
model_name = "gpt-3.5-turbo"
tokenizer = GPT3Tokenizer.from_pretrained(model_name)
model = GPT3LMHeadModel.from_pretrained(model_name)

def format_prompt_for_character(prompt):
    # Format prompt for character description
    return f"Describe a character with the following traits: {prompt}"

def generate_character(prompt):
    formatted_prompt = format_prompt_for_character(prompt)
    inputs = tokenizer(formatted_prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=300, num_return_sequences=1, temperature=0.7)
    character_description = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return character_description

def generate_character_with_error_handling(prompt):
    try:
        character = generate_character(prompt)
        return character
    except Exception as e:
        logging.error(f"Error in character generation: {e}")
        return "Error generating character. Please try again."
