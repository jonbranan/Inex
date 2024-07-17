def processData(data, template):
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
                            prd_instance_id=row.get(''),\
                            product_guid=row.get(''),\
                            product_name=row.get(''),\
                            product_version=row.get(''),\
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
                            user_type=row.get(''),\
                            user_domain=row.get('SiteName'),\
                            user_name=row.get('Actor'),\
                            utype=row.get('Command')))
    return processedData