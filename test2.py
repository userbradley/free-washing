"""Redirect HTTP requests to another server."""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    # pretty_host takes the "Host" header of the request into account,
    # which is useful in transparent mode where we usually only have the IP
    # otherwise.
    if flow.request.pretty_host == "https://mobile.laundryrestart.com/jhclaundry/api/checkout/check-payment/67817":
        flow.request.host = "https://mobile.laundryrestart.com/jhclaundry/api/checkout/check-payment/6892"