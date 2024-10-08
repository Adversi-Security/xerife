
# Xerife.py - IOC Aggregation Tool

`xerife.py` is a tool that collects Indicators of Compromise (IOCs) from various sources, such as:

- [MalwareBazaar](https://bazaar.abuse.ch/)
- [Malcore](https://malcore.io/)
- [ThreatFox](https://threatfox.abuse.ch/)
- [DigitalSite](https://osint.digitalside.it/)
- [GreenSnow](https://greensnow.co/)
- [ThreatView](https://threatview.io/)
- [AlienVault](https://otx.alienvault.com/)

## Features

- Aggregates multiple types of IOCs, including:
  - Malicious SHA256 hashes
  - Malicious domains
  - Malicious IP addresses
  - Malicious URLs
- Outputs the IOCs into a specified file for further analysis.

## Usage

```bash
usage: xerife.py [-h] [--hashes] [--domains] [--ips] [--urls] [-o OUTPUT]

Get IOCs from various sources.

optional arguments:
  -h, --help            show this help message and exit
  --hashes              get malicious sha256 hashes
  --domains             get malicious domains
  --ips                 get malicious IP addresses
  --urls                get malicious URLs
  -o OUTPUT, --output OUTPUT
                        the filename to receive the IOCs
```

## Examples

1. Get all IOCs and save them to a file:
    ```bash
    python xerife.py --hashes --domains --ips --urls -o iocs.txt
    ```

2. Get only malicious domains and IP addresses:
    ```bash
    python xerife.py --domains --ips -o domains_ips.txt
    ```

3. Get SHA256 hashes and output to `hashes.txt`:
    ```bash
    python xerife.py --hashes -o hashes.txt
    ```

## Requirements

Ensure that Python 3.x is installed on your machine. Additional dependencies might be required based on the data sources being used.

## Contributing

If you'd like to contribute to the development of this tool, feel free to fork this repository and create a pull request.

## License

This project is licensed under the MIT License.
