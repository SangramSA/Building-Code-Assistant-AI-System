import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from config.neo4j_config import Neo4jConfig

# def main():
#     config = Neo4jConfig()
    
#     print("Testing Neo4j connection...")
#     if config.verify_connectivity():
#         print("✅ Connection successful!")
#     else:
#         print("❌ Connection failed!")
#         sys.exit(1)

# if __name__ == "__main__":
#     main() 

# test_connection.py - Run at start of each work session
from config.neo4j_config import Neo4jConnection

conn = Neo4jConnection()
print(f"Connection status: {conn.test_connection()}")
conn.close()