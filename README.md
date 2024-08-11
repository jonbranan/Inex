# Inex

##### Information Exchange - Ingest ARM data into EFC
This application is designed to pull data from an Microsoft SQL database, reformat it, and then send that data via the web to the Event Fusion Center. It's designed to be performant. The embedded query doesn't return unneccesary data and data is written to memory before being pushed into EFC. Initially you may have to pull a large amount of days so the system is caught up but the sweet spot would be to pull a set of data every day. 

# Build from source
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

# Setup

#### Config.toml
| Table | Purpose |
|-|-|
| fortraPlatform | Fortra Specific data |
| database | MSSQL Configuration |
| immutables | Data that must be included but is not provided by the source database |
| output | If and where to write files|
| logging | Set If, where and level of logging |


fortraPlatform
: Fortra Specific data.

database
: MSSQL Configuration.

immutables
: Data that must be included but is not provided by the source database

output
: If and where to write files.

logging
: Set If, where and level of logging.

##### Usage

