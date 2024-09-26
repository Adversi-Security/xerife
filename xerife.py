import argparse

from feeds.greensnow import get_greensnow_ips
from feeds.bazaar import get_bazaar_sha256, get_bazaar_recent_sha256
from feeds.malcore import get_malcore_data, get_malcore_sha256, get_malcore_ips
from feeds.threatview import get_threatview_data, get_threatview_sha1, get_threatview_domains
from feeds.digitalsite import get_digitalsite_data, get_digitalsite_domains, get_digitalsite_ips
from feeds.threatfox import get_threatfox_data, get_threatfox_domains, get_threatfox_ips, get_threatfox_urls

#
# Main :3
#
if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Get IOCs from various sources.')

    parser.add_argument('--hashes', action="store_true", help='get malicious sha256 hashes')
    parser.add_argument('--domains', action="store_true", help='get malicious domains')
    parser.add_argument('--ips', action="store_true", help='get malicious IP addresses')
    parser.add_argument('--urls', action="store_true", help='get malicious URLs')
    parser.add_argument('-o','--output', help='the filename to receive the IOCs')

    args = parser.parse_args()

    filename = 'output.txt'

    if args.output:
        filename = args.output

    if args.hashes:
        sha256, sha1 = set(), set()
        l = get_bazaar_sha256() + get_bazaar_recent_sha256() + get_threatview_sha1()
        
        for h in l:
            if len(h) == 64:
                sha256.add(h)
            if len(h) == 40:
                sha1.add(h)

        with open(filename, 'w+') as fp:
            fp.write('\n'.join(sha256) + '\n')
            fp.write('\n'.join(sha1) + '\n')
    
    if args.domains:
        l = get_threatfox_domains() + get_digitalsite_domains()

        domains = set(l)

        with open(filename, 'w+') as fp:
            fp.write('\n'.join(domains) + '\n')
            fp.write(get_threatview_domains())
    
    if args.ips:
        l = get_threatfox_ips() + get_digitalsite_ips() + get_greensnow_ips() + get_malcore_ips()

        ips = set(l)

        with open(filename, 'w+') as fp:
            fp.write('\n'.join(ips) + '\n')

    if args.urls:
        l = get_threatfox_urls()

        urls = set(l)

        with open(filename, 'w+') as fp:
            fp.write('\n'.join(urls) + '\n')
