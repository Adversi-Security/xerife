import requests
import re

#
# Threatview.io
#
def get_threatview_data(feed_type: str) -> str:
    base_url = "https://threatview.io/Downloads/"
    feeds = {
        "sha1": "SHA-HASH-FEED.txt",
        "domains": "DOMAIN-High-Confidence-Feed.txt"
    }
    
    url = base_url + feeds[feed_type]
    return requests.get(url).text

def get_threatview_sha1() -> list[str]:
    data = get_threatview_data("sha1")
    pattern = r'\b[a-fA-F0-9]{40}\b'
    return re.findall(pattern, data)

def get_threatview_domains() -> str:
    return get_threatview_data("domains")