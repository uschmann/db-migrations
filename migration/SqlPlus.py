from .config import config
import subprocess
from .console import console
import re
from .SqlError import SqlError

def execute_script(script):
    user = config['database']['user']
    password = config['database']['password'] 
    host = config['database']['host']
    port = config['database']['port']
    service = config['database']['service']
    
    cmd = f'echo exit | sqlplus {user}/{password}@{host}:{port}/{service} @{script}'
    
    process = subprocess.run(cmd, shell=True, capture_output=True)
    
    if process.returncode != 0:
        output = process.stdout.decode()
        raise SqlError(output)

    return process
    