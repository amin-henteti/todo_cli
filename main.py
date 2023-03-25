
import click
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning, module="pyreadline.py3k_compat")

# Dictionary mapping priority keys to priority names
PRIORITIES = {"o": "Optional", "l": "Low", "m": "Medium", "h": "High", "c": "Crucial"}

# List of all priority keys and priority names
PRIORITIES_LIST = list(PRIORITIES.keys()) + list(PRIORITIES.values())

# Default file to store todos
DEFAULT_FILE = "mytodos.txt"


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES_LIST), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
@click.option("-n", "--name", prompt="Enter the todo name", help="The name of the todo")
@click.option(
    "-d", "--desc", prompt="Describe the todo", help="The description of the todo task"
)
def add_todo(name, desc, priority, todofile):
    """
    Add a new todo to the list.
    :param name: name of the todo
    :param desc: description of the todo
    :param priority: priority of the todo, defaults to 'Medium'
    :param todofile: file to store the todos, defaults to 'mytodos.txt'
    """
    filename = todofile if todofile is not None else DEFAULT_FILE
    with open(filename, "a+", encoding="utf-8") as f:
        f.write(f"{name}: {desc} [Priority: {PRIORITIES[priority]}]")


@click.command()
@click.argument("priority", type=click.Choice(PRIORITIES.keys()), default="m")
@click.argument("todofile", type=click.Path(exists=False), required=False)
def list_todos(priority, todofile):
    """
    List all the todos in the file, optionally filtering by priority.
    :param priority: priority to filter by, defaults to 'Medium'
    :param todofile: file to read the todos from, defaults to 'mytodos.txt'
    """
    filename = todofile if todofile is not None else DEFAULT_FILE
    with open(filename, "r", encoding="utf-8") as f:
        todo_list = f.read().splitlines()
    filter_str = "" if priority is None else f"[Priority: {PRIORITIES[priority]}]"
    out_list = [
        f"({i}) - {todo}" for i, todo in enumerate(todo_list) if filter_str in todo
    ]
    click.echo("\n".join(out_list))


@click.command()
@click.argument(
    "indexes",
    type=click.Int(),
    nargs=-1,
    required=True,
    help="indexes of the todo entries to delete from the list",
)
@click.argument("todofile", type=click.Path(exists=False), required=False)
def delete_todos(indexes, todofile):
    """
    Delete the specified todo entries from the list.
    :param indexes: indexes of the todo entries to delete
    :param todofile: file to read the todos from, defaults to 'mytodos.txt'
    """

    filename = todofile if todofile is not None else DEFAULT_FILE
    with open(filename, "r", encoding="utf-8") as f:
        todo_list = f.read().splitlines()
    # Convert the indexes to a set to remove duplicates, then sort in reverse order
    # to avoid problems with deleting multiple items from the list.
    indexes_set = set(indexes)
    indexes_sorted = sorted(indexes_set, reverse=True)
    # Delete each item in the list one by one, starting from the end
    for index in indexes_sorted:
        if index >= len(todo_list):
            click.echo(
                f"Cannot delete the entry {index} because it exceeds the entries that currently exist ({len(todo_list)})"
            )
        else:
            del todo_list[index]
    with open(filename, "w", encoding="utf-8") as f:
        f.write("\n".join(todo_list))


@click.combine()
def mycommands():
    """Combines multiple click commands"""
    print("running commands")

mycommands.add_command(add_todo)
mycommands.add_command(delete_todos)
mycommands.add_command(list_todos)


if __name__ == "__main__":
    mycommands()
