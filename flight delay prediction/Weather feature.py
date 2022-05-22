"""
Example script that scrapes data from the IEM ASOS download service
"""
from __future__ import print_function
import json
import time
import datetime
import pandas as pd
import io
# Python 2 and 3: alternative 4
try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

# Number of attempts to download data
MAX_ATTEMPTS = 6
# HTTPS here can be problematic for installs that don't have Lets Encrypt CA
SERVICE = "http://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"


def download_data(uri):
    """Fetch the data from the IEM
    The IEM download service has some protections in place to keep the number
    of inbound requests in check.  This function implements an exponential
    backoff to keep individual downloads from erroring.
    Args:
      uri (string): URL to fetch
    Returns:
      string data
    """
    attempt = 0
    while attempt < MAX_ATTEMPTS:
        try:
            data = urlopen(uri, timeout=300).read().decode("utf-8")
            if data is not None and not data.startswith("ERROR"):
                return data
        except Exception as exp:
            print("download_data(%s) failed with %s" % (uri, exp))
            time.sleep(5)
        attempt += 1

    print("Exhausted attempts to download, returning empty data")
    return ""


def get_stations_from_filelist(filename):
    """Build a listing of stations from a simple file listing the stations.
    The file should simply have one station per line.
    """
    stations = []
    for line in open(filename):
        stations.append(line.strip())
    return stations


def get_stations_from_networks():
    """Build a station list by using a bunch of IEM networks."""
    stations = []

    states = """AK AL AR AZ CA CO CT DE FL GA HI IA ID IL IN KS KY LA MA MD ME
     MI MN MO MS MT NC ND NE NH NJ NM NV NY OH OK OR PA RI SC SD TN TX UT VA VT
     WA WI WV WY"""

    #states = 'NJ'
    networks = []
    for state in states.split():
        networks.append("%s_ASOS" % (state,))

    for network in networks:
        # Get metadata
        uri = (
            "https://mesonet.agron.iastate.edu/geojson/network/%s.geojson"
        ) % (network,)
        data = urlopen(uri)
        jdict = json.load(data)
        for site in jdict["features"]:
            stations.append(site["properties"]["sid"])
    return stations

'''
def download_alldata():
    """An alternative method that fetches all available data.
    Service supports up to 24 hours worth of data at a time."""
    # timestamps in UTC to request data for
    startts = datetime.datetime(2013, 1, 1)
    endts = datetime.datetime(2013, 1, 3)
    interval = datetime.timedelta(hours=24)

    service = SERVICE + "data=all&tz=Etc/UTC&format=comma&latlon=yes&"

    now = startts
    while now < endts:
        thisurl = service
        thisurl += now.strftime("year1=%Y&month1=%m&day1=%d&")
        thisurl += (now + interval).strftime("year2=%Y&month2=%m&day2=%d&")
        print("Downloading: %s" % (now,))
        data = download_data(thisurl)
        outfn = "%s.txt" % (now.strftime("%Y%m%d"),)
        with open(outfn, "w") as fh:
            fh.write(data)
        now += interval
'''

def main():
    """Our main method"""
    # timestamps in UTC to request data for
    startts = datetime.datetime(2013, 1, 1)
    endts = datetime.datetime(2013, 8, 1)

    service = SERVICE + "data=all&tz=Etc/UTC&format=comma&latlon=yes&"

    service += startts.strftime("year1=%Y&month1=%m&day1=%d&")
    service += endts.strftime("year2=%Y&month2=%m&day2=%d&")

    # Two examples of how to specify a list of stations
    stations = get_stations_from_networks()
    # stations = get_stations_from_filelist("mystations.txt")
    for station in stations:
        #print(station)
        #station is the location within each state
        #change code here
        dest_history = set(['LGB', 'TUL', 'SAN', 'CAE', 'DFW', 'CLE', 'DCA', 'BQN', 'RDU', 'MYR', 'ORF', 'ACK', 'OMA', 'OAK', 'CMH', 'IND',
         'BNA', 'PWM', 'FLL', 'BDL', 'SAT', 'MSN', 'AVL', 'STT', 'EGE', 'CAK', 'SJU', 'RSW', 'HOU', 'BGR', 'RIC', 'GRR',
         'ROC', 'GSO', 'SMF', 'SDF', 'TYS', 'BUR', 'CVG', 'PIT', 'SFO', 'HNL', 'PBI', 'BUF', 'MCI', 'BWI', 'OKC', 'TVC',
         'GSP', 'ABQ', 'PSE', 'TPA', 'EYW', 'PVD', 'SAV', 'BHM', 'XNA', 'MVY', 'BOS', 'IAD', 'SRQ', 'MKE', 'MEM', 'SYR',
         'MDW', 'MIA', 'CHS', 'SNA', 'MHT', 'DAY', 'CRW', 'PSP', 'IAH', 'JAX', 'LAX', 'MSP', 'MTJ', 'BZN', 'BTV', 'SEA',
         'PHX', 'JAC', 'MSY', 'PHL', 'ATL', 'MCO', 'HDN', 'ALB', 'DTW', 'SJC', 'ORD', 'DSM', 'SLC', 'LAS', 'AUS', 'DEN',
         'CLT', 'PDX', 'CHO', 'STL'])
        history_origin = set(['EWR','LGA','JFK'])
        dest_test = set(['LGB', 'TUL', 'SAN', 'CAE', 'DFW', 'CLE', 'DCA', 'BQN', 'RDU', 'MYR', 'ORF', 'ACK', 'OMA', 'OAK', 'CMH', 'IND', 'BNA', 'PWM', 'FLL', 'SAT', 'MSN', 'AVL', 'STT', 'CAK', 'SJU', 'RSW', 'HOU', 'BGR', 'RIC', 'GRR', 'ROC', 'GSO', 'SMF', 'SDF', 'TYS', 'BUR', 'CVG', 'PIT', 'SFO', 'HNL', 'BUF', 'PBI', 'MCI', 'BWI', 'OKC', 'TVC', 'GSP', 'ABQ', 'PSE', 'TPA', 'PVD', 'SAV', 'ANC', 'BHM', 'XNA', 'MVY', 'BOS', 'IAD', 'SRQ', 'MKE', 'MEM', 'SYR', 'MDW', 'MIA', 'CHS', 'SNA', 'MHT', 'DAY', 'IAH', 'JAX', 'LAX', 'MSP', 'BZN', 'BTV', 'SEA', 'PHX', 'MSY', 'PHL', 'ATL', 'MCO', 'ALB', 'DTW', 'SJC', 'ORD', 'DSM', 'SLC', 'LAS', 'AUS', 'DEN', 'CLT', 'PDX', 'STL'])
        '''
        for value in history_origin:
            if value in history_origin:
                break
        '''
        if station not in history_origin:
            continue
        #一个station如果有多个destination的话

        uri = "%s&station=%s" % (service, station)
        print("Downloading: %s" % (station,))
        data = download_data(uri)
        '''
        outfn = "%s_%s_%s.txt" % (
            station,
            startts.strftime("%Y%m%d%H%M"),
            endts.strftime("%Y%m%d%H%M"),
        )
        '''
        #print(type(data))
        #print(data)

        df = pd.read_csv(io.StringIO(data), sep=",", header=5)
        df.to_csv('/Users/edwu/Desktop/UCI/LexisNexis Interview Project/origin data/'+station+'.csv')
        #print(df)
        #out = open(outfn, "w")
        #out.write(data)
        #out.close()


if __name__ == "__main__":
    #download_alldata()
    main()