from migration.MigrationManager import MigrationManager
from migration.database import engine
from migration.MigrationLogRepository import MigrationLogRepository
import click
from migration.models import Base
from migration.MigationGenerator import MigrationGenerator
from rich.console import Console
from rich.table import Table
from migration.console import console

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

@main.command('status', help='Display a list of executed migrations')
def status():
   Base.metadata.create_all(engine, checkfirst=True)
   
   migrationLogRepository = MigrationLogRepository(engine)
   migrationManager = MigrationManager(engine, migrationLogRepository)
   
   table = Table()
   table.add_column("#", justify="right", style="cyan", no_wrap=True)
   table.add_column("Name", style="magenta")
   table.add_column("Batch", style="red", justify="center")
   table.add_column("Executed?", justify="right", style="green")

   count = 1
   for migration in migrationManager.migrations:
      batch = migrationLogRepository.get_batch_by_name(migration.name)
      table.add_row(f'{count}', migration.name, f'[bold green]{batch}' if batch != None else '-', '[bold]Yes' if batch != None else '[red]No')
      count += 1
   
   console.print(table)

@main.command('replay', help='Runs rollback and migrate in a row')
def replay():
   Base.metadata.create_all(engine, checkfirst=True)
   
   migrationLogRepository = MigrationLogRepository(engine)
   migrationManager = MigrationManager(engine, migrationLogRepository)
   
   migrationManager.run_down()
   migrationManager.run_up()

@main.command('reset', help='Rollback all migrations and migrate everything from scratch')
def reset():
   Base.metadata.create_all(engine, checkfirst=True)

   migrationLogRepository = MigrationLogRepository(engine)
   migrationManager = MigrationManager(engine, migrationLogRepository)

   while(migrationManager.run_down()):
      pass
   
   migrationManager.run_up()

if __name__ == '__main__':
    main()
