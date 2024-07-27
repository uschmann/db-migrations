import os
import sys
from .Migration import Migration 

class MigrationManager():
    def __init__(self, engine, basedir='sql'):
        self.engine = engine
        self.basedir = os.path.dirname(os.path.realpath(sys.argv[0])) + f'/{basedir}'
        self.migrations = []
        self.read_migrations()
    
    def read_migrations(self):
        dirs = os.listdir(self.basedir)
        dirs.sort()
        
        for dir in dirs:
            if(os.path.isdir(self.basedir + '/' + dir)):
                migration = Migration(dir, self.basedir)
                self.migrations.append(migration)
                
    def run_up(self):
        for migration in self.migrations:
            if(migration.has_up()): 
                migration.up.execute(self.engine)
                
    def run_down(self):
        for migration in self.migrations:
            if(migration.has_down()): 
                migration.down.execute(self.engine)
