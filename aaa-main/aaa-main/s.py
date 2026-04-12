from mitmproxy import http

def response(flow: http.HTTPFlow):
    url = flow.request.pretty_url

    # fileinfo -> aa
    if "fileinfo" in url:
        with open("aa", "rb") as f:
            data = f.read()

        flow.response = http.Response.make(
            200,
            data,
            {
                "Content-Type": "application/octet-stream",
                "Content-Encoding": "gzip",
                "Connection": "keep-alive"
            }
        )

    # assetindexer -> a
    elif "assetindexer" in url:
        with open("rrb.txt", "rb") as f:
            data = f.read()

        flow.response = http.Response.make(
            200,
            data,
            {
                "Content-Type": "application/octet-stream",
                "Content-Encoding": "gzip",
                "Connection": "keep-alive"
            }
        )