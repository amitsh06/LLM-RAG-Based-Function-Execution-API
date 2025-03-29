# LLM + RAG-Based Function Execution API

## Overview
This project implements a FastAPI service that uses RAG (Retrieval-Augmented Generation) to map user prompts to predefined automation functions, generates executable Python code, and executes it securely.

## Features
- Natural language to code conversion
- Secure function execution environment
- FastAPI-based REST endpoints
- Vector database for efficient retrieval
- Automated code generation and validation

## Prerequisites
- Python 3.8 or higher
- FastAPI
- Virtual environment (recommended)

## Setup
1. Clone the repository
2. Create and activate a virtual environment (recommended)
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Start the server:
   ```bash
   python -m uvicorn src.api.app:app --reload
   ```
2. Access the API documentation at `http://localhost:8000/docs`
3. Use the endpoints to submit prompts and execute functions

## Project Structure
```
├── src/
│   ├── api/         # FastAPI application and routes
│   ├── database/    # Vector database implementation
│   ├── functions/   # Automation functions
│   └── utils/       # Utility functions
├── screenshots/     # API usage examples
└── requirements.txt # Project dependencies
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License.