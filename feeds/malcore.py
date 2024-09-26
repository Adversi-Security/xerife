import requests

import api_info

#
# Malcore
#
def get_malcore_data(data_type: str) -> list[str]:
    
    data_mapping = {
        "ips": api_info.malcore_ip_data,
        "sha256": api_info.malcore_sha256_data
    }

    response = requests.post(
            "https://api.malcore.io/api/feed",
            data=data_mapping[data_type],
            headers=api_info.malcore_headers
    )
    json_data = response.json()

    if data_type == "ips":
            return json_data.get('data', {}).get('data', {}).get('list', [])
    elif data_type == "sha256":
            pass


def get_malcore_sha256() -> str:
    return get_malcore_data("sha256")

def get_malcore_ips() -> list[str]:
    return get_malcore_data("ips")
