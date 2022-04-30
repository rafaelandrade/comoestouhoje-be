## Como estou hoje

-----------

## About:

Microservice responsible for deal with services that try to identify you salary based
on the location where each person is born.

----

## How to install:

First of all, one thing that not that important but make a difference is
the installation and creation of virtual environment in you machine, using venv. That
basically is a tool to create isolated Python environment.

For venv, basically what you need to do is:

```bash
 - Install the virtualenv package
pip install virtualenv

- After that, create virtual environment
virtualenv ANY_NAME_THAT_YOU_WANT

- For finish just need to activate the virtual environment
source ANY_NAME_THAT_YOU_WANT/bin/activate

- If you want to deactivate the virtual environment
deactivate
```

Obs:. If you want read the official documentation can be found [here](https://virtualenv.pypa.io/en/latest/).

---

## Getting started

It is recommended that start the service using Docker, it is more easily and faster. So, the first step is
install docker, you can find all the information about that on the [website](https://docs.docker.com/get-docker/).

After have docker on your machine, just need to run the follow code: 

```bash
docker-compose up
```

After finish the service should be running. Any doubt you can send a message to Contributors or create a issue.

### Second option to initiate the service

It is also possible to execute in other way, that is:

```
# First have to install all requirements running #
pip3 install -r requirements.txt

# After all requirements installed just need to run the uvicorn code #
uvicorn app.main:app --host 0.0.0.0 --reload --port 5000
```