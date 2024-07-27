from sqlalchemy import Table, Column, Integer, String, Identity
from sqlalchemy import MetaData



class Storage():
    def __init__(self, engine, migration_table = 'migrations'):
        self.migration_table = migration_table
        self.engine = engine
        self.metadata = MetaData()

    def create_migration_table(self):
        Table(
            self.migration_table,
            self.metadata,
            Column("id", Integer, Identity(start=1), primary_key=True),
            Column("migration", String(255)),
            Column("batch", Integer),
        )
        self.metadata.create_all(self.engine, checkfirst=True)


