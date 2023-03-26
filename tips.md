# Click tips
## naming convention
The **add-todo** vs **add_todo** naming difference is due to how Click translates Python function names to command names. By default, ``Click`` will convert *underscores* to *hyphens* and lowercase all letters. So if you define a function named add_todo and you don't specify a custom command name, the command name will be **add-todo**.

If you want to change the command names to use underscores instead, you can use the name parameter of the click.command decorator, like this:
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
To open the settings.json file to set some parameters like terminal.integrated.rendererType, follow these steps:

1. Open VSCode
2. Open the Command Palette by pressing Ctrl+Shift+P on Windows/Linux or Cmd+Shift+P on Mac.
3. Type Preferences: Open Settings (JSON) and press Enter.
4. Add the following line to the JSON object: "terminal.integrated.rendererType": "dom" (or "canvas" if you prefer the canvas renderer)
5. Save the settings.json file and close it.

## highlight a line
when having many sections in a markdown file, the titles of section become very similar to the normal text. Typically when using "###"+ title. 

In order to highlight section we can use >:
> #### highlighted section

## correct spelling in the code
``Code Spell Checker `` is an extension that highlights spelling mistakes in the code and allows you to cycle through them with keyboard shortcuts.
To use it in VS Code, you can follow these steps:

1. Install the extension by going to the Extensions tab in VS Code and searching for "Code Spell Checker". Click Install and then Reload when prompted.

2. Open a file that you want to spell-check.

3. The extension will start highlighting words that it thinks are misspelled. To correct a spelling mistake, you can right-click on the word and select from the suggestions provided.

4. To see a list of all spelling mistakes in your file, you can open the Command Palette (``Ctrl + Shift + P``) and search for "**Code Spell Checker: Show Report**". This will open a new panel that lists all the spelling mistakes in your file.

5. You can navigate through the list of spelling mistakes using the up and down arrow keys, and make changes as needed.

6. Once you've corrected all the spelling mistakes, you can save your file and close the Code Spell Checker report panel.

Note that you can also configure Code Spell Checker to ignore certain words or patterns by adding them to a configuration file. You can access the configuration file by:
1. open Preferences tab in VS Code 
2. select "Settings".
3. search for "Code Spell Checker" 
4. click "Edit in settings.json". 
5. In the settings file, you can add an "ignoreWords" or "ignoreRegExp" property to specify words or patterns to ignore.
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


## tag a commit
To tag a commit in Git, you can use the git tag command. Here are the steps:

First, identify the commit you want to tag. You can use the ``git log`` command to view a list of recent commits, along with their commit IDs.

Once you've identified the commit you want to tag, use run:

```
git tag <tag-name> <commit-ID>
# example
git tag v1.0.0 abcdef123456
```
This creates a new tag called v1.0.0 that points to the commit with ID abcdef123456.

By default, the tag will be created on your local machine. To push the tag to GitHub, use the git push command with the --tags flag. For example:

```git
git push --tags
```
This will push all local tags to the remote repository, making them available to other users who clone the repository.

To **tag a new commit**, you can use the following command:

```git
git tag <tag_name>
```
This will create a new tag pointing to the current commit.

If you want to include a message with the tag, you can use the -a option:

```git
git tag -a <tag_name> -m "<message>"
```

After creating the tag, you can push it to the remote repository using:

```git
git push origin <tag_name>
```

To add a message to a tag that already exists:
```bash
git tag -f v1.0 -m "This is a new message for tag v1.0"
```
This will update the tag v1.0 with the new message. 

Note that using the -f flag can be dangerous as it overwrites the existing tag with the same name, so use it with caution.

## make Release in github
To make automatic releases using Jenkins, you can use a Jenkins job that is triggered by a Git webhook. The Jenkins job can then perform the following steps:

1. Clone the Git repository.
2. Build the Python package.
3. Create a release tag in Git with the package version.
4. Create a release on GitHub with the same release tag.
5. Upload the package to PyPI.
Here is an example Jenkinsfile that performs these steps:

```jenkins
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python setup.py sdist bdist_wheel'
            }
        }

        stage('Create tag') {
            steps {
                sh "git tag $(python setup.py --version)"
                sh "git push origin $(python setup.py --version)"
            }
        }

        stage('Create GitHub release') {
            steps {
                withCredentials([string(credentialsId: 'github_token', variable: 'GITHUB_TOKEN')]) {
                    sh "curl -H 'Authorization: token ${GITHUB_TOKEN}' -X POST https://api.github.com/repos/<owner>/<repo>/releases -d '{\"tag_name\":\"$(python setup.py --version)\"}'"
                }
            }
        }

        stage('Upload to PyPI') {
            steps {
                withCredentials([string(credentialsId: 'pypi_credentials', variable: 'PYPI_CREDENTIALS')]) {
                    sh "twine upload -u __token__ -p ${PYPI_CREDENTIALS} dist/*"
                }
            }
        }
    }
}
```
This Jenkinsfile assumes that you have defined two credentials in Jenkins: 
    * **github_token**: should contain a personal access token with the repo scope
    * **pypi_credentials**: should contain the username and password for your PyPI account.

To use this Jenkinsfile, you can create a new Pipeline job in Jenkins and select "``Pipeline script from SCM``" as the ``Pipeline`` definition. Then, configure the job to use your Git repository and select "``GitHub hook trigger for GITScm polling``" as the **Build Trigger**. Finally, configure the owner and repo variables in the Create GitHub release stage to match your GitHub repository.

## install tree
tree command is not included by default in Git Bash, but you can install it using the following steps:

> ### Method 1: install
1. Download the tree executable file for Windows from its official website: http://gnuwin32.sourceforge.net/packages/tree.htm

2. Extract the downloaded ZIP file to a directory, for example, **C:\Program Files\Git\mingw64\bin\tree**.

3. Add the directory containing the tree executable to your PATH environment variable. You can do this by adding the following line to your **~/.bashrc** file (create the file if it doesn't exist):

```bash
export PATH="/c/Program Files/Git/mingw64/bin/tree:$PATH"
```
4. Restart Git Bash, and the tree command should now be available.

> ### Method 2: using Chocolatey
To install the tree command on git bash and PowerShell, you can use the following steps:

1. Install Chocolatey package manager by following the instructions on the official website: https://chocolatey.org/install

2. Open PowerShell as an administrator.

3. Install the tree command using Chocolatey by running the following command:
```powershell
choco install tree
```

4. Once the installation is complete, you can use the tree command in PowerShell by running:
```powershell
tree <directory_path>
# if want to exclude some folders as they have many suborders or files
tree <directory_path> -I "<exclude_folder>|<exclude_folder2>"
```

## move files

If you want to move a file or a directory without losing the git tracking history, you can use the git mv command instead of the regular mv command.

```bash
git mv <source> <destination>
```
This command will move the file or directory from <source> to <destination> and also tell git to track the move. This means that git will know that the file has been moved and it will preserve the history of the file.

Note that if you move a file or a directory without using git mv, git will not be able to track the move and you will lose the history of the file.

You can also use the same command to rename a folder:

```bash
git mv old_folder new_folder
```