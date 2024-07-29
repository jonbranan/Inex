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
        if self.os.path.exists(self.tokenFilepath):
            with open(self.tokenFilepath, 'rb') as t:
                self.token = self.j.load(t)
                print(self.token["access_token"])

    def saveToken(self):
        with open(self.tokenFilepath, "w") as f:
             self.j.dump(self.tokenData, f, indent = 2)

    def getToken(self):
        self.tokenData = self.r.post(self.platformConfig["idp"], headers={"client_id": self.platformConfig["client_id"],"client_secret": self.platformConfig["secret"]})
        
    def pushPayload(self):
        url = f'{self.host}/api/v1/unity/data/{self.tenant_id}/machine_event'
        pushPayloadResponse = self.r.post(self.platformConfig["efc_url"], headers={'Authorization': f'bearer {self.token["access_token"]}'},\
                                           payload=self.modifiedData)
        return pushPayloadResponse.status_code