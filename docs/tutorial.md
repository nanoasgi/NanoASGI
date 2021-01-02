---
layout: default
title: Tutorial
nav_order: 2
---
# Tutorial

This tutorial introduces you to the concepts and features of the NanoASGI web framework and covers basic and advanced topics alike. You can read it from start to end, or use it as a reference later on. The API Reference (not created yet) may be interesting for you, too. It covers more details, but explains less than this tutorial. Solutions for the most common questions can be found in our  Recipes(not created yet)  collection or on the  Frequently Asked Questions(not created yet)  page. If you need any help, join our  mailing list(not created yet)  or visit us in our  IRC channel(not created yet)

**See [Installation page](installation.md) for Installation guide.**

## QUICKSTART: “HELLO WORLD”

This tutorial assumes you have NanoASGI either  [installed](#installation)  or copied into your project directory. Let’s start with a very basic “Hello World” example:
```python
from nanoasgi import App, Response


app = App()

@app.route('GET', '/hello/{name}/')
async def hello_handler(request, name):
    return Response(
        {'result': f'Hello {name}!'},
        status=200,
        headers=[('Content-Type', 'application/json')],
    )
```
This is it. Run this script, using an ASGI server like uvicorn. I'll use Unicorn.
```bash
uvicorn example:app
```
Visit  http://localhost:8000/hello/World!.  and you will see “Hello World!” in your browser. Here is how it works:

The  `route()` decorator binds a piece of code to an URL path. In this case, we link the  `/hello`  path to the  `hello_handler()`  function. This is called a  route  (hence the decorator name) and is the most important concept of this framework. You can define as many routes as you want. Whenever a browser requests a URL, the associated function is called and the return value is sent back to the browser. It’s as simple as that.

This is just a demonstration of the basic concept of how applications are built with NanoASGI. Continue reading and you’ll see what else is possible.
