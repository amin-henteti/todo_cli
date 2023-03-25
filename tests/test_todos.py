import os
import tempfile
import pytest
from click.testing import CliRunner
from ..main import DEFAULT_FILE, add_todo, list_todos, delete_todos


def test_add_todo():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, "test_todos.txt")
        result = runner.invoke(
            add_todo, ["-n", "Test Todo", "-d", "This is a test todo.", "-p", "m", filename]
        )
        assert result.exit_code == 0
        assert os.path.exists(filename)
        with open(filename, "r") as f:
            contents = f.read()
        assert "Test Todo: This is a test todo. [Priority: Medium]" in contents


def test_delete_todos():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, "test_todos.txt")
        with open(filename, "w") as f:
            f.write("Test Todo: This is a test todo. [Priority: High]\n")
            f.write("Test Todo 2: This is another test todo. [Priority: Medium]\n")
            f.write("Test Todo 3: This is yet another test todo. [Priority: Low]\n")
        result = runner.invoke(delete_todos, ["0", "2", filename])
        assert result.exit_code == 0
        with open(filename, "r") as f:
            contents = f.read()
        assert "Test Todo: This is a test todo. [Priority: High]" not in contents
        assert "Test Todo 2: This is another test todo. [Priority: Medium]" in contents
        assert "Test Todo 3: This is yet another test todo. [Priority: Low]" not in contents

def test_list_todos():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as tempdir:
        filename = os.path.join(tempdir, "test_todos.txt")
        with open(filename, "w") as f:
            f.write("Test Todo: This is a test todo. [Priority: High]\n")
            f.write("Test Todo 2: This is another test todo. [Priority: Medium]\n")
            f.write("Test Todo 3: This is yet another test todo. [Priority: Low]\n")
        result = runner.invoke(list_todos, ["-p", "h", filename])
        assert result.exit_code == 0
        assert "Test Todo: This is a test todo. [Priority: High]" in result.output
        assert "Test Todo 2: This is another test todo. [Priority: Medium]" not in result.output
        assert "Test Todo 3: This is yet another test todo. [Priority: Low]" not in result.output


def test_add_todo_invalid_priority():
    runner = CliRunner()
    result = runner.invoke(
        add_todo, ["--name", "Test Todo", "--desc", "This is a test todo", "--priority", "invalid"]
    )
    assert result.exit_code != 0
    assert "Invalid value for '-p' / '--priority': invalid" in result.output

def test_delete_todos_invalid_index():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with open(DEFAULT_FILE, "w", encoding="utf-8") as f:
            f.write("Test Todo: This is a test todo [Priority: Medium]\n")
        result = runner.invoke(delete_todos, ["1"])
        assert result.exit_code != 0
        assert "Cannot delete the entry 1" in result.output


