# TUF and PIP

## Setup

For development or testing purposes, it is recommended that you install and use `virtualenv`. More on virtualenv [here](https://virtualenv.pypa.io/en/stable/).

#### 1. Install virtualenv
Using pip
```sh
$ pip install virtualenv
```
Use virtualenv to create a Python environment
```sh
$ virtualenv env
$ source ./env/bin/activate
```
#### 2. Download and Install TUF
Clone the latest version of TUF
```sh
$ git clone --recursive git@github.com:theupdateframework/tuf.git
```
Install TUF
```sh
$ pip install -r dev-requirements.txt
```
#### 3. Re-install PIP to incorporate TUF
Clone the current development version 
```sh
$ git clone https://github.com/prasanmouli/pip
```
Install PIP
```sh
$ pip install -e /path/to/pip/directory
```
This should update pip in that environment to add support for TUF. 

## Test

Try running 
```sh
$ pip install simplejson --no-cahce-dir
```
You should be able to see TUF metadata being downloaded. This version of pip will automatically download the initial client metadata required if it doesn't already exist. 
