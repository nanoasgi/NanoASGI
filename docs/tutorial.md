# Tutorial

This tutorial introduces you to the concepts and features of the NanoASGI web framework and covers basic and advanced topics alike. You can read it from start to end, or use it as a reference later on. The API Reference (not created yet) may be interesting for you, too. It covers more details, but explains less than this tutorial. Solutions for the most common questions can be found in our  Recipes(not created yet)  collection or on the  Frequently Asked Questions(not created yet)  page. If you need any help, join our  mailing list  or visit us in our  IRC channel(not created yet)
## INSTALLATION

NanoASGI does not depend on any external libraries. You can just download  [`nanoasgi.py`](https://github.com/nanoasgi/NanoASGI/blob/main/nanoasgi.py)  into your project directory and start coding:
```python
wget https://raw.githubusercontent.com/nanoasgi/NanoASGI/main/nanoasgi.py
```
```python
curl https://raw.githubusercontent.com/nanoasgi/NanoASGI/main/nanoasgi.py --output "nanoasgi.py"
```
This will get you the latest development snapshot that includes all the new features. If you prefer a more stable environment, you should stick with the stable releases. These are available on  [PyPI](http://pypi.python.org/pypi/nanoasgi)  and can be installed via  **pip**  (recommended),  **easy_install**  or your package manager:
```python
sudo pip install nanoasgi              # recommended
```
```python
sudo easy_install nanoasgi             # alternative without pip
```

Either way, you’ll need Python 3.6 or newer to run NanoASGI applications. If you do not have permissions to install packages system-wide or simply don’t want to, create a  [virtualenv](http://pypi.python.org/pypi/virtualenv)  first:
```python
virtualenv develop              # Create virtual environment
$ source develop/bin/activate     # Change default python to virtual one
(develop)$ pip install -U nanoasgi  # Install bottle to virtual environment
```
Or, if virtualenv is not installed on your system:
```python
$ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
$ python virtualenv.py develop    # Create virtual environment
$ source develop/bin/activate     # Change default python to virtual one
(develop)$ pip install -U bottle  # Install bottle to virtual environment
```
