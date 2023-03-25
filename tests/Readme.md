# How to test
## Automated tests
the `tests` folder contains automated tests for the Todo CLI application.

How to run tests
To run the tests, navigate to the tests folder in your terminal and run the following 
```bash
pytest
# view more logs
pytest -v -s
# view only failed tests
pytest -p no:warnings
pytest -W ignore::DeprecationWarning
```

## Manual tests
The following are manual tests that can be performed to verify the functionality of the ``todo_cli`` program:

> ### Test **add_todo** function with valid inputs
This test case verifies that the **add_todo** function works correctly when given valid input. 

It creates a test TODO item with a medium priority and adds it to the list. It then verifies that the list of todos contains the test item.

To run this test case, open a terminal and navigate to the project directory. Then execute the following command:

```python
python -m pytest tests/test_todo.py::test_add_todo_valid
```

> ## Test delete_todos function with valid inputs
This test case verifies that the delete_todos function handles invalid index input correctly. It creates a test TODO item with a medium priority and adds it to the list. It then attempts to delete an item with an index that is out of range and verifies that an error message is displayed.

To run this test case, open a terminal and navigate to the project directory. Then execute the following command:

```python
python -m pytest tests/test_todo.py::test_delete_todos_invalid_index
```

## interactive test

Alternatively, you can run the ``click.testing.CliRunner().invoke(list_todos)`` command directly in the *Python interactive shell* by launching the shell in the same directory as where the file that contain list_todos function. Just type the command after importing the necessary modules and functions
```python
>>> import click
>>> from main import list_todos
>>> runner = click.testing.CliRunner()
>>> result = runner.invoke(list_todos)
>>> print(result.output)
```
`click.testing.CliRunner().invoke(func)` is used to simulate the command-line interface (CLI) of a Python script and invoke one of its commands in a testing environment.

The ``Click`` library have the `CliRunner()` class, which creates a testing environment for invoking commands of a Click-based CLI. `invoke()` is a method of CliRunner() that simulates a command-line input and returns the output and the exit code of the command.
These can then be tested against expected values to ensure that the command is functioning as expected.
