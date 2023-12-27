import requests
import json

def genetrate(prompt, api):
    
    # api_key = "AIzaSyCmTh3lXw-dqVf-RhUmkjONdQuy0OmF5Fg"
    api_key = api
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + api_key
    # Request headers
    headers = {
        'Content-Type': 'application/json'
    }

    # Request payload
    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": f"{prompt}"
                    }
                ]
            }
        ]
    }

    # Convert payload to JSON format
    payload_json = json.dumps(payload)

    # Make POST request
    response = requests.post(url, headers=headers, data=payload_json)

    # Check response status
    if response.status_code == 200:
        # Print the response content
        print("- Fetching Data ...")
    else:
        print("Request failed with status code:", response.status_code)
        print("Response:", response.text)


    # Convert the JSON string to a Python dictionary
    data = json.loads(response.text)

    # Extracting text from the JSON data
    text = data["candidates"][0]["content"]["parts"][0]["text"]
    print(f"- Result {len(text)} long")
    return text


# if __name__=='__main__':
#     api_key = "AIzaSyCmTh3lXw-dqVf-RhUmkjONdQuy0OmF5Fg"
#     inp = "tell me a story"
#     out = genetrate(api=api_key, prompt=inp)
#     with open('output.txt', 'w') as file:
#         file.write(out)
    