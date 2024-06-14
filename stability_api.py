import requests

def generate_image(prompt, api_key, index):
    response = requests.post(
        f"https://api.stability.ai/v2beta/stable-image/generate/sd3",
        headers={
            "authorization": api_key,
            "accept": "image/*"
        },
        files={"none": ''},
        data={
            "prompt": "modern comics style." + prompt,
            "output_format": "jpeg",
        },
    )

    if response.status_code == 200:
        with open(f"{index}.jpeg", 'wb') as file:
            file.write(response.content)
        with open(f"{index}.txt", 'w') as file:
            file.write(prompt)
    else:
        raise Exception(response.json())
