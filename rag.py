from src.database.vector_db import VectorDatabase

class RAGModel:
    def __init__(self):
        self.vector_db = VectorDatabase()
    
    def retrieve_function(self, query):
        """
        Retrieves the most relevant function based on the user query
        using the vector database.
        
        Args:
            query (str): The user's natural language query
            
        Returns:
            str: The name of the most relevant function
        """
        return self.vector_db.retrieve_function(query)