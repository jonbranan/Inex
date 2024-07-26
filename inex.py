import pyodbc
import os
import logging
import datetime
from tomllib import load
from inexLogging import inexLog
import inexConnect
from inexDataModel import dataTemplate
from inexDataProcessing import processData
import json
import decimal
import requests

class Inex:
    def __init__(self):
        """Initilize config, calls functions from inex-connect.py and inex-logging.py"""
        if os.path.exists('./config.toml'):
            config_file_path = './config.toml'
            with open(config_file_path, 'rb') as c:
                self.config = load(c)

        # assign libraries
        self.db = pyodbc
        self.tm = datetime
        self.il = logging
        self.ic = inexConnect
        self.r = requests

        # set config
        self.dbDriver = self.config["database"]["driver"]
        self.dbServer = self.config["database"]["server"]
        self.dbDatabase = self.config["database"]["database"]
        self.dbUser = self.config["database"]["user"]
        self.dbPassword = self.config["database"]["password"]
        self.dbQuery = self.config["database"]["query"]
        self.outputFile = self.config["output"]["filename"]
        self.useLog = self.config["logging"]["useLog"]
        self.logPath = self.config["logging"]["logPath"]
        self.logLevel = self.config["logging"]["logLevel"]
        self.prdInstanceID = self.config["immutables"]["prd_instance_id"]
        self.productGUID = self.config["immutables"]["product_guid"]
        self.productName = self.config["immutables"]["product_name"]
        self.productVersion = self.config["immutables"]["product_version"]
        
        #Setup logging
        inexLog(self)

        # create the connection to the database
        self.cursor = self.ic.connectDatabase(self, self.db, self.dbDriver, self.dbServer, self.dbDatabase, self.dbUser, self.dbPassword)

        self.data = self.ic.databaseQuery(self, self.cursor, self.dbQuery)

        self.modifiedData = processData(self.data, dataTemplate, prd_instance_id=self.prdInstanceID,\
                                         product_guid=self.productGUID,product_name=self.productName,product_version=self.productVersion)


        # TODO: move this to its own function
        if self.useLog:
            self.il.warning(f"Writing to '{self.outputFile}'.")

        with open(self.outputFile, "w") as f:
            json.dump(self.modifiedData, f, indent = 2, cls=Encoder)

# TODO: Move this class to it's own file
class Encoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            return int(o)
        if isinstance(o, datetime.datetime):
            return str(o)
        return super().default(o)

# Run
if  __name__== "__main__":
    Inex()