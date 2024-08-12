import sqlite3
import click

def get_db():

    db = sqlite3.connect("expenses.db")
    return db

def init_db():

    db = get_db()

    with open("create_db.sql", "r") as f:
        sql_script = f.read()

    cursor = db.cursor()
    cursor.executescript(sql_script)
    db.commit()
    db.close()


@click.command("init-db")
def init_db_command():
    init_db()
    click.echo("Database initialized.")

# main
if __name__ == "__main__":
    init_db_command()