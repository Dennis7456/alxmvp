import click
from flask.cli import with_appcontext

from hirehub import db
from hirehub.models import User, JobPost, Profile, JobApplication

@click.command(name='create_tables')
@with_appcontext
def create_tables():
	db.create_all

	