from rest_framework.throttling import BaseThrottle

class RegisterThrottle(BaseThrottle):
    rate="15/hour"

class TokenObtainThrottle(BaseThrottle):
    rate="10/hour"

class BasicThrottle(BaseThrottle):
    rate="50/minute"