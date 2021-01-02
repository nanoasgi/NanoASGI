---
title: Installation
nav_order: 2
---
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
