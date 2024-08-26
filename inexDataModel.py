def dataTemplate(transactionType,**kwargs):
    """Created templates for use. This function forms json data into an
    appropriate model for EFC. It returnes the appropriate template based
    on the transaction type passed into the function. The logic to process
    this is at the bottom of the function."""
    upload = {
        "bytes" : kwargs.get('bytes'),
        "dst_endpoint": { 
            "port": kwargs.get('dst_endpoint_port'),
            "ip": kwargs.get('dst_endpoint_ip'),
            "type": kwargs.get('dst_endpoint_type')
        },
        "duration": kwargs.get('duration'),
        "file": {
            "created_time": kwargs.get('file_created_time'),
            "uid": kwargs.get('file_uid'),
            "size": kwargs.get('file_size'),
            "name": kwargs.get('file_name'),
            "path": kwargs.get('file_path')
        },
        "guid": kwargs.get('file_uid'),
        "node_name": kwargs.get('node_name'),
        "prd_ext_tenant_id": kwargs.get('prd_ext_tenant_id'),
        "product_name": kwargs.get('product_name'),
        "prd_ext_tenant_name": kwargs.get('prd_ext_tenant_name'),
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
        "tenant": kwargs.get('prd_ext_tenant_id'),
        "tenant_name":"GlobalScape",
        "time": kwargs.get('time'),
        "status_code": kwargs.get('status_code'),
        "status_detail": kwargs.get('status_detail'),
        "user": {
            "home_directory": kwargs.get('user_home_directory'),
            "uuid": kwargs.get('guid'),
            "uid": kwargs.get('user_uid'),
            "type": kwargs.get('user_type'),
            "name": kwargs.get('user_name')
        },
        "utype": kwargs.get('utype')
    }
    download = {
        "bytes" : kwargs.get('bytes'),
        "dst_endpoint": { 
            "port": kwargs.get('dst_endpoint_port'),
            "ip": kwargs.get('dst_endpoint_ip'),
            "type": kwargs.get('dst_endpoint_type')
        },
        "duration": kwargs.get('duration'),
        "file": {
            "uid": kwargs.get('file_uid'),
            "size": kwargs.get('file_size'),
            "name": kwargs.get('file_name'),
            "path": kwargs.get('file_path')
        },
        "guid": kwargs.get('file_uid'),
        "node_name": kwargs.get('node_name'),
        "prd_ext_tenant_id": kwargs.get('prd_ext_tenant_id'),
        "product_name": kwargs.get('product_name'),
        "prd_ext_tenant_name": kwargs.get('prd_ext_tenant_name'),
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
        "tenant": kwargs.get('prd_ext_tenant_id'),
        "tenant_name":"GlobalScape",
        "time": kwargs.get('time'),
        "status_code": kwargs.get('status_code'),
        "status_detail": kwargs.get('status_detail'),
        "user": {
            "home_directory": kwargs.get('user_home_directory'),
            "uuid": kwargs.get('guid'),
            "uid": kwargs.get('user_uid'),
            "type": kwargs.get('user_type'),
            "name": kwargs.get('user_name')
        },
        "utype": kwargs.get('utype')
    }
   
    fileDeleted = {
        "file": {
                "size": kwargs.get('file_size'),
                "name": kwargs.get('file_name'),
                "path": kwargs.get('file_path'),
                "uid": kwargs.get('file_uid'),
        },
        "guid": f'deleted:{kwargs.get("guid")}',
        "node_name": kwargs.get('node_name'),
        "classifications": [{
            "ref_id": f"globalscape:{kwargs.get('guid')}",
            "time": kwargs.get('time'),
        }],
        "prd_ext_tenant_name": kwargs.get("prd_ext_tenant_name"),
        "prd_ext_tenant_id": kwargs.get('prd_ext_tenant_id'),
        "product_name": kwargs.get("product_name"),
        "session": {
            "created_time": kwargs.get('time'),
            "uid": kwargs.get('session_uid')
        },
        "src_endpoint": {
            "port": kwargs.get('src_endpoint_port'),
            "ip": kwargs.get('src_endpoint_ip'),
            "type": kwargs.get('src_endpoint_type')
        },
        "tenant": kwargs.get('prd_ext_tenant_id'),
        "tenant_name":"GlobalScape",
        "dst_endpoint": {
            "port": kwargs.get('dst_endpoint_port'),
            "ip": kwargs.get('dst_endpoint_ip'),
            "type": kwargs.get('dst_endpoint_type')
        },
        "time": kwargs.get('time'),
        "status_code": kwargs.get('status_code'),
        "status_detail": kwargs.get('status_detail'),
        "user": {
            "home_directory": kwargs.get('user_home_directory'),
            "uuid": kwargs.get('user_session_uid'),
            "uid": kwargs.get('user_uid'),
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
    "node_name": kwargs.get('node_name'),
    "tenant": kwargs.get('prd_ext_tenant_id'),
    "tenant_name":"GlobalScape",
    "prd_ext_tenant_id": kwargs.get('prd_ext_tenant_id'),
    "product_name": kwargs.get("product_name"),
    "prd_ext_tenant_name": kwargs.get('prd_ext_tenant_name'),
    "status_code": kwargs.get('status_code'),
    "status_detail": kwargs.get('status_detail'),
    "src_endpoint": {
        "port": kwargs.get('src_endpoint_port'),
        "ip": kwargs.get('src_endpoint_ip'),
        "type": kwargs.get('src_endpoint_type')
    },
    "time": kwargs.get('time'),
    "user": {
        "home_directory": kwargs.get('user_home_directory'),
        "uuid": kwargs.get('user_session_uid'),
        "uid": kwargs.get('user_uid'),
        "type": kwargs.get('user_type'),
        "name": kwargs.get('user_name')
    },
    "session": {
        "created_time": kwargs.get('time'),
        "uid": kwargs.get('session_uid')
    },
    "utype": kwargs.get('utype')
    }

    if transactionType == "file_uploaded":
        template = upload
    if transactionType == "file_downloaded":
        template = download
    if transactionType == "file_deleted":
        template = fileDeleted
    if transactionType == "user_logged_on":
        template = logon
    if transactionType == "other":
        template = {}
    
    return template