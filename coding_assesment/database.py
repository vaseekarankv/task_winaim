import mysql.connector
from config import mysql_config
from fastapi import HTTPException

# Connect to MySQL database
try:
    connection = mysql.connector.connect(**mysql_config)
    print("Connected to MySQL database")
except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)
    connection = None

# Function to execute MySQL queries
def execute_query(query, data=None, fetchall=False):
    if connection:
        try:
            cursor = connection.cursor(dictionary=True)
            cursor.execute(query, data)
            if fetchall:
                result = cursor.fetchall()
            else:
                result = cursor.fetchone()
            cursor.close()
            return result
        except mysql.connector.Error as error:
            print("Error executing MySQL query:", error)
            raise HTTPException(status_code=500, detail="Error executing MySQL query")
    else:
        raise HTTPException(status_code=500, detail="Database connection error")

# Function to close database connection
def close_connection():
    if connection:
        connection.close()
        print("Database connection closed")
