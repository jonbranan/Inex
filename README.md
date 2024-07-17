# Inex

Information Exchange - Pull data from EFT ARM then dump it to a json file

# Data Map:
## tbl_ProtocolCommands
- ProtocolCommandID
- Time_stamp
- RemoteIP
- RemotePort
- LocalIP
- LocalPort
- Protocol
- SiteName
- Command
- CommandParameters
- FileName
- VirtualFolderName
- PhysicalFolderName
- IsInternal
- FileSize
- TransferTime
- BytesTransferred
- ResultID
- TransactionID
- Description
- Actor
## tbl_Transactions
- TransactionID
- ParentTransactionID
- TransactionObject
- TransactionGUID
- NodeName
- time_stamp