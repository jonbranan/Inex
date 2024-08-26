def processData(data, template, **kwargs):
    """Translates data from sql query to the appropriate place in the respective template.
    Accepts data, which is the sql query output, the template function, and finally
    additional data to insert into the template. Uses other functions to further 
    process row data."""
    processedData = []
    transactionLoginid = []
    
    for row in data:
        # print(f'Row: {row}')
        # must set variables for the different templates and do logic based on that. Do not call identifyUtype many times
        identifyUtypecommand = identifyUtype(row.get('Command'))

        if identifyUtypecommand == "other":
            continue

        if row.get('Command') == None:
            continue

        userType = identifyUserType(row.get('user_type'))
        userHome = parseHomefolder(row.get('Actor'),row.get('VirtualFolderName'))
        try:
            processedData.append(template(identifyUtypecommand,\
                prd_ext_tenant_name=kwargs.get('prd_ext_tenant_name'),\
                user_uid=row.get('TransactionID'),\
                status_detail=row.get('Description'),\
                prd_ext_tenant_id=kwargs.get('prd_ext_tenant_id'),\
                status_code=row.get('ResultID'),\
                file_created_time=row.get('Time_stamp'),\
                file_size=row.get('FileSize'),\
                file_uid=row.get('ProtocolCommandID'),\
                file_path=row.get('PhysicalFolderName'),\
                file_name=row.get('FileName'),\
                guid=row.get('TransactionGUID'),\
                product_name=kwargs.get('product_name'),\
                node_name=row.get('NodeName'),\
                session_uid=row.get('TransactionID'),\
                src_endpoint_type=row.get('Protocol'),\
                src_endpoint_port=row.get('RemotePort'),\
                src_endpoint_ip=row.get('RemoteIP'),\
                dst_endpoint_port=row.get('LocalPort'),\
                dst_endpoint_ip=row.get('LocalIP'),\
                dst_endpoint_type=row.get('Protocol'),\
                user_session_uid=row.get('TransactionID'),\
                bytes=row.get('BytesTransferred'),\
                time=row.get('Time_stamp'),\
                duration=row.get('TransferTime'),\
                user_type=userType,\
                user_name=row.get('Actor'),\
                user_home_directory=userHome,\
                utype=identifyUtypecommand))
        except UnboundLocalError:
            print(f'Problem row GUID:{row.get("TransactionGUID")} ::: TransactionObject:{row.get("TransactionObject")} Command: {row.get("Command")}')
            continue

        identifyUtypetransactionObject = identifyUtype(row.get('TransactionObject'))

        if identifyUtypetransactionObject == "other":
            continue

        if row.get('TransactionGUID') not in transactionLoginid:
            try:
                processedData.append(template(identifyUtypetransactionObject,\
                    prd_ext_tenant_id=kwargs.get('prd_ext_tenant_id'),\
                    prd_ext_tenant_name=kwargs.get('prd_ext_tenant_name'),\
                    status_detail=row.get('Description'),\
                    guid=row.get('TransactionGUID'),\
                    status_code=row.get('ResultID'),\
                    node_name=row.get('NodeName'),\
                    prd_instance_id=kwargs.get('prd_instance_id'),\
                    product_name=kwargs.get('product_name'),\
                    src_endpoint_type=row.get('Protocol'),\
                    src_endpoint_port=row.get('RemotePort'),\
                    src_endpoint_ip=row.get('RemoteIP'),\
                    dst_endpoint_port=row.get('LocalPort'),\
                    dst_endpoint_ip=row.get('LocalIP'),\
                    dst_endpoint_type=row.get('Protocol'),\
                    session_uid=row.get('TransactionID'),\
                    transfer_time=row.get('TransferTime'),\
                    time=row.get('Time_stamp'),\
                    user_session_uid=row.get('TransactionID'),\
                    user_uid=row.get('TransactionID'),\
                    user_type=userType,\
                    user_name=row.get('Actor'),\
                    user_home_directory=userHome,\
                    utype=identifyUtypetransactionObject\
                    ))
                transactionLoginid.append(row.get('TransactionGUID'))
            except UnboundLocalError:
                print(f'Problem row GUID:{row.get("TransactionGUID")} ::: TransactionObject:{row.get("TransactionObject")} Command: {row.get("Command")}')
                continue

    return processedData

def identifyUserType(obj):
    """Check string if it has Admin-> return Administrator else return User."""
    if obj:
        if "Admin" in obj:
            return "Administrator"
        else:
            return "User"
    else:
        return None

def parseHomefolder(user, virtualfolder):
    """Extract users home folder using the username. Will not work on edge cases
    such as when a users home folder does not have the user name. When that occurs
    it is impossible to know based on the arm data what the home folder is.
    This function is an assumption so it may return the incorrect home folder. 
    This function finds the user name and takes the path from the left of the folder
    as the home folder. There are cases where this may not be accurate."""
    if user:
        userSplit = f'/{user}/'
    if virtualfolder:
        if userSplit in virtualfolder:
            home = virtualfolder.split(userSplit)[0] + userSplit
            return home if home else None

def identifyUtype(obj):
    """Process Type of transaction based on string that passed in.
    Return transaction type."""
    user_logged_on = ['AUTH']
    file_deleted = ["dele"]
    file_uploaded = ["created"]
    file_downloaded = ["sent"]

    if obj in user_logged_on:
        return "user_logged_on"
    elif obj in file_deleted:
        return "file_deleted"
    elif obj in file_uploaded:
        return "file_uploaded"
    elif obj in file_downloaded:
        return "file_downloaded"
    else:
        return "other"