from firebase_functions import https_fn, options
import flask
import flask_cors

app = flask.Flask(__name__)
flask_cors.CORS(app)

@app.get('/')
def hello_server():
    return 'Hello, server!'

@https_fn.on_request(timeout_sec=60, memory=options.MemoryOption.GB_1)
def on_request(req: https_fn.Request) -> https_fn.Response:
    with app.request_context(req.environ):
        return app.full_dispatch_request()
