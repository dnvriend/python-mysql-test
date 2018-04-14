# python-mysql-test
A small study project on using mysql from Python3

## Installation
To install type:

```
$ pip3 install pipenv
$ pipenv install
$ pipenv run "python setup.py bdist_wheel"
$ pip3 install dist/study_mysql-0.1-py3-none-any.whl
```

## Uninstall
To uninstall type:

```
$ pip3 uninstall dist/shotty-0.1-py3-none-any.whl -y
```

## Running
I assume that docker and docker-compose is installed. 

To run the example type: 

```
$ ./launch-mysql.sh
$ ./create-table.sh
$ ./insert-person.sh
$ ./list-persons.sh
```

## Create the project
To create the project type:

```
$ brew install python --devel
$ pip3 install pipenv
$ pipenv --three
$ pipenv install -d ipython setuptools mypy
$ pipenv install click mysql-connector-python 
```

## Resources
- [Python tutorial](https://docs.python.org/3/tutorial/index.html)
- [Python standard library](https://docs.python.org/3/library/index.html)
- [Python built-in functions](https://docs.python.org/3/library/functions.html)
- [Python Package Index - pypi](https://pypi.python.org/pypi)
- [pipenv](https://docs.pipenv.org/)
- [IPython reference](https://ipython.org/ipython-doc/3/interactive/reference.html)
- [Setuptools - packaging python projects](https://setuptools.readthedocs.io/en/latest/)
- [MySQL Connector/Python](https://github.com/mysql/mysql-connector-python) - [docs](https://dev.mysql.com/doc/connector-python/en/)

## Docker
- [mysql](https://hub.docker.com/_/mysql/)
