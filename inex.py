import pandas
import pyodbc
import os
from datetime import datetime
from tomllib import load
import inexLogging
import inexConnect
from json import dump,dumps

class Inex:
    def __init__(self):
        """Initilize config, calls functions from inex-connect.py and inex-logging.py"""
        if os.path.exists('./config.toml'):
            config_file_path = './config.toml'
            with open(config_file_path, 'rb') as c:
                self.config = load(c)

        # assign libraries
        self.pd = pandas
        self.db = pyodbc
        self.tm = datetime
        self.il = inexLogging
        self.ic = inexConnect

        # set config
        self.dbDriver = self.config["database"]["driver"]
        self.dbServer = self.config["database"]["server"]
        self.dbDatabase = self.config["database"]["database"]
        self.dbUser = self.config["database"]["user"]
        self.dbPassword = self.config["database"]["password"]
        self.dbQuery = self.config["database"]["query"]
        self.outputFile = self.config["output"]["filename"]

        # create the connection to the database
        self.cursor = self.ic.connectDatabase(self.db, self.dbDriver, self.dbServer, self.dbDatabase, self.dbUser, self.dbPassword)

        self.data = self.ic.databaseQuery(self.cursor, self.dbQuery)
        
        # self.jsonData = dumps(self.data)
        # print(self.jsonData)

        with open(self.outputFile, "w") as f:
            dump(self.data, f)


# Run
if  __name__== "__main__":
    Inex()