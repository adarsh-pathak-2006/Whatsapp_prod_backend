from rest_framework.throttling import SimpleRateThrottle

class RegisterThrottle(SimpleRateThrottle):
    rate="15/hour"
    def get_cache_key(self, request, view):
        return self.get_ident(request)

class TokenObtainThrottle(SimpleRateThrottle):
    rate="10/hour"
    def get_cache_key(self, request, view):
        return self.get_ident(request)

class BasicThrottle(SimpleRateThrottle):
    rate="50/minute"
    def get_cache_key(self, request, view):
        if request.user.is_authenticated:
            return request.user.pk
        return self.get_ident(request)