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


def identifyUtype(obj):
    """Process Type of transaction based on string that passed in.
    Return transaction type."""
    user_logged_on = ['AUTH']
    file_deleted = ["dele"]
    file_uploaded = ["created"]
    file_downloaded = ["sent"]

    if obj in user_logged_on:
        return "user_logged_on"
    if obj in file_deleted:
        return "file_deleted"
    if obj in file_uploaded:
        return "file_uploaded"
    if obj in file_downloaded:
        return "file_downloaded"
    else:
        return "other"
    

testfolder = '/Usr/a/asdf/asf/asdfas/asdfasdf/'
user = 'a'

def parsehomefolder(user, virtualfolder):
    userSplit = f'/{user}/'
    home = virtualfolder.split(userSplit)[0] + userSplit
    print(home)
    return home

a = parsehomefolder(user, testfolder)