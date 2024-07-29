import pyodbc
import os
import logging
import datetime
import tomllib
from inexLogging import inexLog
import inexConnect
from inexDataModel import dataTemplate
from inexDataProcessing import processData
import json
import decimal
import requests
import inexEncoder

class Inex:
    def __init__(self):
        """Initilize config, calls functions from inex-connect.py and inex-logging.py"""
        # assign libraries
        self.db = pyodbc
        self.tm = datetime
        self.il = logging
        self.ic = inexConnect
        self.r = requests
        self.tl = tomllib
        self.os = os
        self.j = json
        self.e = inexEncoder.Encoder

        if self.os.path.exists('./config.toml'):
            config_file_path = './config.toml'
            with open(config_file_path, 'rb') as c:
                self.config = self.tl.load(c)
        
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
        self.tokenFilepath = self.config["output"]["token"]
        self.selectedPlatform = self.config["fortraPlatform"]["selectedPlatform"]
        self.writeJsonfile = self.config["output"]["dumpTojson"]
        self.pushToplatform = self.config["output"]["pushToplatform"]

        if "dev" in self.selectedPlatform.lower():
            self.platformConfig = self.config["fortraPlatform"]["dev"]
        if "stag" in self.selectedPlatform.lower():
            self.platformConfig = self.config["fortraPlatform"]["stage"]
        if "prod" in self.selectedPlatform.lower():
            self.platformConfig = self.config["fortraPlatform"]["prod"]
        # print(self.platformConfig)

        #Setup logging
        inexLog(self)

        # create the connection to the database
        self.cursor = self.ic.connectDatabase(self, self.db, self.dbDriver, self.dbServer, self.dbDatabase, self.dbUser, self.dbPassword)

        self.data = self.ic.databaseQuery(self, self.cursor, self.dbQuery)

        self.modifiedData = processData(self.data, dataTemplate, prd_instance_id=self.prdInstanceID,\
                                         product_guid=self.productGUID,product_name=self.productName,product_version=self.productVersion)
        
        if self.pushToplatform:
            inexConnect.fortraEFC.pushPayload(self)

        # TODO: move this to its own function
        if self.useLog:
            self.il.warning(f"Writing to '{self.outputFile}'.")
        if self.writeJsonfile:
            with open(self.outputFile, "w") as f:
                self.j.dump(self.modifiedData, f, indent = 2, cls=self.e)

# Run
if  __name__== "__main__":
    Inex()