import requests

#
# Greensnow IP's
#
def get_greensnow_ips() -> list[str]:
    return requests.get(
        "https://blocklist.greensnow.co/greensnow.txt"
    ).text.split('\n')[:-1]