"""
This is an example How to use click package to create a professional CLI
"""

import click

PRIORITIES = {
    "o": "Optional",
    "2": "Low",
    "m": "Medium",
    "h": "High",
    "c": "Crucial"
}
PRIORITIES_LIST = list(PRIORITIES.keys()) + list(PRIORITIES.values())
DEFAULT_FILE = "mytodos.txt"


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES_LIST), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option("-n", "--name", prompt="Enter the todo name", help="The name of the todo")
@click.option("-d", "--desc", prompt="Describe the todo", help="The description of the todo task")
def add_todo(name, desc, priority, todofile):
    filename = todofile if todofile is not None else DEFAULT_FILE
    # "a+" mode is to add to file if it does not exist otherwise create it
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]\n")
    click.echo("Todo added successfully")


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
def list_todos(priority, todofile):
    filename = todofile if todofile is not None else DEFAULT_FILE
    with open(filename, "r", encoding="utf-8") as f:
        todo_list = f.read().splitlines()
    filter_str = "" if priority is None else f"[Priority: {PRIORITIES[priority]}]"
    out_list = [f"({i}) - {todo}" for i, todo in enumerate(todo_list) if filter_str in todo]
    if out_list:
        click.echo("\n".join(out_list))
    else:
        click.echo("No todos found")


@click.command()
@click.argument("indexes", type=click.IntRange(min=0), nargs=-1, required=True, help="indexes of the todo entries to delete from the list")
@click.argument("todofile", type=click.Path(exists=False), required=False)
def delete_todo(indexes, todofile=None):
    """
    Delete one or more items from the todo list.

    Parameters:
        indexes (tuple): The indexes of the items to delete. Allows for multiple arguments with the nargs=-1 option.
        todofile (str): The file path of the todo list. If not provided, the default file will be used.

    """
    filename = todofile or DEFAULT_FILE
    with open(filename, "r", encoding="utf-8") as f:
        todo_list = f.read().splitlines()

    # Convert to set to remove duplicates and sort in reverse order to avoid deleting the wrong items
    indexes = sorted(set(indexes), reverse=True)

    for index in indexes:
        if index >= len(todo_list):
            click.echo(f"Cannot delete the entry {index} because it exceeds the entries that currently exist ({len(todo_list)})")
            continue
        # Delete the item from the list
        del todo_list[index]

    # Write the updated list back to the file
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(todo_list))


@click.group()
def mycommands():
    pass


mycommands.add_command(add_todo)
mycommands.add_command(delete_todo)
mycommands.add_command(list_todos)


if __name__ == "__main__":
    mycommands()
