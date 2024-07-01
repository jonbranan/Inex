def connectDatabase(driver, server, database, user, password):
    connectionString = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes'
    print(connectionString)

a = connectDatabase("ODBC Driver 18 for SQL Server","b","c","d","e")