![logo](https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/C20_Fullerene.png/128px-C20_Fullerene.png)
![logo text](docs/logotext.png)

![Lines of code](https://img.shields.io/tokei/lines/github/nanoasgi/nanoasgi?logo=github&style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/nanoasgi/nanoasgi?logo=github&style=flat-square)
![GitHub top language](https://img.shields.io/github/languages/top/nanoasgi/nanoasgi?logo=python&style=flat-square&logoColor=9cf)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/nanoasgi/nanoasgi/Python%20package?logo=github)
![GitHub](https://img.shields.io/github/license/nanoasgi/nanoasgi?style=flat-square&logo=github)


#  NanoASGI: Asynchronous Python Web Framework

NanoASGI is a fast:zap:, simple and light:bulb:weight [ASGI](https://asgi.readthedocs.io "Asynchronous Server Gateway Interface") micro:microscope: web:earth_asia:-framework for Python:snake:. It is distributed as a single file module and has no dependencies other than the [Python Standard Library.](http://docs.python.org/library/)


## Download and Install

Download :arrow_down: nanoasgi.py into your project directory. There are no hard dependencies other than the Python standard library. NanoASGI runs with Python versions above 3.7.


## Example

```python
# example.py
from nanoasgi import App, Response


app = App()


@app.on('startup')
async def on_startup():
    print('Ready to serve requests')


@app.on('shutdown')
async def on_shutdown():
    print('Shutting down')


@app.route('GET', '/api/hello/{name}/')
async def hello_handler(request, name):
    return Response(
        {'result': f'Hello {name}!'},
        status=200,
        headers=[('Content-Type', 'application/json')],
    )
```
```bash
uvicorn example:app
```

## License

Code and documentation are available according to the MIT License:page_with_curl: (see [LICENSE](LICENSE)).

The NanoASGI logo however is NOT covered by that license. It is allowed to use the logo as a link to the repo or in direct context with the unmodified library. In all other cases, please ask first.

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/Ksengine)

[**LOGO**](#logo) - [Perditax](https://commons.wikimedia.org/wiki/File:C20_Fullerene.png), CC0, via Wikimedia Commons
