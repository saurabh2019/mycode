#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

#imports always go at the top of your code
import requests
LOOKUPAPI = 'https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=17042&date=2019-01-24&distance=25&API_KEY=8E37C209-52C8-4D2F-A382-33C48D60EE20'
#Replace me with AirNow's Generated URL


def main():
    """Run time code"""
    # create r, which is our request object
    r = requests.get(LOOKUPAPI)
    ##Set up screen
    print("Weather Forecast")
    print("-----------------")

    #Display json we returned
    for x in r.json():
      print(x.get('DateForecast'))
      print("---------------------")
      print(x.get("Discussion"))

    # display the methods available to our new object
   # print( r.json() )

main()
