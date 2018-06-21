# 511-gtfsrt-list
Script to understand which 511 API feeds have GTFSrt available

## Usage

Python3 main.py <YOUR_511_API_KEY>

Agencies with TripUpdates: ['3D', 'AC', 'BA', 'CC', 'CT', 'DE', 'FS', 'GG', 'MA', 'SC', 'SF', 'SM', 'SR', 'ST', 'VN', 'WC', 'WH']
Agencies with Positions:   ['3D', 'AC', 'BA', 'CC', 'CT', 'DE', 'FS', 'GG', 'MA', 'SC', 'SF', 'SM', 'SR', 'ST', 'VN', 'WC', 'WH']

## Dependencies:
    Google Transit GTFSrt bindings (`python3 -m pip install --upgrade gtfs-realtime-bindings`)
    Requests (`python3 -m pip install requests`)
