import falcon
from os import urandom
from base64 import b64encode

class RandomDataResource:
    def on_get(self, req, resp):
        length = int(req.params.get("length", "1024"))
        random_bytes = urandom(length)
        random_text = b64encode(random_bytes).decode('utf-8')

        # because data get larger when base64 encoded, trim to length to ensure fixed size
        # e.g. 1024 to get 1KB, 1048576 to get 1MB
        resp.text = random_text[0:length]
        resp.content_type = "text/plain"
        resp.status = falcon.HTTP_OK

app = application = falcon.App()
app.add_route("/random", RandomDataResource())
