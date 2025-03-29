import chromadb
from sentence_transformers import SentenceTransformer

class VectorDatabase:
    def __init__(self):
        self.client = chromadb.Client()
        self.collection = self.client.create_collection("automation_functions")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.function_descriptions = {
            "open_chrome": "Opens the Google Chrome web browser.",
            "open_calculator": "Opens the Windows Calculator application.",
            "open_notepad": "Opens the Notepad text editor.",
            "get_cpu_usage": "Retrieves the current CPU usage as a percentage.",
            "get_ram_usage": "Retrieves the current RAM usage as a percentage.",
            "run_command": "Runs a PowerShell command and returns the output.",
            "create_file": "Creates a new empty file with the specified name.",
            "get_disk_space": "Retrieves the free disk space on the C: drive in GB.",
            "list_running_processes": "Lists the top 5 running processes by memory usage.",
            "check_internet_connection": "Checks if there is an active internet connection."
        }
        self.populate_db()

    def populate_db(self):
        """Populates the ChromaDB with function descriptions and names."""
        ids = list(self.function_descriptions.keys())
        embeddings = self.model.encode(list(self.function_descriptions.values())).tolist()
        metadatas = [{"function_name": id} for id in ids]
        self.collection.add(embeddings=embeddings, metadatas=metadatas, ids=ids)

    def retrieve_function(self, query):
        """Retrieves the most relevant function based on the query."""
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(query_embeddings=[query_embedding], n_results=1)
        function_name = results['metadatas'][0][0]['function_name']
        return function_name