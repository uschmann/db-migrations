from .config import config
import subprocess


def execute_script(script):
    user = config['database']['user']
    password = config['database']['password'] 
    host = config['database']['host']
    port = config['database']['port']
    service = config['database']['service']
    
    cmd = f'echo exit | sqlplus {user}/{password}@{host}:{port}/{service} @{script}'
    
    return subprocess.getoutput(cmd)
    