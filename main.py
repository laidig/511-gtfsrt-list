#!/usr/local/bin/python3

import json
import argparse
import codecs
from time import sleep
from google.transit import gtfs_realtime_pb2
import requests

parser = argparse.ArgumentParser(description='Check 511.org for valid GTFS-rt APIs')
parser.add_argument('key', help="API key for 511.org")
args = parser.parse_args()

agencyListUrl = "http://api.511.org/transit/gtfsoperators?format=json&api_key={}".format(args.key)

agencyList = requests.get(agencyListUrl)

agencyList = json.loads(codecs.decode(agencyList.content, encoding='utf-8-sig'))

agenciesWithTripUpdates = []
agenciesWithVehiclePositions = []


def isFeedValid(url):
    feed = gtfs_realtime_pb2.FeedMessage()
    r = requests.get(tripUpdateUrl)
    try:
        feed.ParseFromString(r.content)
        if len(feed.entity) > 0:
            return True
        else:
            return False
    except:
        return False


for a in agencyList:
    agencyId = a['Id']
    tripUpdateUrl = "http://api.511.org/transit/TripUpdates?api_key={}&agency={}".format(args.key, agencyId)
    vehiclePositionUrl = "http://api.511.org/transit/VehiclePositions?api_key={}&agency={}".format(args.key, agencyId)
    if isFeedValid(tripUpdateUrl):
        agenciesWithTripUpdates.append(agencyId)
    if isFeedValid(vehiclePositionUrl):
        agenciesWithVehiclePositions.append(agencyId)
    sleep(.5)

print("Agencies with TripUpdates: " + str(agenciesWithTripUpdates))
print("Agencies with Positions:   " + str(agenciesWithVehiclePositions))


