#!/bin/python3
# Usage: python3 ip2loc.py <GeoLite2-City.mmdb> <an_IP_addr>
#     or python3 ip2loc.py <GeoLite2-City.mmdb> -f <ip_addresses_file>
#
#   - (ex1) python3 ip2loc.py ./GeoLite2-City_20230202/GeoLite2-City.mmdb ./ip_list.txt
#   - (ex2) python3 ip2loc.py ./GeoLite2-City_20230202/GeoLite2-City.mmdb 123.234.123.234
#
#   - The <GeoLite2-City.mmdb> database can be downloaded from the MaxMind webpage
#   - <an_IP_addr> is a single IPv4 addr
#   - <ip_addresses_file> should be a text file that has multiple IPs in each line
#
# Another tip
# Usage: sed '/\n/!s/[0-9.]\+/\n&\n/;/^\([0-9]\{1,3\}\.\)\{3\}[0-9]\{1,3\}\n/P;D' <some_TXT_file> | uniq -u | xargs -n 1 -t python3 ip2loc.py ./go-ip2loc/GeoLite2-City_20240202/GeoLite2-City.mmdb 
#   - when <some_TXT_file> contains IP addresses, filter those addresses and look for their locations

import maxminddb # pip install maxminddb
import argparse

def get_loc(db, ip):
    try:
        record = db.get(ip)
        
        # Print out
        print(f"IP: {ip}")
        print(f"City: {record.get('city', {}).get('names', {}).get('en', 'N/A')}")
        print(f"Region: {record.get('subdivisions', [{}])[0].get('names', {}).get('en', 'N/A')}")
        print(f"Country: {record.get('country', {}).get('names', {}).get('en', 'N/A')}")
        print(f"Latitude: {record.get('location', {}).get('latitude', 'N/A')}")
        print(f"Longitude: {record.get('location', {}).get('longitude', 'N/A')}")
        print("--------------")

    except Exception as e:
        print(f"Error getting geolocation for {ip}: {e}")

def main():

    parser = argparse.ArgumentParser(description='Retrieve geolocation of a given IP(s)')
    parser.add_argument('db_path', help='The path to MaxMind geolite2 db file(.mmdb)')
    parser.add_argument('-f', '--file', help='The path to the text file containing IP addresses')
    parser.add_argument('ip_addr', nargs='?', help='An IP address')

    args = parser.parse_args()

    with maxminddb.open_database(args.db_path) as db:
        if args.ip_addr:
            get_loc(db, args.ip_addr)
        elif args.file: 
            try:
                with open(args.file, 'r') as file:
                    for line in file:
                        ip = line.strip()
                        get_loc(db, ip)
            except Exception as e:
                print(f"Error opening file: {e}")
        
        else:
            printf("You need to provide an IP address or a file path")

if __name__ == "__main__":
    main()