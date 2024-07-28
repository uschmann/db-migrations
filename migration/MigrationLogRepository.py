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
    
    def delete_migration_log_by_name(self, name):
        with Session(self.engine) as session:
            stmt = delete(MigrationLog).where(MigrationLog.name == name)
            
            session.execute(stmt)
            session.commit()
            
    def get_batch_by_name(self, name):
        with Session(self.engine) as session:
            stmt = select(MigrationLog).where(MigrationLog.name == name)
            
            migrationLog = session.scalar(stmt)
            return migrationLog.batch
            
    def get_last_migration_logs(self):
        with Session(self.engine)as sesssion:
            batch = self.get_last_batch()
            stmt = select(MigrationLog).where(MigrationLog.batch == batch).order_by(MigrationLog.name.desc())

            return sesssion.scalars(stmt).all()

    def get_last_batch(self):
        with Session(self.engine) as session:
            stmt = select(MigrationLog).order_by(MigrationLog.batch.desc())
            
            migrationLog = session.scalar(stmt)
            
            if(migrationLog == None):
                return 0
            
            return migrationLog.batch;
    
    def is_migration_executed(self, name):
        with Session(self.engine) as session:
            stmt = select(MigrationLog).where(MigrationLog.name == name).exists()
            
            return session.scalar(select(stmt))
        
    def delete_all_migration_logs(self):
        with Session(self.engine) as session:
            stmt = delete(MigrationLog)
            
            session.execute(stmt)
            session.commit()
        