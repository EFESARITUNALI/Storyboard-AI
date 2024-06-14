import configparser

def get_api_keys():
    config = configparser.ConfigParser()
    config.read('config.ini')
    cohere_api_key = config['API_KEYS']['cohere_api_key']
    stability_api_key = config['API_KEYS']['stability_api_key']
    return cohere_api_key, stability_api_key

def get_prompt_template(file_path='prompt_template.txt'):
    with open(file_path, 'r') as file:
        template = file.read()
    return template