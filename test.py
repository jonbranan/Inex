import datetime

def connectDatabase(driver, server, database, user, password):
    connectionString = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes'
    print(connectionString)

# a = connectDatabase("ODBC Driver 18 for SQL Server","b","c","d","e")

def converttimestamp(t):
    print(int(t.timestamp()* 1000))

a = converttimestamp(datetime.datetime(2024, 7, 23, 14, 26, 38, 214000))