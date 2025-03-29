import requests
import json

# Define the API endpoint
url = 'http://127.0.0.1:8000/api/execute'

# Define the request payload
payload = {
    'prompt': 'Get CPU usage'
}

# Make the POST request
response = requests.post(url, json=payload)

# Print the status code and response
print(f'Status Code: {response.status_code}')
print('Response:')
print(json.dumps(response.json(), indent=2) if response.status_code == 200 else response.text)