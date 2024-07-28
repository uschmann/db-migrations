import os
import sys
from .Migration import Migration 
from .MigrationLogRepository import MigrationLogRepository

class MigrationManager():
    def __init__(self, engine, migrationLogRepository: MigrationLogRepository, basedir='sql'):
        self.engine = engine
        self.migrationLogRepository = migrationLogRepository
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
        batch = self.migrationLogRepository.get_last_batch() + 1
        
        for migration in self.migrations:
            if(migration.has_up() and self.migrationLogRepository.is_migration_executed(migration.name) == False): 
                migration.up.execute(self.engine)
                self.migrationLogRepository.add_migration_log(migration.name, batch)
    
    def run_down(self):
        migrationLogs = self.migrationLogRepository.get_last_migration_logs()
        
        for migrationLog in migrationLogs:
            migration = next(x for x in self.migrations if x.name == migrationLog.name)
            
            if(migration.has_down()): 
                migration.down.execute(self.engine)
                self.migrationLogRepository.delete_migration_log_by_name(migration.name)
