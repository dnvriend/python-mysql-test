from setuptools import setup

setup(
    name='study-mysql',
    version='0.1',
    author='Dennis Vriend',
    author_email='dnvriend@gmail.com',
    description="testing python and mysql",
    licence='Apache 2.0',
    packages=['study'],
    url="https://github.com/dnvriend/python-mysql-test",
    install_requires=[
        'click',
        'mysql-connector-python'
    ],
    entry_points='''
        [console_scripts]
        study-mysql=study.study:cli
    ''',
)