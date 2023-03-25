# untrack files & folders in git
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

# Undo last commit
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