# Todo List CLI

This is a command-line interface (CLI) tool for managing a todo list. 
- add_todo: Add a new todo to the list.
- delete_todos: Delete the specified todo entries from the list.
- list_todos: List all the todos in the file, optionally filtering by priority.

## Installation

1. Clone the repository: `git clone https://github.com/example/todo-cli.git`
2. Navigate to the project directory: `cd todo-cli`
3. Install the required packages: `pip install -r requirements.txt`

## Usage

The CLI tool provides the following commands:

### Add a new todo item



# test cases
## Test add_todo function with valid inputs:
```python
>>> with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
...     f.write("Test Todo: This is a test todo [Priority: Medium]\n")
>>> result = click.testing.CliRunner().invoke(list_todos)
>>> assert result.exit_code == 0
>>> assert "(0) - Test Todo: This is a test todo [Priority: Medium]" in result.output
```

## Test delete_todos function with valid inputs:

```python
>>> with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
...     f.write("Test Todo: This is a test todo [Priority: Medium]\n")
>>> result = click.testing.CliRunner().invoke(delete_todos, ["0"])
>>> assert result.exit_code == 0
>>> with open(DEFAULT_FILE, "r", encoding="utf-8") as f:
...     contents = f.read()
>>> assert contents == ""
```

## Test add_todo function with invalid priority input:
```python
>>> result = click.testing.CliRunner().invoke(
...     add_todo, ["--name", "Test Todo", "--desc", "This is a test todo", "--priority", "invalid"]
... )
>>> assert result.exit_code != 0
>>> assert "Invalid value for '-p' / '--priority': invalid" in result.output
```

## Test delete_todos function with invalid index input:
```python
>>> with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
...     f.write("Test Todo: This is a test todo [Priority: Medium]\n")
>>> result = click.testing.CliRunner().invoke(delete_todos, ["1"])
>>> assert result.exit_code != 0
>>> assert "Cannot delete the entry 1" in result.output


