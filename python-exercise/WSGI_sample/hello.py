def application(environ, start_response):
    start_response("200 OK",[("Content-Type", "text/html")])
    return [b'<h1>Web Service Test</h1>']
