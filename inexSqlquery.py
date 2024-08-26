class sqlQuerymodel:
    def queryData(overRideflag, configQuery, daysTopull):
        """Embedded query data. Data is slightly modified to change the amount of days to pull."""
        q ="""DECLARE @stopTime DATETIME2
        SET @stopTime=DATEADD(DAY, -30, GETDATE())
        SELECT p.ProtocolCommandID, t.Time_stamp, p.RemoteIP, p.RemotePort, p.LocalIP, p.LocalPort, p.Protocol, p.SiteName, p.Command, p.FileName, p.PhysicalFolderName, p.VirtualFolderName, p.FileSize, p.TransferTime, p.BytesTransferred, p.Description, p.ResultID, t.TransactionID, p.Actor, t.TransactionObject, t.NodeName, t.TransactionGUID, a.Protocol user_type
        FROM tbl_Transactions t
             Full JOIN tbl_ProtocolCommands p ON(t.TransactionID=p.TransactionID)
             Full join tbl_Authentications a ON(t.TransactionID=a.TransactionID)
        WHERE p.Time_stamp>@stopTime AND p.Command IS NOT NULL""".replace("30", str(daysTopull))
        return configQuery if overRideflag else q