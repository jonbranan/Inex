def connectDatabase(lib, driver, server, database, user, password):
    connectionString = f'DRIVER={{ODBC Driver 18 for SQL Server}};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes'
    print(connectionString)
    connection = lib.connect(connectionString)
    # connection = lib.connect(f'DRIVER={{driver}};SERVER={server};DATABASE={database}')
    cursor = connection.cursor()
    return  cursor

def databaseQuery(cursor, query):
    cursor.execute(query)