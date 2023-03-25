# Click tips
## naming convention
The **add-todo** vs **add_todo** naming difference is due to how Click translates Python function names to command names. By default, ``Click`` will convert *underscores* to *hyphens* and lowercase all letters. So if you define a function named add_todo and you don't specify a custom command name, the command name will be **add-todo**.

In the provided code, the commands were defined with the function names, so you would need to call them with hyphenated names, like python myscript.py **add-todo**. If you want to change the command names to use underscores instead, you can use the name parameter of the click.command decorator, like this:
```python
@click.command(name="add_todo")
def add_todo_func():
    # ...
```
## group commands
The easy way to group/combine commands is the following
```python
@click.group()
def main():
    pass

@click.command()
def foo():
    click.echo('foo')

@click.command()
def bar():
    click.echo('bar')

main.add_command(foo)
main.add_command(bar)

if __name__ == '__main__':
    main()
```

# vscode tips 
## open the settings.json file of VSCode
To open the settings.json file to set some parametes like terminal.integrated.rendererType, follow these steps:

1. Open VSCode
2. Open the Command Palette by pressing Ctrl+Shift+P on Windows/Linux or Cmd+Shift+P on Mac.
3. Type Preferences: Open Settings (JSON) and press Enter.
4. Add the following line to the JSON object: "terminal.integrated.rendererType": "dom" (or "canvas" if you prefer the canvas renderer)
5. Save the settings.json file and close it.

# git tips
## untrack files & folders in git
To ignore all files that end with .pyc in Git, you can add the following line to your **.gitignore** file:

```bash
*.pyc
```
If you have already tracked some .pyc files in your Git repository, you will need to remove them from the repository before they will be ignored. You can do this with the following command:

```bash
git rm --cached *.pyc
```
This will remove the .pyc files from Git's index (but not from your local file system). Once you have done this and added the *.pyc line to your **.gitignore** file, Git should no longer track .pyc files.

To ignore a folder, you can simply add it name or path to your **.gitignore** file

```bash
echo "venv" >> .gitignore 
echo ".pytest_cache" >> .gitignore 
echo "tests/__pycache__" >> .gitignore 
```

## Undo last commit
To undo the last commit in Git, you can use the command 
```bash
git reset HEAD~1
```
This will remove the most recent commit from the current branch but leave the changes in your working directory.

If you also want to remove the changes from your working directory, you can use the --hard option
```bash
git reset --hard HEAD~1
```
However, be careful when using --hard as it will permanently discard any changes that have not been committed or pushed to a remote repository.

It's worth noting that if you have already pushed the commit to a remote repository, you will need to use
```bash
git push --force
```
to overwrite the remote branch with the new changes. However, be cautious when using git push --force as it can cause issues for collaborators working on the same branch.