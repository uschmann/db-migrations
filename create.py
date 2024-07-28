import click
from datetime import datetime
import os
import sys

def get_dir(name):
    dir = os.path.dirname(os.path.realpath(sys.argv[0])) + f'/sql'
    now = datetime.now()
    formatted = now.strftime("%Y_%m_%d_%H%M%S")
    return f'{dir}/{formatted}_{name}'

@click.command()
@click.argument('name')
def create(name):
    dir = get_dir(name)
    os.mkdir(dir)
    os.mknod(f'{dir}/up.sql')
    os.mknod(f'{dir}/down.sql')
    
    
if __name__ == '__main__':
    create()
