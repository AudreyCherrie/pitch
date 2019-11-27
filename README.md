## PITCH
updated on 23/11/2019

## By Audrey Macharia

## Description
This is an application that lets you know how you use your one minute within a first impression.

## features

1. Users can login or and register into the website.
2. users can read and write pitches

## Installation Requirements
To visit this website one needs a web browser.
link to the website or the url.
python3.6
Db

#### windows
* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python -m venv virtual`
* Activating the virtual environment may change based on the terminal or shell being used.
* For command prompt, enter `virtual\Scripts\activate` or simply type in activate.
* For powershell, the execution policy should be bypassed for the script to run. This can be done by entering `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` then proceeding on with entering .`.\virtual\Scripts\Activate.ps1`
* Install packages. `pip install -r requirements.txt`
* Setting environment variables differs with the terminal or shell being used
* 
* initiate database the database `python3.6 manage.py db upgrade`
* then start the server `python manage.py server`

#### unix

* In the root directory, create a virtual environment by opening command prompt or powershell and entering in `python3.x -m venv --without-pip virtual` replace x with version in host machine, preferably version v3.6 for this project
* Activate the virtual environment `source virtual/bin/activate`
* Download pip into the virtual environment `curl https://bootstrap.pypa.io/get-pip.py | python`
* Install packages. `pip install -r requirements.txt`>`
* initiate database the database `python3.6 manage.py db upgrade`
* start the server `python3.x manage.py server`