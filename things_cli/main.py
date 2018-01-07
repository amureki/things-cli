import sys

import click

from .smtp import send_email_message


@click.group()
def cli():
    """Command-line interface for Things 3"""


@cli.command('add', short_help='Add new task to Inbox.')
@click.argument('task')
@click.argument('note', required=False)
def add(task, note):
    """Adds new task to Inbox via Mail to Things feature."""
    task_sent = send_email_message(subject=task, body=note or '')
    if task_sent:
        click.echo('Task "{}" added to inbox!'.format(task))
    else:
        click.echo('Task was not added, please, check logs.')


if __name__ == '__main__':
    sys.exit(cli())
