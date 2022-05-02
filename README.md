[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
# Network Scanner
Uses ARP broadcast request to scan for local devices within specified IP range, returns IP and MAC addresses of found devices.

For use with Linux.
# Usage
Install requirements, run program.
```
pip install -r requirements.txt
sudo python3 network_scanner.py
```
You can specify the IP range when running, otherwise you will be prompted to enter when the program is run.
# Options
```
  -i, --ip TEXT  IP range to scan
  --help         Show this message and exit.
```