from spin_sdk import http
from spin_sdk.http import Request, Response

from consumer.imports.verify import verify

class IncomingHandler(http.IncomingHandler):
    def handle_request(self, request: Request) -> Response:
        #valid = verify("", "", "")
        #print(valid)
        res = verify(bytes("", 'utf-8'), bytes("", 'utf-8'), bytes("", 'utf-8'))
        print(res)
        return Response(
            200,
            {"content-type": "text/plain"},
            bytes("Hello from Python!", "utf-8")
        )