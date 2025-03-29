import inspect
import textwrap
from src.functions.automation import *

class CodeGenerator:
    def __init__(self):
        # Get all functions from the automation module
        self.functions = {name: func for name, func in globals().items() 
                         if callable(func) and not name.startswith('_') and func.__module__ == 'src.functions.automation'}
    
    def generate_code(self, function_name, args=None):
        """
        Generates executable Python code for the specified function.
        
        Args:
            function_name (str): The name of the function to generate code for
            args (str, optional): Arguments to pass to the function
            
        Returns:
            str: Executable Python code as a string
        """
        if function_name not in self.functions:
            raise ValueError(f"Function '{function_name}' not found")
        
        function = self.functions[function_name]
        
        # Get the function's source code and signature
        source = inspect.getsource(function)
        signature = inspect.signature(function)
        
        # Generate the import statement
        import_statement = f"from src.functions.automation import {function_name}\n\n"
        
        # Generate the function call
        if function_name == "run_command" and args:
            function_call = f"result = {function_name}('{args}')\n"
        elif len(signature.parameters) > 0 and args:
            function_call = f"result = {function_name}('{args}')\n"
        else:
            function_call = f"result = {function_name}()\n"
        
        # Generate the print statement to capture the output
        print_statement = "print(result)"
        
        # Combine everything into a complete code snippet
        code = import_statement + function_call + print_statement
        
        return code