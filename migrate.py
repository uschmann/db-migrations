from migration.MigrationManager import MigrationManager
from migration.Storage import Storage
from migration.database import engine
import click


@click.command()
@click.option('--rollback/--no-rollback', default=False, help='Rollback the last batch')
def migrate(rollback):
   storage = Storage(engine)
   migrationManager = MigrationManager(engine)
   
   if(rollback == False):
      migrationManager.run_up()
   else:
      migrationManager.run_down()


if __name__ == '__main__':
    migrate()
