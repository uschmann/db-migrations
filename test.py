from migration.database import engine
from migration.MigrationLogRepository import MigrationLogRepository

repo = MigrationLogRepository(engine)

print(repo.get_next_batch())
repo.delete_all_migration_logs()

print(repo.get_next_batch())