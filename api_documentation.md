# LLM + RAG-Based Function Execution API - Documentation and Examples

This document provides examples and screenshots demonstrating the API usage.

## API Endpoint

```
POST /api/execute
```

## Request Format

```json
{
  "prompt": "Your prompt here"
}
```

## Response Format

```json
{
  "function": "Called function name",
  "code": "Generated code",
  "output": "Function output"
}
```

## Available Functions

1. `open_chrome` - Opens Google Chrome
2. `open_calculator` - Opens Windows Calculator
3. `open_notepad` - Opens Notepad
4. `get_cpu_usage` - Returns current CPU usage percentage
5. `get_ram_usage` - Returns current RAM usage percentage
6. `run_command` - Executes PowerShell commands
7. `create_file` - Creates an empty file with given name
8. `get_disk_space` - Returns available disk space on C: drive in GB

## API Testing Examples

### Example 1: Getting CPU Usage

#### Using FastAPI Swagger UI
[Screenshots will be added here]

#### Using Postman
[Screenshots will be added here]

**Request:**
```json
{
  "prompt": "Get CPU usage"
}
```

**Response:**
```json
{
  "function": "get_cpu_usage",
  "code": "from src.functions.automation import get_cpu_usage\n\nresult = get_cpu_usage()\nprint(result)",
  "output": "0.0"
}
```

### Example 2: Opening Calculator

#### Using FastAPI Swagger UI
[Screenshots will be added here]

#### Using Postman
[Screenshots will be added here]

**Request:**
```json
{
  "prompt": "Open calculator"
}
```

**Response:**
```json
{
  "function": "open_calculator",
  "code": "from src.functions.automation import open_calculator\n\nresult = open_calculator()\nprint(result)",
  "output": "None"
}
```

### Example 3: Running PowerShell Command

#### Using FastAPI Swagger UI
[Screenshots will be added here]

#### Using Postman
[Screenshots will be added here]

**Request:**
```json
{
  "prompt": "Run command dir"
}
```

**Response:**
```json
{
  "function": "run_command",
  "code": "from src.functions.automation import run_command\n\nresult = run_command('dir')\nprint(result)",
  "output": "Directory: C:\\Users\\username\\Documents\n\nMode                 LastWriteTime         Length Name\n----                 -------------         ------ ----\n..."
}
```

## Testing the API with Code

Use the following Python code to test the API:

```python
import requests
import json

# Define the API endpoint
url = 'http://127.0.0.1:8000/api/execute'

# Define the request payload
payload = {
    'prompt': 'Get CPU usage'  # Change this prompt as needed
}

# Send POST request
response = requests.post(url, json=payload)

# Print status code and response
print(f'Status Code: {response.status_code}')
print('Response:')
print(json.dumps(response.json(), indent=2) if response.status_code == 200 else response.text)
```

## Testing with cURL

```bash
curl -X POST "http://127.0.0.1:8000/api/execute" \
     -H "Content-Type: application/json" \
     -d "{\"prompt\":\"Get CPU usage\"}"
```

## Testing with Postman

1. Open Postman
2. Create a new request
3. Set HTTP method to POST
4. Enter URL field: `http://127.0.0.1:8000/api/execute`
5. Click on Body tab and select "raw" option
6. Choose JSON from the dropdown
7. Enter the following JSON payload:
   ```json
   {
     "prompt": "Get CPU usage"
   }
   ```
8. Click "Send" button
9. Response will appear in the panel below