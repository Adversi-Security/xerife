
#
# Abuse.ch (Bazaar, Threatfox)
#
G_ABUSE_API_KEY = '' # fill me
bazaar_headers = { 'API-KEY': f'{G_ABUSE_API_KEY}' }
bazaar_data = {
    'query': 'get_recent',
    'selector': 'time',
}

G_THREATFOX_API_KEY = '' # fill me
threatfox_data = {
    'query' : 'get_iocs',
    'days' : 5
}

#
# Malcore.io
#
G_MALCORE_API_KEY = '' # fill me
malcore_headers = { 'apiKey': f'{G_MALCORE_API_KEY}' }
malcore_ip_data = {
    'feed_type' : 'ip',
}
malcore_sha256_data = {}
