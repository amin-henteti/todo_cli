from setuptools import setup, find_packages
install_requires = open('requirements.txt').readlines()

setup(
    name='todo_cli',
    version='2.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    entry_points='''
        [console_scripts]
        todo_cli=todo_cli.main:cli
    ''',
)