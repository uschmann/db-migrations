from .models import MigrationLog
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy import delete

class MigrationLogRepository():
    def __init__(self, engine):
        self.engine = engine
    
    def add_migration_log(self, name, batch):
        with Session(self.engine) as session:
            migrationLog = MigrationLog(
                name = name, 
                batch = batch
            )
            
            session.add(migrationLog)
            session.commit()
            
    def get_next_batch(self):
        with Session(self.engine) as session:
            stmt = select(MigrationLog).order_by(MigrationLog.batch.desc())
            
            migrationLog = session.scalar(stmt)
            
            if(migrationLog == None):
                return 1
            
            return migrationLog.batch + 1;
    
    def is_migration_executed(self, name):
        with Session(self.engine) as session:
            stmt = select(MigrationLog).where(MigrationLog.name == name).exists()
            
            return session.scalar(select(stmt))
        
    def delete_all_migration_logs(self):
        with Session(self.engine) as session:
            stmt = delete(MigrationLog)
            
            session.execute(stmt)
            session.commit()
        