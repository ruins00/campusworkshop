"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagijhp8u791gu2ukg-a.singapore-postgres.render.com",
        database="todo_52s7",
        user="todo_52s7_user",
        password="cnRdixiRjwLnGPoW3yX7cHdUgEjTBPjX")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
