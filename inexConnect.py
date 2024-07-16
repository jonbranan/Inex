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
    # return (r[0] if r else None) if one else r
    return r