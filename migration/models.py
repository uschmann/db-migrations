from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import String
from sqlalchemy import Identity

class Base(DeclarativeBase):
    pass
 
class MigrationLog(Base):
    __tablename__ = 'migration_logs'
     
    id: Mapped[int] = mapped_column(Identity(start=1), primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    batch: Mapped[int]
    
    def __repr__(self) -> str:
        return f'MigrationLog(id={self.id}, name={self.name}, batch={self.batch})'