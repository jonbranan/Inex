# Inex

### Information Exchange - Ingest ARM data into EFC
This application is designed to pull data from an Microsoft SQL database, reformat it, and then send that data via the web to the Event Fusion Center. It's designed to be performant. The embedded query doesn't return unneccesary data and data is written to memory before being pushed into EFC. Initially you may have to pull a large amount of days so the system is caught up but the sweet spot would be to pull a set of data every day. 

## Build from source
You will need to install git and clone the repository:

`git clone https://git.jonb.io/jblu/Inex.git`

Alternitively you can download the files from [the releases page](https://git.jonb.io/jblu/Inex/releases).

Then follow OS specific instructions. These are taken directly from the steps used in automation to build the executables found in the releases page.
##### Windows

You can find the requirements.txt in the repository.

`python -m pip install -r requirements.txt`

`pyinstaller --noconfirm --onefile --console path/to/inex.py`

##### Linux
Update Linux Distro. This is Ubuntu specific. Please check the package management tool in your specific version.

`apt-get update`

You need unixodbc or else pyodbc cannot install.

`apt-get install unixodbc -y`

You can find the requirements.txt in the repository.

`pip install -r requirements.txt`

`pyinstaller --noconfirm --onefile --console path/to/inex.py`

## Setup
You will need a *config.toml* file in the same directory where *inex.py* or inex executable is. It's recommended to rename the existing config.toml.example file to save sometime and avoid omitting any data.

> If the application doesn't find the *config.toml* at the time of execution, it will not continue.

#### Config.toml
| Table | Purpose |
|-|-|
| fortraPlatform | Fortra Specific data |
| database | MSSQL Configuration |
| immutables | Data that must be included but is not provided by the source database |
| output | If and where to write files|
| logging | Set if, where and level of logging |

The following settings are not obvious as to how they affect the application.
```
[fortraPlatform]
selectedPlatform = "dev" # This will modify which environment the data is pushed to. The tenant_id and secret must be manually modified.

[database]
overrideEmbeddedquery = true # Choose if embedded query should be overridden.
driver = "ODBC Driver 18 for SQL Server" # Select which windows driver should be used. This one is recommended.

[output]
pushToplatform = false # if true, send data to fortraPlatform setting to false is useful in dry-runs.
dumpTojson = true # if true, write data to json file
token = "./.token" # Recommended to leave as-is

```

## Usage

### Windows
##### Run inex.py 
1. Download [source](https://git.jonb.io/jblu/Inex/releases)
2. `cd C:\path\to\Inex`
3. `python inex.py`

OR

##### Run inex.exe
1. Download [source](https://git.jonb.io/jblu/Inex/releases)
2. `cd C:\path\to\Inex.exe`
3. CMD `.\inex.exe`

### Linux
##### Run inex.py
1. Download [source](https://git.jonb.io/jblu/Inex/releases)
2. `cd /path/to/Inex`
3. `python ./inex.py`

OR
1. Download [source](https://git.jonb.io/jblu/Inex/releases)
2. `cd /path/to/Inex`
3. RUN `./inex`