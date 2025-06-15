# import os
# from dotenv import load_dotenv
# from neo4j import GraphDatabase

# # Load environment variables
# load_dotenv()

# class Neo4jConfig:
#     def __init__(self):
#         self.uri = os.getenv("NEO4J_URI")
#         self.username = os.getenv("NEO4J_USERNAME")
#         self.password = os.getenv("NEO4J_PASSWORD")
#         self.database = os.getenv("NEO4J_DATABASE", "neo4j")

#     def get_driver(self):
#         """Create and return a Neo4j driver instance."""
#         return GraphDatabase.driver(
#             self.uri,
#             auth=(self.username, self.password)
#         )

#     def verify_connectivity(self):
#         """Verify the connection to the Neo4j database."""
#         try:
#             driver = self.get_driver()
#             driver.verify_connectivity()
#             driver.close()
#             return True
#         except Exception as e:
#             print(f"Connection failed: {str(e)}")
#             return False 

import os
from neo4j import GraphDatabase
from dotenv import load_dotenv

load_dotenv()

class Neo4jConnection:
    def __init__(self):
        self.driver = GraphDatabase.driver(
            os.getenv("NEO4J_URI"),
            auth=(os.getenv("NEO4J_USERNAME"), 
                  os.getenv("NEO4J_PASSWORD"))
        )
    
    def close(self):
        self.driver.close()
    
    def test_connection(self):
        with self.driver.session() as session:
            result = session.run("RETURN 'Connected!' as message")
            return result.single()["message"]