"""Send a reply from the proxy without sending any data to the remote server."""
from mitmproxy import http


def request(flow: http.HTTPFlow) -> None:
    if flow.request.pretty_url == "https://mobile.laundryrestart.com/jhclaundry/api/checkout/check-payment/67817":
        flow.response = http.Response.make(
            200,  # (optional) status code
            b"""{"status": "none"}""",  # (optional) content
            {"Content-Type": "application/json"}  # (optional) headers
        )