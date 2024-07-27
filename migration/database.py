from .config import config
from sqlalchemy import create_engine

user = config['database']['user']
password = config['database']['password'] 
dsn = config['database']['tns']
host = config['database']['host']
port = config['database']['port']
service = config['database']['service']

engine = create_engine(
    f'oracle+oracledb://{user}:{password}@{host}:{port}/?service_name={service}',
    thick_mode=None
    )