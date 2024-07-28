from migration.database import engine
from migration.MigrationLogRepository import MigrationLogRepository

repo = MigrationLogRepository(engine)

logs = repo.get_last_migration_logs()

res = next(x for x in logs if x.name == 'foo')
print(res)
