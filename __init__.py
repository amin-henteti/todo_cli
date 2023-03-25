"""
The __init__.py file is a special file that is present in Python packages. 
It can be an empty file, or it can contain Python code, 
and it serves as an indication that the directory 
should be considered as a Python package.

When a directory is marked as a package with the __init__.py file, 
Python can then import modules from the package using the dot notation. 
For example, if a package called my_package has a module called my_module, 
it can be imported with import my_package.my_module.

The __init__.py file can also contain initialization code that gets executed when the package is imported. 
This code can define variables, import modules, or run any other Python code 
that you want to execute when the package is imported.
"""

from . import main
