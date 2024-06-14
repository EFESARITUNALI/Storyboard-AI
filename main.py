from prompt_generator import process_text
from stability_api import generate_image
from config import get_api_keys

def main():
    cohere_api_key, stability_api_key = get_api_keys()
    text = input("Enter your text: ")
    prompt_list = process_text(text, cohere_api_key)
    for i in range(len(prompt_list[0])):
        generate_image(prompt_list[1][i], stability_api_key, i)

if __name__ == "__main__":
    main()