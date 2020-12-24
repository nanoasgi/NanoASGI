# API

## class App()

The ASGI application class of NanoASGI. Instances are callable WSGI applications.

### Methods:
#### def route(metod='GET', path)
A decorator to bind a function to a request URL. Example:
```python
@app.route('GET', '/hello/<name>')
async def hello(request, name):
    return 'Hello %s' % name
```
**Note: The ``<name>`` part is a wildcard.**
- **method:** HTTP method (`GET`, `POST`, `PUT`, ...) or a list of
methods to listen to. (default: `GET`)
- **path:** Request path or a list of paths to listen to. If no
path is specified, it is automatically generated from the
signature of the function.

### def on(event)
A decorator to bind a function to an event. Example:
```python
@app.on('startup')
async def on_startup():
    print('Ready to serve requests')
```
- **event:** lifespan event (`startup`, `shutdown`, ...) to listen to.

## class Request(path, method, headers, query, body, text, json)

A combination of ASGI Request object and Scope that adds a lot of convenient access methods and properties. Most of them are read-only. This is the recommended way to store and access request-specific data.
- `path` (_Unicode string_) – HTTP request target excluding any query string, with percent-encoded sequences and UTF-8 byte sequences decoded into characters.
- `method` (_Unicode string_) – The HTTP method name, uppercased. `GET`,  `POST`, `HEAD` etc.
- `headers` (_{Unicode string: Unicode string}_) – An dict of `{name:  value}` pairs, where `name` is the header name, and `value` is the header value. Order of header values will be preserved from the original HTTP request; order of header names is not important. Duplicates are possible and must be preserved in the message as received. Header names are lowercased. Pseudo headers (present in HTTP/2 and HTTP/3) are be removed; if `:authority` is present its value will be added to the start of the iterable with `host` as the header name or replace any existing host header already present.
- `query`(_{Unicode string: Unicode string}_) – Parsed from query string(URL portion after the `?`, percent-encoded). An dict of `{name:  value}` pairs, where `name` is the quary name, and `value` is the query value. Order of query names is not important. Duplicates are possible. e.g.: `https://search.com?q=test&lang=en`**->**`{'q': 'test', 'lang': 'en'}`
- `body` (_byte string_) – Body of the request as raw bytes.
- `text`(_Unicode string_) – Body of the request as text.
- `json`(_Unicode string_) – Body of the request as object if it's json string.

## class Response(data=None, status, headers, body)

Storage class for a response body as well as headers and cookies.

- `data` (_bytes, str, list, dict or None_) – Data for send to client. if missing defaults to `None`.
- `status`  (_int_) – HTTP status code.
- `headers` (_Iterable[[byte string, byte string]]_) – An iterable of `[name,  value]` two-item iterables, where `name` is the header name, and `value` is the header value. Header names are lowercased.  if missing defaults to an empty list.
- `body` – Body of the response. body is the `data`, prepared to serve.  if missing defaults to `b""`.
