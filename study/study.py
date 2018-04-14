import click
import mysql.connector
import uuid
from random import randint


@click.group()
def cli():
    """Study Mysql"""


def with_connection(config: dict, f) -> None:
    """manages a connection"""
    try:
        conn = mysql.connector.connect(**config)
        f(conn)
    finally:
        conn.commit()
        conn.close()
    return None


def with_cursor(conn, f) -> None:
    """manages a cursor"""
    try:
        cursor = conn.cursor()
        f(cursor)
    finally:
        cursor.close()
    return None


def create_config(user: str, password: str, host: str, database: str) -> dict:
    """creates a database config"""
    return {
        'user': user,
        'password': password,
        'host': host,
        'database': database,
        'raise_on_warnings': True,
    }


@cli.command('create-table')
@click.option('--user', default='root', help='The database username')
@click.option('--password', default='root', help='The database password')
@click.option('--host', default='localhost', help='The database host')
@click.option('--database', default='mysql', help='The database name')
def create_table(user: str, password: str, host: str, database: str) -> None:
    """Create the person table"""
    cfg = create_config(user, password, host, database)
    with_connection(cfg, lambda conn: with_cursor(conn, lambda cursor: cursor.execute("""
            CREATE TABLE `person` (
              `id` int(11) PRIMARY KEY NOT NULL AUTO_INCREMENT,
              `name` VARCHAR(255) NOT NULL,
              `age` int(11) NOT NULL
            ) 
        """)))
    return None


@cli.command('insert-person')
@click.option('--user', default='root', help='The database username')
@click.option('--password', default='root', help='The database password')
@click.option('--host', default='localhost', help='The database host')
@click.option('--database', default='mysql', help='The database name')
@click.option('--name', default=None, help='The name of the person to insert')
@click.option('--age', default=None, help='The age of the person to insert')
def create_table(user: str, password: str, host: str, database: str, name: str, age: int) -> None:
    """Insert a person"""
    def insert_person(cursor):
        sql = """INSERT INTO person (name, age) VALUES (%s, %s)"""
        cursor.execute(sql, (name if name else str(uuid.uuid4()), age if age else randint(1, 101)))

    cfg = create_config(user, password, host, database)
    with_connection(cfg, lambda conn: with_cursor(conn, insert_person))
    return None


@cli.command('list-persons')
@click.option('--user', default='root', help='The database username')
@click.option('--password', default='root', help='The database password')
@click.option('--host', default='localhost', help='The database host')
@click.option('--database', default='mysql', help='The database name')
def list_persons(user: str, password: str, host: str, database: str) -> None:
    """lists the person table"""
    def print_persons(cursor) -> None:
        query = "SELECT * FROM `person`"
        cursor.execute(query)
        for (_id, name, age) in cursor:
            print(f"Person({_id}, {name}, {age})")
        return None

    cfg = create_config(user, password, host, database)
    with_connection(cfg, lambda conn: with_cursor(conn, print_persons))
    return None


if __name__ == "__main__":
    cli()
