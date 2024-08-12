from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

# Load pre-trained model and tokenizer
model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def format_prompt_for_poetry(prompt):
    # Format prompt for poetry generation
    return f"Write a poem about {prompt}"

def generate_poetry(prompt):
    formatted_prompt = format_prompt_for_poetry(prompt)
    inputs = tokenizer(formatted_prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=200, num_return_sequences=1, temperature=0.7)
    poetry = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return poetry

def generate_poetry_with_error_handling(prompt):
    try:
        poetry = generate_poetry(prompt)
        return poetry
    except Exception as e:
        logging.error(f"Error in poetry generation: {e}")
        return "Error generating poetry. Please try again."
