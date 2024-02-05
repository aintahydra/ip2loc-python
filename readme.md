# ip2loc
Retrieve geolocation of given IP(s)

# Usage

- `python3 ip2loc.py <GeoLite2-City.mmdb> <an_ip_addr>`, or
- `python3 ip2loc.py <GeoLite2-City.mmdb> -f <ip_addresses_file>`
	- The <GeoLite2-City.mmdb> database can be downloaded from the MaxMind webpage
	- <an_ip_addr> is a single IPv4 addr
	- <ip_addresses_file> should be a text file that has multiple IPs in each line

# How to use
- `python3 ip2loc.py ./GeoLite2-City_20230202/GeoLite2-City.mmdb ./ip_list.txt`
- `python3 ip2loc.py ./GeoLite2-City_20230202/GeoLite2-City.mmdb 123.234.123.234`

# Shell users may run it like
```
	sed '/\n/!s/[0-9.]\+/\n&\n/;/^\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}\n/P;D' <some_TXT_file> | uniq -u | xargs -n 1 -t python3 ip2loc.py <GeoLite2-City.mmdb>
```
	- when <some_TXT_file> contains IP addresses, filter those addresses and look for their locations
