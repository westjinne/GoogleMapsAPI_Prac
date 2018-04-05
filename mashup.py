from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stdout = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "IEFTGLJWGSSXVXUOTNQS2IR5MZQH3JH0GBXCWSKNEBXHCMLJ"
foursquare_client_secret = "LNGMY5D55PNKNSXBQFCGOFT31AO4KYIEACZRLO1QD2S123RB"


def findARestaurant(mealType, location):
#1. use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
#        latitude, longitude = getGeocodeLocation(location)
        myLocation = getGeocodeLocation(location)
        latitude = myLocation[0]
        longitude = myLocation[1]
#2. use foursquare api to find a nearby restaurant with the latitude, longitude, and mealType strings.
#hint: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
        url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&ll=%s,%s&query=%s&v=20180404' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, mealType))
        h = httplib2.Http()
        response, content = h.request(url, 'GET')
        result = json.loads(content)
#3. grab the first restaurant
        firstRes = result['response']['venues'][0]
        resName = firstRes['name']
        sys.stdout.write("Restaurant Name: %s" % resName)
        print

        resAddr = firstRes['location']['formattedAddress']

        sys.stdout.write("Restaurant Address: ")
        for i in resAddr:
            sys.stdout.write("%s " % i)
        print
"""
        photoUrlID = firstRes['id']
        photoUrl = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % (photoUrlID, foursquare_client_id, foursquare_client_secret))
        photoResult = json.loads(h.request(photoUrl, 'GET'))
"""
#Photo url part must be updated
#        prefix = firstRes['categories'][0]['icon']['prefix']
#        suffix = firstRes['categories'][0]['icon']['suffix']
#        return prefix, suffix
#        sys.stdout.write("Image: %s%s"%(prefix, suffix))
#        print

#sys.stdout.write("%s - %.2f" % (date, rate))

#4. get a 300x300 picture of the restaurant using the venue_id (can be changed by me, by altering the 300x300 value in the url of replacing it with 'original' to get the original picture)

#5. grab the first image

#6. if no image is available, insert default a image url

#7. return a dictionary containing the restaurant name, address, and image url

if __name__ == '__main__':
    findARestaurant("Pizza", "Tokyo, Japan")
    print
    findARestaurant("Tacos", "Jakarta, Indonesia")
    print
    findARestaurant("Tapas", "Maputo, Mozambique")
    print
    findARestaurant("Falafel", "Cairo, Egypt")
    print
    findARestaurant("Spaghetti", "New Delhi, India")
    print
    findARestaurant("Cappuccino", "Geneva, Switzerland")
    print
    findARestaurant("Sushi", "Los Angeles, California")
    print
    findARestaurant("Steak", "La Paz, Bolivia")
    print
    findARestaurant("Gyros", "Sydney, Australia")
