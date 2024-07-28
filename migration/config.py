import os
from dotenv import load_dotenv

load_dotenv(override=True)


config = {
    "database": {
        "user": os.environ.get('DB_USER'),
        "password": os.environ.get('DB_PASSWORD'), 
        "host": os.environ.get('DB_HOST'), 
        "port": os.environ.get('DB_PORT'), 
        "service": os.environ.get('DB_SERVICE'), 
        "tns": os.environ.get('DB_TNS')
    }
}
