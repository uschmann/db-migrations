from sqlalchemy import text
import re
from .SqlPlus import execute_script

class SqlFile():
    def __init__(self, filename) -> None:
        self.filename = filename
    
    def execute(self, engine):
        print(f'Running: {self.filename}')
        output = execute_script(self.filename)
        print(output)
    