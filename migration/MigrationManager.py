import os
import sys
from .Migration import Migration 
from .MigrationLogRepository import MigrationLogRepository
from .console import log_up, log_down, log_nothing_to_migrate, log_error
from .SqlError import SqlError

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
                
        return self.migrations
                
    def run_up(self):
        batch = self.migrationLogRepository.get_last_batch() + 1
        
        migrationsToRun = []
        for migration in self.migrations:
            if(migration.has_up() and self.migrationLogRepository.is_migration_executed(migration.name) == False): 
                migrationsToRun.append(migration)
            
        if(len(migrationsToRun) == 0):
            log_nothing_to_migrate()
            return False
            
        for migration in migrationsToRun:
            if(migration.has_up() and self.migrationLogRepository.is_migration_executed(migration.name) == False): 
                log_up(migration)
                try:
                    migration.up.execute(self.engine)
                    self.migrationLogRepository.add_migration_log(migration.name, batch)
                except SqlError as error:
                    msg = error.args[0]
                    log_error(msg)
                    sys.exit(1)
        
        return True
    
    def run_down(self):
        migrationLogs = self.migrationLogRepository.get_last_migration_logs()
        
        if(len(migrationLogs) == 0):
            log_nothing_to_migrate()
            return False
        
        for migrationLog in migrationLogs:
            migration = next(x for x in self.migrations if x.name == migrationLog.name)
            
            if(migration.has_down()): 
                log_down(migration)
                try:
                    migration.down.execute(self.engine)
                    self.migrationLogRepository.delete_migration_log_by_name(migration.name)
                except SqlError as error:
                    msg = error.args[0]
                    log_error(msg)
                    sys.exit(1)
                    
        return True
