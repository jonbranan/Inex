def processData(data, template, **kwargs):
    processedData = []
    for row in data:
        # print(f'Row: {row}')
        processedData.append(template(status=row.get(''),\
                            status_detail=row.get(''),\
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
                            utype=row.get('TransactionObject')))
    return processedData

def identifyUserType(obj):
    if obj:
        if "Admin" in obj:
            return "Administrator"
        else:
            return "User"
    else:
        return None