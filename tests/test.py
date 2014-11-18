__author__ = 'Vivan'

import json

from uberipy import Uber
from uberipy import (
    UnauthorisedException, MalformedRequestException, InvalidRequestException,
    UnacceptableContentException, NotFoundException, RateLimitException, ServerException, UberipyException
)

uber = Uber(
    'CPPRD08zE_pagsI5CmSyh3URj7ITxpXx',
    'TbP2woYtHL2_pPuBxM2r-Q8OoPr6BFBwKUt_w4sZ',
    'UcAhCFC2SdKXKb2_jNjwmyy8LtuSg552C5ZQ9yPK'
)

#estimate = uber.get_fare_estimate(51.5289526,-0.1410641,51.5107835,-0.1167915)
try:
    products = uber.get_products(51.5286416,-0.1015987)
    start_latitude = 51.5252162
    start_longitude = -0.1036919
    end_latitude = 51.5049949
    end_longitude = -0.0103968

    time_estimate = uber.get_time_estimate(start_latitude, start_longitude, None, 'ea52c793-1ad7-4c46-96b3-b1836b8cd0f9' )
    time_object = uber.get_time_estimate_object(time_estimate, "uberx")
    print time_object.get_estimate

    fare_estimate = uber.get_price_estimate(start_latitude, start_longitude, end_latitude, end_longitude)
    fare_object = uber.get_price_estimate_object(fare_estimate, "uberexec")

    print fare_object.get_surge_multiplier
    #print json.dumps(fare_estimate, sort_keys=True, indent=4, separators=(',', ': '))


except UberipyException as e:
    print e.get_message
#print products
#print estimate
