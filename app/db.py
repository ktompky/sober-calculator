import sqlite3
import click
from flask import current_app, g


#creating the database
def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
        db.commit()

@click.command('init-db')
@with_appcontext
def init_db_command():
    """clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database')