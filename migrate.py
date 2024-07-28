from migration.MigrationManager import MigrationManager
from migration.database import engine
from migration.MigrationLogRepository import MigrationLogRepository
import click
from migration.models import Base

@click.command()
@click.option('--rollback/--no-rollback', default=False, help='Rollback the last batch')
def migrate(rollback):
   Base.metadata.create_all(engine, checkfirst=True)
   
   migrationLogRepository = MigrationLogRepository(engine)
   migrationManager = MigrationManager(engine, migrationLogRepository)
   
   if(rollback == False):
      migrationManager.run_up()
   else:
      migrationManager.run_down()


if __name__ == '__main__':
    migrate()
