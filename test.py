import datetime

def connectDatabase(driver, server, database, user, password):
    connectionString = f'DRIVER={{{driver}}};SERVER={server};DATABASE={database};UID={user};PWD={password};TrustServerCertificate=yes'
    print(connectionString)

# a = connectDatabase("ODBC Driver 18 for SQL Server","b","c","d","e")

def converttimestamp(t):
    print(int(t.timestamp()* 1000))

def builddict(keys,*args,**kwargs):
    dict = {}
    for key in keys:
        dict[key] = kwargs.get(key)
    print(dict)

testfolder = '/Usr/a/asdf/asf'
user = 'a'

print(testfolder.split(f"/{user}/"))