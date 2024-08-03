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

FileUploaded = {
    "bytes" : 2490,
    "dst_endpoint": { 
        "port": 22,
        "ip": "10.91.160.77",
        "type": "SFTP"
    },
    "duration": 200,
    "file": {
        "created_time": 1722485724000,
        "size": 2490,
        "name": "Case9.vbs",
        "path": "\\\\10.255.255.9\\shared\\HASite\\InetPub\\EFTRoot\\MySite\\Usr\\Ivan //<PhysicalFolderName>"
    },
    "guid": "48D9C7A3-2DC6-11EF-AA59-00155D641204",
    "node_name":"PERF01-S2019-77",
    "prd_ext_tenant_id": "e71851c2-593f-4f49-9c07-91727b1be94b",
    "product_name": "GlobalScape EFT",
    "prd_ext_tenant_name": "GlobalScape EFT",
    "classifications": [{
        "ref_id": "globalscape:48D9C7A3-2DC6-11EF-AA59-00155D641204",
        "time":1722485724000,
    }],
    "session": {
       "created_time":1722485724000,
       "uid": "3615136"
    },
    "src_endpoint": {
        "port": 58868,
        "ip": "10.91.160.45",
        "type":"SFTP"
    },
    "tenant": "e71851c2-593f-4f49-9c07-91727b1be94b",
    "tenant_name":"GlobalScape",
    "time":1722485724000,
    "status_code":226,
    "status_detail":"Upload Successful",
    "user": {
        "home_directory": "/Usr/Ivan/",
        "uuid":"48D9C7A3-2DC6-11EF-AA59-00155D641204",
        "uid": "3978403",
        "type": "User",
        "name": "Ivan"
    },
    "utype": "file_uploaded"
}

FileDownloaded = {
"bytes" : 4891,
"dst_endpoint": {
    "port": 443,
    "ip": "10.91.160.77",
    "type": "HTTPS"
},
"duration": 200,
"file": {
    "created_time": 1722518124000,
    "size": 4891,
    "name": "FileDownload1.exe",
    "path": "\\\\10.255.255.9\\shared\\HASite\\InetPub\\EFTRoot\\MySite\\Usr\\Ivan //<PhysicalFolderName>"
},
"guid": "48D9C7A3-2DC6-11EF-AA59-00155D641205",
"node_name":"PERF01-S2019-77",
"prd_ext_tenant_id": "e71851c2-593f-4f49-9c07-91727b1be94b",
"product_name": "GlobalScape EFT",
"prd_ext_tenant_name": "GlobalScape EFT",
"classifications": [{
    "ref_id": "globalscape:48D9C7A3-2DC6-11EF-AA59-00155D641205",
    "time":1722518124000,
}],
"session": {
   "created_time":1722518124000,
   "uid": "3615137"
},
"src_endpoint": {
    "port": 443,
    "ip": "10.91.160.45",
    "type":"HTTPS"
},
"tenant": "e71851c2-593f-4f49-9c07-91727b1be94b",
"tenant_name":"GlobalScape",
"time":1722518124000,
"status_code":226,
"status_detail":"Download Successful",
"user": {
    "home_directory": "/Usr/Ivan/",
    "uuid":"48D9C7A3-2DC6-11EF-AA59-00155D641205",
    "uid": "3978404",
    "type": "User",
    "name": "Ivan" 
},
"utype": "file_downloaded"}

FileDeleted = {
        "file": {
        "size": 304673,
        "path": "\\\\10.255.255.9\\shared\\HASite\\InetPub\\EFTRoot\\MySite\\Usr\\Ivan",
"name": "DeleteME.txt"
},
"guid": "48D9C7A3-2DC6-11EF-AA59-00155D641207",
"classifications": [{
    "ref_id": "globalscape:48D9C7A3-2DC6-11EF-AA59-00155D641207",
    "time":1722515664000,
}],
"prd_ext_tenant_name": "Globalscape EFT",
"prd_ext_tenant_id": "e71851c2-593f-4f49-9c07-91727b1be94b",
"product_name": "Globalscape EFT",
"session": {
   "created_time":1722515664000,
   "uid": "3615138"
},
"src_endpoint": {
    "port": 443,
    "ip": "10.91.160.45",
    "type":"HTTPS"
},
"dst_endpoint": {
    "port": 443,
    "ip": "10.91.160.77",
    "type": "HTTPS"
},
"time": 1722515664000,
"user": {
    "home_directory": "/Usr/Ivan/",
    "uuid":"48D9C7A3-2DC6-11EF-AA59-00155D641207",
    "uid": "3978406",
    "type": "User",
    "name": "Ivan"
},
"utype": "file_deleted"
}

Logon ={
"classifications": [{
    "ref_id": "globalscape:48D9C7A3-2DC6-11EF-AA59-00155D641206",
    "time": 1722510924000,
    
}],
"dst_endpoint": {
    "port": 443,
    "ip": "10.91.160.77",
    "type": "HTTPS"
},
"guid": "48D9C7A3-2DC6-11EF-AA59-00155D641206",
"prd_ext_tenant_id": "e71851c2-593f-4f49-9c07-91727b1be94b",
"product_name": "GlobalScape EFT",
"prd_ext_tenant_name": "GlobalScape EFT",
"src_endpoint": {
    "port": 443,
    "ip": "10.91.160.45",
    "type":"HTTPS"
},
"time": 1722510924000,
"user": {
    "home_directory": "/Usr/Ivan/",
    "uuid":"48D9C7A3-2DC6-11EF-AA59-00155D641206",
    "uid": "3978405",
    "type": "User",
    "name": "Ivan"
},
"utype": "user_logged_on"
}