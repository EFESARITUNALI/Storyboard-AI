import json
from cohere_integration import generate_prompts

def process_text(text, cohere_api_key):
    prompt_list = json.loads(generate_prompts(text, cohere_api_key))
    return prompt_list