import urllib3
import json
import api_info

#
# ThreatFox
#
def get_threatfox_data(ioc_type: str) -> list[str]:
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    pool = urllib3.HTTPSConnectionPool(
        'threatfox-api.abuse.ch',
        port=443,
        maxsize=50,
        cert_reqs='CERT_NONE',
        assert_hostname=True
    )
    
    response = pool.request(
        "POST",
        "/api/v1/",
        body=json.dumps(api_info.threatfox_data)
    )
    
    response_data = json.loads(response.data.decode("utf-8"))
    
    return [
        entry['ioc']
        for entry in response_data.get('data', [])
        if entry['ioc_type'] == ioc_type
    ]
    

def get_threatfox_domains() -> list[str]:
    return get_threatfox_data("domain")

def get_threatfox_ips() -> list[str]:
    return get_threatfox_data("ip:port")

def get_threatfox_urls() -> list[str]:
    return get_threatfox_data("url")