from rich.console import Console

console = Console()


def log_nothing_to_migrate():
    console.log('Nothing to migrate');

def log_up(migration):
    console.log(f'Running [green bold]{migration.name}', end="")
    
def log_down(migration):
    console.log(f'Rollback [red bold]{migration.name}')