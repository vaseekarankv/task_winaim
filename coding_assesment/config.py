import os
from dotenv import load_dotenv

# MySQL configuration parameters
mysql_config = {
    'host': 'localhost',
    'user': os.getenv('USER'),
    'password': os.getenv('PASSWORD'),
    'database': os.getenv('DATABASE')
}
