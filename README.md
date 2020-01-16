# Event Registration - REST API

[![GitHub license](https://img.shields.io/github/license/arch888/MiStay_REST?logo=github&)](https://github.com/arch888/MiStay_REST/blob/master/LICENSE)[![GitHub last commit](https://img.shields.io/github/last-commit/arch888/MiStay_REST?logo=github)](https://github.com/arch888/MiStay_REST/)![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/arch888/MiStay_REST?logo=snyk&color=green)



## About Problem

To **design Event Registration system REST API** with ability to do following tasks - 

● Users can create events

●Users can limit the number of attendees

● Users can delete an event

● Users can view public events

● Private events can be viewed only by invited users

● Users should be able to register/unregister for an event

● Users cannot register for another event if its schedule overlaps with a previously registered event

## Pre-Requisites

[![GitHub top language](https://img.shields.io/github/languages/top/arch888/MiStay_REST?label=Python&logo=Python)](https://github.com/arch888/MiStay_REST/)[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arch888/MiStay_REST?logo=github&color=teal)](https://github.com/arch888/MiStay_REST/)[![Issues](https://img.shields.io/github/issues/arch888/MiStay_REST)

](https://github.com/arch888/MiStay_REST)

The Source-Code for this project is written using Python. Make Sure you have [Python](https://www.python.org/) Installed on your PC. If you are using Windows/Mac please install from [here](https://www.python.org/downloads/).

Also make sure you have install [pip](https://pypi.org/project/pip/) properly in your system. [Link](https://www.liquidweb.com/kb/install-pip-windows/)

To check if you have Python and pip installed properly please use following commands in your terminal/command prompt.

- **Test Python : -** To see if python installed in your terminal type `python3 --version` in Terminal. This should print the version number. so you'll see something like this `Python 3.6.8` .
- **Test pip :-** To see if pip is installed. type `pip3 --version`.This will print the version number. so you'll see something like this `pip 9.0.1`.

> **Note:** You have to install Python and pip separately.

## How to Run ?

Clone the Repository in your local system.

```
git clone https://github.com/arch888/MiStay_REST
```

Navigate (`cd`) to this folder using following command

```
cd MiStay_REST/
```

Next Step is to install [Django](https://docs.djangoproject.com/en/3.0/topics/install/) and other requirements using the following command

```
pip3 install -r requirements.txt
```

Migrate the Project such that Database and Tables and everything is synchronised.

```
python3 manage.py migrate
```

Now It's turn to host the project on local server which can be done using following command 

```
python3 manage.py runserver 8000
```

Here 8000 is the port on which we wanted to serve our API if you wanted to use on any other port you can replace there.

If you see something like this in your terminal/Command Prompt

```
Performing system checks...

System check identified no issues (0 silenced).
January 16, 2020 - 17:48:14
Django version 3.0.2, using settings 'MiStay_REST.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Hurrah ! You are Done with the Setup. If you are facing any issue please create an [issue](https://github.com/arch888/MiStay_REST/issues).

