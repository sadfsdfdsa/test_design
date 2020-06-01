from database.models import *

from werkzeug.utils import secure_filename
import psycopg2


class Database:
    def __init__(self, db_name="db.db"):
        self.__conn = psycopg2.connect(dbname='d2j8681f905ao',
                                     user='uoayucjbyhhbpw',
                                     password='09f4cadf9152d7bd48cfb5ee161ed0ecfa7e7531334e5e9d7ca598ac286aa3a6',
                                     host='ec2-54-217-236-206.eu-west-1.compute.amazonaws.com')
        self.__cursor = self.__conn.cursor()

        # import sqlite3
        # self.__conn = sqlite3.connect(db_name, check_same_thread=False)
        # self.__cursor = self.__conn.cursor()

        self.User = User(self.__cursor, self.__conn)

