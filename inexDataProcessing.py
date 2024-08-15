def processData(data, template, **kwargs):
    """Translates data from sql query to the appropriate place in the respective template.
    Accepts data, which is the sql query output, the template function, and finally
    additional data to insert into the template."""
    processedData = []
    transactionLoginid = []

    for row in data:
        # print(f'Row: {row}')
        if identifyUtype(row.get('Command')) == "other":
            continue
        
        if row.get('Command') == None:
            continue
        try:
            processedData.append(template(identifyUtype(row.get('Command')),\
                prd_ext_tenant_id='',\
                status_code=row.get('ResultID'),\
                file_size=row.get('FileSize'),\
                file_path=row.get('PhysicalFolderName'),\
                file_virtual_path=row.get('VirtualFolderName'),\
                file_name=row.get('FileName'),\
                guid=row.get('TransactionGUID'),\
                ref_id=row.get('ProtocolCommandID'),\
                prd_instance_id=kwargs.get('prd_instance_id'),\
                product_guid=kwargs.get('product_guid'),\
                product_name=kwargs.get('product_name'),\
                product_version=kwargs.get('product_version'),\
                node_name=row.get('NodeName'),\
                src_endpoint_type=row.get('Protocol'),\
                src_endpoint_port=row.get('RemotePort'),\
                src_endpoint_ip=row.get('RemoteIP'),\
                dst_endpoint_port=row.get('LocalPort'),\
                dst_endpoint_ip=row.get('LocalIP'),\
                dst_endpoint_type=row.get('Protocol'),\
                session_uid=row.get('TransactionID'),\
                bytes_out=row.get('BytesTransferred'),\
                duration=row.get('TransferTime'),\
                time=row.get('Time_stamp'),\
                user_type=identifyUserType(row.get('user_type')),\
                user_domain=row.get('SiteName'),\
                user_name=row.get('Actor'),\
                user_home_directory=row.get('VirtualFolderName'),\
                description=row.get('Description'),\
                utype=identifyUtype(row.get('Command'))))
        except UnboundLocalError:
            print(f'Problem row GUID:{row.get("TransactionGUID")} ::: TransactionObject:{row.get("TransactionObject")} Command: {row.get("Command")}')

            continue

        if row.get('TransactionGUID') not in transactionLoginid:
            try:
                processedData.append(template(identifyUtype(row.get('TransactionObject')),\
                    guid=row.get('TransactionGUID'),\
                    prd_instance_id=kwargs.get('prd_instance_id'),\
                    product_guid=kwargs.get('product_guid'),\
                    product_name=kwargs.get('product_name'),\
                    product_version=kwargs.get('product_version'),\
                    src_endpoint_type=row.get('Protocol'),\
                    src_endpoint_port=row.get('RemotePort'),\
                    src_endpoint_ip=row.get('RemoteIP'),\
                    dst_endpoint_port=row.get('LocalPort'),\
                    dst_endpoint_ip=row.get('LocalIP'),\
                    dst_endpoint_type=row.get('Protocol'),\
                    session_uid=row.get('TransactionID'),\
                    bytes_out=row.get('BytesTransferred'),\
                    transfer_time=row.get('TransferTime'),\
                    time=row.get('Time_stamp'),\
                    user_type=identifyUserType(row.get('user_type')),\
                    user_domain=row.get('SiteName'),\
                    user_name=row.get('Actor'),\
                    user_home_directory=row.get('VirtualFolderName'),\
                    utype=identifyUtype(row.get('TransactionObject'))\
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