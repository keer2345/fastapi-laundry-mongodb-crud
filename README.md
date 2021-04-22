**[Build A Laundry CRUD API with FastAPI using MongoDB](https://dev.to/totoolakehinde/build-a-laundry-crud-api-with-fastapi-using-mongodb-1-3ccl)**

- [Basic CRUD in a Laundry API](#basic-crud-in-a-laundry-api)
- [Installing FastAPI](#installing-fastapi)
- [Setting up MongoDB Atlas](#setting-up-mongodb-atlas)
- [Connect MongoDB Database](#connect-mongodb-database)
- [Building each API Endpoints](#building-each-api-endpoints)
## Basic CRUD in a Laundry API
- Login
- signup
- update-profile
- book-service
- update-pickup

## Installing FastAPI
``` sh
python3.9 -m venv .venv
source .venv/bin/activate

pip install fastapi
pip install uvicorn
```

`main.py`:
``` python
import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8000,
    )
```
Let's run and test our API with `uvicorn main:app --reload` or `python main.py`:
``` sh
python main.py
INFO:     Uvicorn running on http://0.0.0.0:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [45020] using statreload
INFO:     Started server process [45022]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

## Setting up MongoDB Atlas
- Signup for a free MongoDB cloud storage [here](https://www.mongodb.com/cloud/atlas/signup)
- After signup, create a project, name it *laundrystore*.
- Click build a cluster to create an Atlas:free atlas! *New clusters take 1-3 minutes to provision*.
- After the cluster has been created, click on *connect* for details on how to connect your cloud storage to your app!
- Set your cloud storage access permissions to allow *connection from anywhere*!
- Set a database *username* and *password*, and choose a connection method! For example: mongo / mongo123456 .

## Connect MongoDB Database
``` sh
pip install motor
```

create a `settings.py` file and type the following code:
``` python
mongodb_uri = 'mongodb+srv://mongo:mongo123456@cluster0.ugtyx.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
port = 8000
```
Create a file `connection.py`, This is basically a connection file that creates a connection with MongoClient! Also, a database called *usersdata*:
``` python
client = motor.motor_asyncio.AsyncIOMotorClient(settings.mongodb_uri)
db = client['usersdata']
```

Update our `main.py` file:
## Building each API Endpoints
[Schematics](https://schematics.readthedocs.io/en/latest/) is a Python library to combine types into structures, validate them, and transform the shapes of your data based on simple descriptions.
``` sh
pip install schematics
```
