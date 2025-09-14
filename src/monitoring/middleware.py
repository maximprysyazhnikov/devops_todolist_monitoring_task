from __future__ import annotations
from .metrics import REQUESTS_TOTAL

class PrometheusRequestCounterMiddleware:
    """Рахує тільки GET/POST — за вимогою."""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method in ("GET", "POST"):
            REQUESTS_TOTAL.labels(method=request.method).inc()
        return self.get_response(request)
