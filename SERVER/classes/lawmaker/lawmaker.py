import mysql.connector
from mysql.connector import cursor
from classes.utils import utils
import datetime
import json

#testing 3
class Lawmaker:            
    db_conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database='lawmaker'

    )
    cur = db_conn.cursor()

    def index(self):
        return {"Hellllo": "Lawmaker"}

    def view(self):
        return {"LAWMAKER": "VIEW"}


    def show(self , id):
        return {"LAWwwMAKER_SHOW": id}

    def search(self, law_string):
        return {"LAWMAKER_SEEARCH": law_string}
