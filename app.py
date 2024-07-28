from migration.MigrationManager import MigrationManager
from migration.database import engine
from migration.MigrationLogRepository import MigrationLogRepository
import click
from migration.models import Base
from migration.MigationGenerator import MigrationGenerator

main = click.Group(help="Oracle schema manager")

@main.command('migrate', help='Execute the migration files')
def migrate():
   Base.metadata.create_all(engine, checkfirst=True)
   
   migrationLogRepository = MigrationLogRepository(engine)
   migrationManager = MigrationManager(engine, migrationLogRepository)
   
   migrationManager.run_up()


@main.command('rollback', help='Roll back the last migration')
def rollback():
   Base.metadata.create_all(engine, checkfirst=True)
   
   migrationLogRepository = MigrationLogRepository(engine)
   migrationManager = MigrationManager(engine, migrationLogRepository)
   
   migrationManager.run_down()
   
@main.command('make', help='Creates a new migration folder')
@click.argument('name')
@click.option('-t', type=str)
def make(name, t):
   generator = MigrationGenerator()
   generator.generate_migration(name, t)

if __name__ == '__main__':
    main()
