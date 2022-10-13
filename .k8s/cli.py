#!/usr/bin/python
import click
import commands
import time


@click.group()
def main():
    """This script enriches Skaffold to run the given commands in K8s for the matrix support."""
    pass

main.add_command(commands.generate)
main.add_command(commands.build)
main.add_command(commands.test)
main.add_command(commands.results)

if __name__ == '__main__':
    start_time = time.time()
    try:
        main()
    finally:
        click.echo(click.style("Command took %.1f seconds" % (time.time() - start_time), fg='white'))
