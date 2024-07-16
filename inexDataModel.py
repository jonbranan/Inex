def dataTemplate(**kwargs):
    """Expects the following keyword arguments:
    status,status_detail,status_code,file_size,file_path,file_virtual_path,file_name,
    guid,ref_id,prd_instance_id,product_guid,product_name,product_version,node_name,
    src_endpoint_port,src_endpoint_ip,dst_endpoint_port,dst_endpoint_ip,dst_endpoint_type,
    session_uid,bytes_out,transfer_time,time,user_type,user_domain,user_name and utype.
    """
    template ={
    "status": kwargs.get('status'),
    "status_detail": kwargs.get('status_detail'),
	"status_code": kwargs.get('status_code'),
    "file": {
        "size": kwargs.get('file_size'),
        "path": kwargs.get('file_path'),
        "virtual_path": kwargs.get('file_virtual_path'),
        "name": kwargs.get('file_name')
    },
    "guid": kwargs.get('guid'),
    "ref_id": kwargs.get('ref_id'),
    "prd_instance_id": kwargs.get('prd_instance_id'),
    "product_guid": kwargs.get('product_guid'),
    "product_name": kwargs.get('product_name'),
    "product_version": kwargs.get('product_version'),
    "node_name":kwargs.get('node_name'),
    "src_endpoint": {
        "port": kwargs.get('src_endpoint_port'),
        "ip": kwargs.get('src_endpoint_ip')
    },
	"dst_endpoint": {
        "port": kwargs.get('dst_endpoint_port'),
        "ip": kwargs.get('dst_endpoint_ip'),
        "type": kwargs.get('dst_endpoint_type')
    },
    "session": {
        "uid": kwargs.get('session_uid') 
    },
	"bytes_out" : kwargs.get('bytes_out'),
	"transfer_time" : kwargs.get('transfer_time'),
    "time": kwargs.get('time'),
    "user": {
        "type": kwargs.get('user_type'),
        "domain": kwargs.get('user_domain'),
        "name": kwargs.get('user_name')
    },
    "utype": kwargs.get('utype')
    }

    return template