from wsgiref.simple_server import make_server
from urllib.parse import parse_qs, unquote
import json

def app(env, start_response):
    headers = [('Content-type', 'text/plain; charset=utf-8')]

    try:
        params = parse_qs(env["QUERY_STRING"])
        if "species" in params:
            status = "200 OK"
            response = '{"credentials": "Rassilon"}'
        else:
            status = "404 Not Found"
            response = '{"credentials": "Unknown"}'
    except Exception as e:
        status = '500 Internal Server Error'
        response = {'error': str(e)}

    start_response(status, headers)
    return [json.dumps(response).encode()]

if __name__ == "__main__":
    with make_server("", 8888, app) as server:
        print("Server has started on port 8888...")
        server.serve_forever()