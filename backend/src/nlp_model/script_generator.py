from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

# Load pre-trained model and tokenizer
model_name = "gpt2-medium"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

def format_prompt_for_script(prompt):
    # Format prompt for script generation
    return f"Write a scene for a script with the following details: {prompt}"

def generate_script(prompt):
    formatted_prompt = format_prompt_for_script(prompt)
    inputs = tokenizer(formatted_prompt, return_tensors='pt')
    outputs = model.generate(inputs['input_ids'], max_length=500, num_return_sequences=1, temperature=0.7)
    script = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return script

def generate_script_with_error_handling(prompt):
    try:
        script = generate_script(prompt)
        return script
    except Exception as e:
        logging.error(f"Error in script generation: {e}")
        return "Error generating script. Please try again."
