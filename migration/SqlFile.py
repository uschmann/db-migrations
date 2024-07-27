from sqlalchemy import text
import re

class SqlFile():
    def __init__(self, filename) -> None:
        self.filename = filename
        
        with open(filename) as file:
            self.statements = re.split(r';\s*$', file.read(), flags=re.MULTILINE)
    
    def execute(self, engine):
        with engine.connect() as connection:
            for statement in self.statements:
                if statement:
                    connection.execute(text(statement))
    