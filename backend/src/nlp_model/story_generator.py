from transformers import GPT3LMHeadModel, GPT3Tokenizer
import logging

# Load pre-trained model and tokenizer
model_name = "gpt-3.5-turbo"
tokenizer = GPT3Tokenizer.from_pretrained(model_name)
model = GPT3LMHeadModel.from_pretrained(model_name)

def format_prompt(prompt):
    # Preprocess the prompt for better results
    return f"Once upon a time, {prompt}"

def generate_story(prompt):
    formatted_prompt = format_prompt(prompt)
    inputs = tokenizer(formatted_prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=500, num_return_sequences=1, temperature=0.7)
    story = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return story

def generate_story_with_error_handling(prompt):
    try:
        story = generate_story(prompt)
        return story
    except Exception as e:
        logging.error(f"Error in story generation: {e}")
        return "Error generating story. Please try again."
