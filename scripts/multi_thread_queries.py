import mysql.connector
from mysql.connector import Error
import threading
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Database configuration from environment variables
config = {
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

def execute_query(query, params=None):
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
            
        if query.strip().lower().startswith('select'):
            result = cursor.fetchall()
            print(f"Query executed successfully. Result: {result}")
        else:
            conn.commit()
            print(f"Query executed successfully. Rows affected: {cursor.rowcount}")
            
    except Error as e:
        print(f"Error executing query: {e}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

def insert_data():
    query = """
    INSERT INTO ClimateData (location, record_date, temperature, precipitation, humidity)
    VALUES (%s, %s, %s, %s, %s)
    """
    data = ('San Francisco', '2023-01-16', 15.5, 3.2, 60.0)
    execute_query(query, data)

def select_data():
    query = "SELECT * FROM ClimateData WHERE temperature > 20"
    execute_query(query)

def update_data():
    query = "UPDATE ClimateData SET humidity = humidity + 5 WHERE location = 'London'"
    execute_query(query)

if __name__ == "__main__":
    # Create threads for each query type
    threads = [
        threading.Thread(target=insert_data),
        threading.Thread(target=select_data),
        threading.Thread(target=update_data)
    ]
    
    # Start all threads
    for thread in threads:
        thread.start()
    
    # Wait for all threads to complete
    for thread in threads:
        thread.join()
    
    print("All concurrent queries completed")