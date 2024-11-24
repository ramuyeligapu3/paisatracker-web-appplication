# import sqlite3
# import click

# def get_db():

#     db = sqlite3.connect("expenses.db")
#     return db

# def init_db():

#     db = get_db()

#     with open("create_db.sql", "r") as f:
#         sql_script = f.read()

#     cursor = db.cursor()
#     cursor.executescript(sql_script)
#     db.commit()
#     db.close()


# @click.command("init-db")
# def init_db_command():
#     init_db()
#     click.echo("Database initialized.")

# # main
# if __name__ == "__main__":
#     init_db_command()
import psycopg2
import click

# # Replace with your Railway PostgreSQL connection URL
# DATABASE_URL = "postgresql://postgres:UdyTcPbTWFObZbISNzexqIdGApqLtauN@junction.proxy.rlwy.net:25810/railwayimport psycopg2"

# def get_db():
#     # Connect to the PostgreSQL database
#     conn = psycopg2.connect(DATABASE_URL)
#     return conn

# def init_db():
#     # Initialize the database
#     db = get_db()
#     cursor = db.cursor()

#     # Load and execute SQL script for initializing tables
#     with open("create_db.sql", "r") as f:
#         sql_script = f.read()
#         cursor.execute(sql_script)

#     db.commit()
#     cursor.close()
#     db.close()

# @click.command("init-db")
# def init_db_command():
#     init_db()
#     click.echo("Database initialized on Railway PostgreSQL.")

# # main
# if __name__ == "__main__":
#     init_db_command()
# import psycopg2

# DATABASE_URL = "postgresql://postgres:UdyTcPbTWFObZbISNzexqIdGApqLtauN@junction.proxy.rlwy.net:25810/railway"

# try:
#     # Establish connection
#     conn = psycopg2.connect(DATABASE_URL)
#     print("Connection successful!")
#     conn.close()
# except Exception as e:
#     print("Failed to connect to the database:", e)
import psycopg2
import click

DATABASE_URL = "postgresql://postgres:UdyTcPbTWFObZbISNzexqIdGApqLtauN@junction.proxy.rlwy.net:25810/railway"

def get_db():
    """Connect to the database."""
    conn = psycopg2.connect(DATABASE_URL)
    return conn

def init_db():
    """Run the SQL script to initialize tables."""
    conn = get_db()
    cursor = conn.cursor()

    with open("create_db.sql", "r") as f:
        sql_script = f.read()
        cursor.execute(sql_script)

    conn.commit()
    cursor.close()
    conn.close()

@click.command("init-db")
def init_db_command():
    """Command to initialize the database."""
    init_db()
    click.echo("Database initialized successfully!")

if __name__ == "__main__":
    init_db_command()
