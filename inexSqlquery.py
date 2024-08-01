class sqlQuerymodel:
    def queryData():
        """Embedded query data"""
        q ="""DECLARE @stopTime DATETIME2
        SET @stopTime=DATEADD(DAY, -30, GETDATE())
        SELECT p.ProtocolCommandID, t.Time_stamp, p.RemoteIP, p.RemotePort, p.LocalIP, p.LocalPort, p.Protocol, p.SiteName, p.Command, p.CommandParameters, p.FileName, p.VirtualFolderName, p.PhysicalFolderName, p.IsInternal, p.FileSize, p.TransferTime, p.BytesTransferred, p.ResultID, t.TransactionID, p.Description, p.Actor, t.ParentTransactionID, t.TransactionObject, t.NodeName, t.TransactionGUID, a.Protocol user_type
        FROM tbl_Transactions t
             Full JOIN tbl_ProtocolCommands p ON(t.TransactionID=p.TransactionID)
             Full join tbl_Authentications a ON(t.TransactionID=a.TransactionID)
        WHERE p.Time_stamp>@stopTime"""
        return q