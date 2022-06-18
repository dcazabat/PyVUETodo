from pathlib import Path

from flask import Config

BASE_DIR=Path(__file__).parent

class Config:
    # SECRET_KEY = 'secret'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + BASE_DIR.joinpath('db.sqlite')
    SQLALCHEMY_TRACK_MODIFICATIONS = False