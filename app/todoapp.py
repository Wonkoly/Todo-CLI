import click
from task import Task
from tasklist import TaskList

task_list = TaskList('todo.db')

@click.group()
def cli():
    pass

@cli.command()
@click.argument('description')
def add(description):
    """Add a new task."""
    task_list.add_task(description)
    click.echo('Task added successfully.')

@cli.command()
def list():
    """List all tasks."""
    tasks = task_list.get_all_tasks()
    if tasks:
        click.echo("Tasks:")
        for task in tasks:
            click.echo(f"- {task[1]} {'(completed)' if task[2] else ''}")
    else:
        click.echo("No tasks found.")

@cli.command()
@click.argument('task_id', type=int)
def complete(task_id):
    """Mark a task as completed."""
    task_list.complete_task(task_id)
    click.echo('Task marked as completed.')

@cli.command()
@click.argument('task_id', type=int)
def delete(task_id):
    """Delete a task."""
    task_list.delete_task(task_id)
    click.echo('Task deleted successfully.')

if __name__ == '__main__':
    cli()
