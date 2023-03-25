# Todo List CLI

This is a command-line interface (CLI) tool for managing a todo list. 
- **add_todo**: Add a new todo to the list.
- **delete_todos**: Delete the specified todo entries from the list.
- **list_todos**: List all the todos in the file, optionally filtering by priority.

## Installation

1. Clone the repository: `git clone https://github.com/amin-henteti/todo_cli.git`
2. Navigate to the project directory: `cd todo_cli`
3. Install the required packages: `pip install -r requirements.txt`

## Usage

The CLI tool provides the following commands:

### Add a new todo item
```bash
python todo.py add-todo [-n NAME] [-d DESC] [-p PRIORITY] [-f FILE]
```

* `-n/--name`: The name of the todo item (required).
* `-d/--desc`: The description of the todo item (required).
* `-p/--priority`: The priority of the todo item. Defaults to `m`. It value can be one of: 
    - `o` (optional)
    - `l` (low)
    - `m` (medium)
    - `h` (high)
    - `c` (crucial).
* `-f/--file`: The file to store the todos. Defaults to `mytodos.txt`.

Example: To add a new todo to the list, run the following command:

```bash
python todo.py add_todo --name "Todo name" --desc "Todo description" --priority "h" --todofile "path/to/todo/file"
```

### Delete todo items

```bash
python todo.py delete-todos INDEX [INDEX ...] [-f FILE]
```


* `INDEX`: The index of the todo item to delete (required).
* `-f/--file`: The file to read the todos from. Defaults to `mytodos.txt`.

Example: To delete one or more todos from the list, run the following command:

```python
todo.py delete_todos "index1" "index2" ... --todofile "path/to/todo/file"
```


### List all todo items

```bash 
python todo.py list-todos [-p PRIORITY] [-f FILE]
```


* `-p/--priority`: The priority to filter by.
* `-f/--file`: The file to read the todos from. Defaults to `mytodos.txt`.

Example: To list all the todos in the file, run the following command:

```bash
python todo.py list_todos --priority "h" --todofile "path/to/todo/file"
```

## Contributing

Contributions are welcome! Please see the [contribution guidelines](Extra/CONTRIBUTING.md) for details.

## License

This project is licensed under the [License](Extra/LICENSE).