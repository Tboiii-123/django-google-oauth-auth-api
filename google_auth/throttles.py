# throttles.py

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

#AnonRateThrottle for annonymous
#Annon uses IP address cause dey are not authenticated

#UserRateThrottle for authenticated user
#authenticated user ID


class LoginThrottle(AnonRateThrottle):
    rate = "7/min"



class MessageThrottle(UserRateThrottle):
    rate = "20/min"