import requests
import re
import json

import api_info

#
# Malware Bazaar
#
def get_bazaar_sha256() -> list[str]:
    data = requests.post("https://mb-api.abuse.ch/api/v1/", data=api_info.bazaar_data, headers=api_info.bazaar_headers).json()
    return [item['sha256_hash'] for item in data.get('data', [])]

def get_bazaar_recent_sha256() -> list[str]:
    pattern = r'\b[a-fA-F0-9]{64}\b'
    content = requests.get("https://bazaar.abuse.ch/export/txt/sha256/recent/").text
    return re.findall(pattern, content) 
