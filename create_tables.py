from migration.database import engine
from migration.models import Base

Base.metadata.create_all(engine, checkfirst=True)