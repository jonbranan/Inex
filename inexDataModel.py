def dataTemplate(transactionType,**kwargs):
    uploadDownload = {
        "bytes" : kwargs.get('bytes_out'),
        "dst_endpoint": { 
            "port": kwargs.get('dst_endpoint_port'),
            "ip": kwargs.get('dst_endpoint_ip'),
            "type": kwargs.get('dst_endpoint_type')
        },
        "duration": kwargs.get('duration'),
        "file": {
            "created_time": kwargs.get('time'),
            "size": kwargs.get('file_size'),
            "name": kwargs.get('file_name'),
            "path": kwargs.get('file_path')
        },
        "guid": kwargs.get('guid'),
        "node_name": kwargs.get('node_name'),
        "prd_ext_tenant_id": kwargs.get('tenant'),
        "product_name": "GlobalScape EFT",
        "prd_ext_tenant_name": "GlobalScape EFT",
        "classifications": [{
            "ref_id": f"globalscape:{kwargs.get('guid')}",
            "time": kwargs.get('time'),
        }],
        "session": {
           "created_time": kwargs.get('time'),
           "uid": kwargs.get('session_uid')
        },
        "src_endpoint": {
            "port": kwargs.get('src_endpoint_port'),
            "ip": kwargs.get('src_endpoint_ip'),
            "type": kwargs.get('src_endpoint_type')
        },
        "tenant": kwargs.get('tenant'),
        "tenant_name":"GlobalScape",
        "time": kwargs.get('time'),
        "status_code": kwargs.get('status_code'),
        "status_detail": kwargs.get('description'),
        "user": {
            "home_directory": kwargs.get('user_home_directory'),
            "uuid": kwargs.get('guid'),
            "uid": kwargs.get('uid'),
            "type": kwargs.get('user_type'),
            "name": kwargs.get('user_name')
        },
        "utype": kwargs.get('utype')
    }
   
    fileDeleted = {
        "file": {
                "size": kwargs.get('file_size'),
                "name": kwargs.get('file_name'),
                "path": kwargs.get('file_path')
        },
        "guid": kwargs.get('guid'),
        "classifications": [{
            "ref_id": f"globalscape:{kwargs.get('guid')}",
            "time": kwargs.get('time'),
        }],
        "prd_ext_tenant_name": "Globalscape EFT",
        "prd_ext_tenant_id": kwargs.get('tenant'),
        "product_name": "Globalscape EFT",
        "session": {
            "created_time": kwargs.get('time'),
            "uid": kwargs.get('session_uid')
        },
        "src_endpoint": {
            "port": kwargs.get('src_endpoint_port'),
            "ip": kwargs.get('src_endpoint_ip'),
            "type": kwargs.get('src_endpoint_type')
        },
        "dst_endpoint": {
            "port": kwargs.get('dst_endpoint_port'),
            "ip": kwargs.get('dst_endpoint_ip'),
            "type": kwargs.get('dst_endpoint_type')
        },
        "time": kwargs.get('time'),
        "user": {
            "home_directory": kwargs.get('user_home_directory'),
            "uuid": kwargs.get('guid'),
            "uid": kwargs.get('uid'),
            "type": kwargs.get('user_type'),
            "name": kwargs.get('user_name')
        },
        "utype": kwargs.get('utype')
    }
    
    logon ={
    "classifications": [{
        "ref_id": f"globalscape:{kwargs.get('guid')}",
        "time": kwargs.get('time'),
    }],
    "dst_endpoint": {
        "port": kwargs.get('dst_endpoint_port'),
        "ip": kwargs.get('dst_endpoint_ip'),
        "type": kwargs.get('dst_endpoint_type')
    },
    "guid": kwargs.get('guid'),
    "prd_ext_tenant_id": kwargs.get('tenant'),
    "product_name": "GlobalScape EFT",
    "prd_ext_tenant_name": "GlobalScape EFT",
    "src_endpoint": {
        "port": kwargs.get('src_endpoint_port'),
        "ip": kwargs.get('src_endpoint_ip'),
        "type": kwargs.get('src_endpoint_type')
    },
    "time": kwargs.get('time'),
    "user": {
        "home_directory": kwargs.get('user_home_directory'),
        "uuid": kwargs.get('guid'),
        "uid": kwargs.get('uid'),
        "type": kwargs.get('user_type'),
        "name": kwargs.get('user_name')
    },
    "utype": kwargs.get('utype')
    }

    if transactionType == "file_uploaded":
        template = uploadDownload
    if transactionType == "file_downloaded":
        template = uploadDownload
    if transactionType == "file_deleted":
        template = fileDeleted
    if transactionType == "user_logged_on":
        template = logon
    
    return template