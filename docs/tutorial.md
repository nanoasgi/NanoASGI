
# Tutorial

This tutorial introduces you to the concepts and features of the NanoASGI web framework and covers basic and advanced topics alike. You can read it from start to end, or use it as a reference later on. The API Reference (not created yet) may be interesting for you, too. It covers more details, but explains less than this tutorial. Solutions for the most common questions can be found in our  Recipes(not created yet)  collection or on the  Frequently Asked Questions(not created yet)  page. If you need any help, join our  mailing list(not created yet)  or visit us in our  IRC channel(not created yet)


## INSTALLATION

You’ll need Python 3.6 or newer to run NanoASGI applications. Run following command on your command prompt(cmd)/terminal to find the version of Python.
```bash
python --version
```
> Maybe you should use `python3` or `py` instead of `python` in above command.

NanoASGI does not depend on any external libraries. You can just download  [`nanoasgi.py`](https://github.com/nanoasgi/NanoASGI/blob/main/nanoasgi.py)  into your project directory and start coding:
```bash
wget https://raw.githubusercontent.com/nanoasgi/NanoASGI/main/nanoasgi.py
```
```bash
curl https://raw.githubusercontent.com/nanoasgi/NanoASGI/main/nanoasgi.py --output "nanoasgi.py"
```
This will get you the latest development snapshot that includes all the new features. If you prefer a more stable environment, you should stick with the stable releases. These are available on  [PyPI](http://pypi.python.org/pypi/nanoasgi)  and can be installed via  **pip**  (recommended),  **easy_install**  or your package manager:
```bash
sudo pip install nanoasgi              # recommended
```
```bash
sudo easy_install nanoasgi             # alternative without pip
```

If you do not have permissions to install packages system-wide or simply don’t want to, create a  [virtualenv](http://pypi.python.org/pypi/virtualenv)  first:
```bash
virtualenv develop              # Create virtual environment
$ source develop/bin/activate     # Change default python to virtual one
(develop)$ pip install -U nanoasgi  # Install NanoASGI to virtual environment
```
Or, if virtualenv is not installed on your system:
```bash
$ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
$ python virtualenv.py develop    # Create virtual environment
$ source develop/bin/activate     # Change default python to virtual one
(develop)$ pip install -U bottle  # Install NanoASGI to NanoASGI environment
```
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
This is it. Run this script, using an ASGI server like uvicorn
```bash
uvicorn example:app
```
Visit  http://localhost:8080/hello/World!.  and you will see “Hello World!” in your browser. Here is how it works:

The  `route()` decorator binds a piece of code to an URL path. In this case, we link the  `/hello`  path to the  `hello_handler()`  function. This is called a  route  (hence the decorator name) and is the most important concept of this framework. You can define as many routes as you want. Whenever a browser requests a URL, the associated function is called and the return value is sent back to the browser. It’s as simple as that.

This is just a demonstration of the basic concept of how applications are built with NanoASGI. Continue reading and you’ll see what else is possible.
