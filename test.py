from rich.console import Console
from rich.table import Table
from time import sleep

console = Console()
table = Table(title="Running migrations")


with console.status('Working') as status:
    table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Box Office", justify="right", style="green")
    console.clear()
    table.add_row("foo", "bar", "OK")
    console.print(table)
    sleep(2)
    console.clear()
    table.add_row("foo", "bar", "OK")
    console.print(table)
    sleep(2)
    console.clear()
    table.add_row("foo", "bar", "OK")
    console.print(table)
    sleep(2)
    console.clear()
    table.add_row("foo", "bar", "OK")
    console.print(table)
