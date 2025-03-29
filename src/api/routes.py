from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import subprocess
import re
import sys
import os

# Add the root directory to the path so we can import from the root
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from rag import RAGModel
from code_generator import CodeGenerator

router = APIRouter()
rag_model = RAGModel()
code_generator = CodeGenerator()

class ExecutionRequest(BaseModel):
    prompt: str

class ExecutionResponse(BaseModel):
    function: str
    code: str
    output: str = None

@router.post("/execute", response_model=ExecutionResponse)
async def execute_prompt(request: ExecutionRequest):
    try:
        # Extract potential arguments from the prompt (e.g., "Run command dir" -> "dir")
        match = re.search(r"run command\s+(.+)", request.prompt.lower())
        args = match.group(1) if match else None

        # Retrieve function
        function_name = rag_model.retrieve_function(request.prompt)
        
        # Generate code with arguments if applicable
        code = code_generator.generate_code(function_name, args=args if function_name == "run_command" else None)

        # Execute the generated code
        process = subprocess.Popen(['python', '-c', code], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if stderr:
            raise HTTPException(status_code=500, detail=f"Execution error: {stderr.decode().strip()}")

        output = stdout.decode().strip()
        return ExecutionResponse(function=function_name, code=code, output=output)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process request: {str(e)}")