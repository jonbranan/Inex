import pyodbc
import os
import logging
import tomllib
from inexLogging import inexLog
import inexConnect
from inexDataModel import dataTemplate
from inexDataProcessing import processData
import json
import requests
import inexEncoder
import inexSqlquery

class Inex:
    def __init__(self):
        """Initilize config, calls functions from inexConnect.py, inexLogging.py 
        inexDataModel.py, inexDataProcessing.py, inexEncoder.py and inexSqlquery.py
        Main logic of the program. Requires a config.toml in the same directory it's
        being run from."""
        # assign libraries
        self.db = pyodbc
        self.il = logging
        self.ic = inexConnect
        self.r = requests
        self.tl = tomllib
        self.os = os
        self.j = json
        self.e = inexEncoder.Encoder
        self.sq = inexSqlquery

        # Check if local config file exists.
        if self.os.path.exists('./config.toml'):
            config_file_path = './config.toml'
            with open(config_file_path, 'rb') as c:
                self.config = self.tl.load(c)
        
        # set config
        try:
            if self.config:
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
                self.prdExttenantname = self.config["immutables"]["prd_ext_tenant_name"]
                self.productName = self.config["immutables"]["product_name"]
                self.tokenFilepath = self.config["output"]["token"]
                self.selectedPlatform = self.config["fortraPlatform"]["selectedPlatform"]
                self.writeJsonfile = self.config["output"]["dumpTojson"]
                self.pushToplatform = self.config["output"]["pushToplatform"]
                self.queryOverride = self.config["database"]["overrideEmbeddedquery"]
                self.queryDaystopull = self.config["database"]["daysTopull"]
        except Exception as e:
            print("No config.toml or possibly missing settings in the file. Please use config.toml.example file and configure appropriately")
            self.il.error(e)
            print(e)

            exit(1)

        if "dev" in self.selectedPlatform.lower():
            self.platformConfig = self.config["fortraPlatform"]["dev"]
        if "stag" in self.selectedPlatform.lower():
            self.platformConfig = self.config["fortraPlatform"]["stage"]
        if "prod" in self.selectedPlatform.lower():
            self.platformConfig = self.config["fortraPlatform"]["prod"]

        #Setup logging
        inexLog(self)

        # create the connection to the database
        self.cursor = self.ic.inexSql.connectDatabase(self, self.db, self.dbDriver, self.dbServer, self.dbDatabase, self.dbUser, self.dbPassword)

        # Query the database
        self.data = self.ic.inexSql.databaseQuery(self, self.cursor, self.sq.sqlQuerymodel.queryData(self.queryOverride,self.dbQuery, self.queryDaystopull))

        # Modify the data to meet EFC requirements
        self.modifiedData = processData(self.data, dataTemplate, prd_ext_tenant_name=self.prdExttenantname,product_name=self.productName,\
                                        prd_ext_tenant_id=self.platformConfig["tenant_id"])

        # Push data to EFC. Check for local Auth token -> Authenticate if needed -> push data
        if self.pushToplatform:
            inexConnect.fortraEFC.__init__(self)

        if self.useLog:
            self.il.warning(f"Writing to '{self.outputFile}'.")
        # Write data to json
        if self.writeJsonfile:
            with open(self.outputFile, "w") as f:
                self.j.dump(self.modifiedData, f, indent = 2, cls=self.e)

# Run
if  __name__== "__main__":
    Inex()