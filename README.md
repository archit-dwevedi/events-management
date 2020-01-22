# Event Registration - REST API

[![GitHub license](https://img.shields.io/github/license/arch888/MiStay_REST?logo=github&)](https://github.com/arch888/MiStay_REST/blob/master/LICENSE)[![GitHub last commit](https://img.shields.io/github/last-commit/arch888/MiStay_REST?logo=github)](https://github.com/arch888/MiStay_REST/)[![Snyk Vulnerabilities for GitHub Repo](https://img.shields.io/snyk/vulnerabilities/github/arch888/MiStay_REST?logo=snyk&color=green)](https://github.com/arch888/MiStay_REST)



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

[![GitHub top language](https://img.shields.io/github/languages/top/arch888/MiStay_REST?label=Python&logo=Python)](https://github.com/arch888/MiStay_REST/)[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/arch888/MiStay_REST?logo=github&color=teal)](https://github.com/arch888/MiStay_REST/)[![Issues](https://img.shields.io/github/issues/arch888/MiStay_REST)](https://github.com/arch888/MiStay_REST)

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

## Tutorial 

To Check the working / tutorial of the whole project can be viewed through this [video](https://youtu.be/88pZ-NUW1V4)

#### Support

For API support, please email [dwevediar@gmail.com](mailto:dwevediar@gmail.com). 

### User Accounts Register & Login

In this project I have used the [Token-Based Authentication](https://auth0.com/learn/token-based-authentication-made-easy/) in which accessing some service through a account then we have to forward the User Token as a header in each request.

User model which is used in this Project is something Looks like

```python
email 					= EmailField(verbose_name="email", max_length=60)
username 				= CharField(max_length=30, unique=True)
date_joined				= DateTimeField(verbose_name='date joined')
last_login				= DateTimeField(verbose_name='last login', auto_now=True)
is_admin				= BooleanField(default=False)
is_active				= BooleanField(default=True)
is_staff				= BooleanField(default=False)
is_superuser			= BooleanField(default=False)
```

#### Registration

For Registration of the users we have to create a POST request  to the `/api/account/register` which can be easily understandable by the following process.

```
POST http://127.0.0.1:8000/api/account/register

POST Data - 
{
	"email"     : "sample@sample.com",
	"username"  : "sample_username",
	"password"  : "some_password",
	"password2" : "some_password"
}

Response - 

{
    "response": "successfully registered new user.",
    "email": "sample@sample.com",
    "username": "sample@sample.com",
    "pk": 3,
    "token": "e5122b5645a40f56adaa69458e8ede60270f742f"
}

```

#### Login / Requesting Token

For Login of the users we have to create a POST request  to the `/api/account/login` which can be easily understandable by the following process.

```
POST http://127.0.0.1:8000/api/account/login

POST Data - 
{
	"username" : "sample@sample.com",
	"password" : "some_password"
}

Response - 

{
    "response": "Successfully authenticated.",
    "pk": 3,
    "email": "sample@sample.com",
    "token": "e5122b5645a40f56adaa69458e8ede60270f742f"
}
```

#### Properties of Users Account

To get the Properties of the user account we have to create a GET request with the Token of the user account as the Headers.

```
GET http://127.0.0.1:8000/api/account/properties

Headers - 

{
	"Authorization" : "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

Response  -

{
    "pk": 3,
    "email": "sample@sample.com",
    "username": "sample@sample.com"
}
```

#### Update Properties of User Account

To Update the properties of the User Account the user must be successfully authenticated that is passing the Token as Header and then user will get access to update properties.

```
PUT http://127.0.0.1:8000/api/account/properties/update

Headers

{
	"Authorization" : "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

POST Data  - 

{
	"pk"          : "3",
	"email"       : "sample@sample.com",
	"username"    : "sample@sample.com"
}

Response  - 

{
    "response": "Account update success"
}
```

#### Change Password of User Account

Changing Password is a essential task of the creation of any service. To change password of any user account please following things

```
PUT http://127.0.0.1:8000/api/account/change_password

Headers  - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

PUT Data  - 

{
	"old_password"          : "some_password",
	"new_password"          : "some_new_password",
	"confirm_new_password"  : "some_new_password"
}

Response  - 

{
    "response": "successfully changed password"
}
```

### Events

Events are generally the timed scheduled process which is used to happen in which multiple/single entities can be involved. So to manage various module We can use this REST API to schedule the Events and manage any Team or people with this API because this API is flexible of Scheduling Events only when both users have the free time.

Events Model will have following properties - 

```python
    title          = CharField(max_length=50,null=False,blank=False)
    description    = TextField(max_length=7000,null=True,blank=True)
    slug           = SlugField(unique=True,auto_created=True)
    start_time     = DateTimeField()
    end_time       = DateTimeField()
    attendees      = IntegerField(default=10)
    private        = BooleanField(default=False)
    organizer 	   = ForeignKey(settings.AUTH_USER_MODEL)
```

#### List All Public Events

To View / List all the Public Events user must be successfully authenticated / must pass Token of the user as Header in the request. To get all the Public Event follow following command.

```
GET http://127.0.0.1:8000/api/event/list

Header - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

Response - 

{
    "count": 3,
    "next": null,
    "previous": null,
    "results": [
        {
            "title": "Sample Event",
            "description": "This Should be under 50 words such that there is no issue. ",
            "start_time": "2020-10-12T10:12:00Z",
            "end_time": "2020-10-12T12:12:00Z",
            "attendees": 10,
            "private": false,
            "slug": "sample-event-639986198"
        }
    ]
}
```

#### Invite User in Event

In this request we generally invite a user to a event using the slug of the event. This Request can be viewed as following.

```
POST http://127.0.0.1:8000/api/event/invite/<str:slug>

Headers  - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

POST Data - 

{
	"username" : "sample@sample.com"
}


Response - 

{
	"response"  : "Success"
}
```

#### Accept Invites of Event

On this url we can request in two types that is GET and POST. In GET request we get all the list of the invites of the events to that user whereas in POST request we post slug of a event in which we accept the invite of event. If there is no event scheduled at that time then event invite is accepted.

```
GET http://127.0.0.1:8000/api/event/accept_invite

Headers - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

Response - 

[
    {
        "title": "Sample Event",
        "description": "This Should be under 50 words such that there is no issue. ",
        "start_time": "2020-10-12T10:12:00Z",
        "end_time": "2020-10-12T12:12:00Z",
        "attendees": 10,
        "private": false,
        "slug": "sample-event-639986198"
    }
]
```

```
POST http://127.0.0.1:8000/api/event/accept_invite

Headers  - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

POST Data  -

{
	"slug"   :  "sample-event-639986198"
}

Response - 

{
    "response": "You have already Scheduled Events in this time !"
}
```

#### Create Event

To Create Event we have to pass all the required fields as POST Data to create new event which can be done as follows - 

```
POST http://127.0.0.1:8000/api/event/create

Headers - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

POST Data - 

{
	"title"           : "Sample Event",
	"description"     : "This will be more than 50 characters",
	"start_time"      : "2020-10-5 10:12",
	"end_time"        : "2020-10-5 10:24",
	"attendees"       : "20"
}

Response - 

{
    "success": true
}
```

#### Delete Event

To Delete any event we can use the following URL `/api/event/delete/<str:slug>` which can be explained in detail as follows 

```
DELETE http://127.0.0.1:8000/api/event/delete/<str:slug>

Headers - 

{
	"Authorization"  :  "Token e5122b5645a40f56adaa69458e8ede60270f742f"
}

Response - 

{
	"response"   : "DELETE SUCCESS"
}
```



## Screenshots & Video

Screenshots of all types of request can be found [here](https://github.com/arch888/MiStay_REST/tree/master/screenshots) and the Video of the tutorial can be found [here](https://youtu.be/88pZ-NUW1V4).

> Feel free to reach out to me via email. Shoot your doubts at [dwevediar@gmail.com](mailto:dwevediar@gmail.com)



## Thank You !

