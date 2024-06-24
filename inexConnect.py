def connectDatabase(lib, driver, server, database, user, password):
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes'
    print(connectionString)
    connection = lib.connect(connectionString)
    cursor = connection.cursor()
    return  cursor

def databaseQuery(cursor, query, args=(), one=False):
    cur = cursor.execute(query, args)
    r = [dict((cur.description[i][0], value) \
               for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if one else r