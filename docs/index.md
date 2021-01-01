---
layout: default
title: Docs
nav_order: 1
permalink: /
---
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
**See [Docs](docs) for more infomation.**
## License

Code and documentation are available according to the MIT License:page_with_curl: (see [LICENSE](LICENSE)).

The NanoASGI logo however is NOT covered by that license. It is allowed to use the logo as a link to the repo or in direct context with the unmodified library. In all other cases, please ask first.

[![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png)](https://www.buymeacoffee.com/Ksengine)

[![Lines of code](https://img.shields.io/tokei/lines/github/nanoasgi/nanoasgi?logo=github&style=flat-square)](#nolink)
[![GitHub issues](https://img.shields.io/github/issues/nanoasgi/nanoasgi?logo=github&style=flat-square)](#nolink)
[![GitHub top language](https://img.shields.io/github/languages/top/nanoasgi/nanoasgi?logo=python&style=flat-square&labelColor=f0ffff)](#nolink)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/nanoasgi/nanoasgi/Python%20package?logo=github)](#nolink)
[![GitHub](https://img.shields.io/github/license/nanoasgi/nanoasgi?style=flat-square&logo=github)](#nolink)
[![GitHub issues](https://img.shields.io/github/issues/nanoasgi/NanoASGI?logo=github&style=flat-square)](https://github.com/nanoasgi/NanoASGI/issues)
[![GitHub forks](https://img.shields.io/github/forks/nanoasgi/NanoASGI?logo=github&style=flat-square)](https://github.com/nanoasgi/NanoASGI/network)
[![GitHub stars](https://img.shields.io/github/stars/nanoasgi/NanoASGI?logo=github&style=flat-square)](https://github.com/nanoasgi/NanoASGI/stargazers)
[![GitHub license](https://img.shields.io/github/license/nanoasgi/NanoASGI?logo=github&style=flat-square)](https://github.com/nanoasgi/NanoASGI/blob/main/LICENSE)
[![Twitter](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2Fnanoasgi%2FNanoASGI)](https://twitter.com/intent/tweet?text=Wow:&url=https%3A%2F%2Fgithub.com%2Fnanoasgi%2FNanoASGI)
[![PyPI - Implementation](https://img.shields.io/pypi/implementation/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nanoasgi?logo=python&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI](https://img.shields.io/pypi/v/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI - License](https://img.shields.io/pypi/l/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI - Downloads](https://img.shields.io/pypi/dd/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI - Format](https://img.shields.io/pypi/format/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![PyPI - Status](https://img.shields.io/pypi/status/nanoasgi?logo=pypi&labelColor=f0ffff&style=flat-square)](#nolink)
[![Downloads](https://pepy.tech/badge/nanoasgi/week)](https://pepy.tech/project/nanoasgi)


[**LOGO**](#logo) - [Perditax](https://commons.wikimedia.org/wiki/File:C20_Fullerene.png), CC0, via Wikimedia Commons
