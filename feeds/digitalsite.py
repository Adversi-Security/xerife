import requests

#
# DigitalSite
#
def get_digitalsite_data(list_name: str) -> list[str]:
    base_url = "https://osint.digitalside.it/Threat-Intel/lists/"
    url = f"{base_url}{list_name}"
    response = requests.get(url)
    return response.text.split("#")[-1].strip().split('\n')[1:-1]
    

def get_digitalsite_domains() -> list[str]:
    return get_digitalsite_data("latestdomains.txt")

def get_digitalsite_ips() -> list[str]:
    return get_digitalsite_data("latestips.txt")