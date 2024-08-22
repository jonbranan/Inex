class inexSql:
    def connectDatabase(self, lib, driver, server, database, user, password):
        """Connects to the database. Requires a windows driver to do so.
        Typically there is one installed by default"""

        connectionString = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes'
        if self.useLog:
            self.il.debug(f"Connection String: connectionString")
            self.il.info(f"Connecting to {database}@{server} with driver[{driver}].")
        try:
            connection = lib.connect(connectionString)
        except lib.Error as ex:
            sqlstate = ex.args[1]
            if self.useLog:
                self.il.error(sqlstate)
        if self.useLog:
            self.il.debug(f"Connected.")
        cursor = connection.cursor()

        return  cursor

    def databaseQuery(self, cursor, query, args=()):
        if self.useLog:
            self.il.debug(f"Query:")
            self.il.debug(query)
            self.il.info(f"Sending query:{query[0:20]}...")

        try:
            cur = cursor.execute(query, args)
        except cur.Error as ex:
            sqlstate = ex.args[1]
            if self.useLog:
                self.il.error(sqlstate)

        if self.useLog:
            self.il.debug(f"Processing database response...")
        r = [dict((cur.description[i][0], value) \
                   for i, value in enumerate(row)) for row in cur.fetchall()]

        cur.connection.close()
        if self.useLog:
            self.il.debug(f"Database connection closed")
        return r

class fortraEFC:
    def __init__(self):
        # Check if .token file is present
        if fortraEFC.readToken(self) == 1:
            # Get fresh token. First run.
            fortraEFC.getToken(self)
            fortraEFC.writeToken(self)
        # Push data with token
        self.pushPayloadresponse = fortraEFC.pushPayload(self)
        if self.pushPayloadresponse == 401:
            fortraEFC.getToken(self)
            fortraEFC.writeToken(self)
            fortraEFC.pushPayload(self)

    def readToken(self):
        if self.os.path.exists(self.tokenFilepath):
            with open(self.tokenFilepath, 'rb') as t:
                self.tokenData = self.j.load(t)
                self.il.debug(f'readToken {self.tokenData["access_token"]}')
            return 0
        else:
            return 1
    
    def getToken(self):
        self.tokenData = self.r.post(self.platformConfig["idp"], data={"grant_type":"client_credentials",\
                                                                              "client_id": self.platformConfig["client_id"],\
                                                                              "client_secret": self.platformConfig["secret"],})
        self.tokenData = self.tokenData.json()
        self.il.debug(f'getToken {self.tokenData["access_token"]}')

    def writeToken(self):
        fortraEFC.getToken(self)
        with open(self.tokenFilepath, "w") as f:
            self.j.dump(self.tokenData, f, indent = 2)
            self.il.debug(f'writeToken {self.tokenData["access_token"]}')

    def pushPayload(self):
        self.il.debug(f'pushPayload {self.tokenData["access_token"]}')
        url = f'{self.platformConfig["efc_url"]}/api/v1/unity/data/{self.platformConfig["tenant_id"]}/machine_event'
        pushPayloadResponse = self.r.post(url, headers={'Authorization': f'Bearer {self.tokenData["access_token"]}'},\
                                           data=self.j.dumps(self.modifiedData, cls=self.e))
        self.il.debug(pushPayloadResponse.status_code)
        self.il.debug(pushPayloadResponse.text)
        return pushPayloadResponse.status_code