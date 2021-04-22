import uvicorn
from bson import ObjectId
from fastapi import FastAPI
from schematics.models import Model
from schematics.types import EmailType, StringType
import connection


class User(Model):
    user_id = ObjectId()
    email = EmailType(required=True)
    name = StringType(required=True)
    password = StringType(required=True)


# An instance of class User
newuser = User()


# function to create and assign values to the instance of class User
def create_user(email, username, password):
    newuser.user_id = ObjectId()
    newuser.email = email
    newuser.name = username
    newuser.password = password

    return dict(newuser)


# A method to check if the email parameter exists from the users database before validation of details
# def email_exists(email):
# user_exists = True

# Counts the number of the times the email exists, if it equal 0 .
# It means the email doesn't exists in the database
# if db.users.find({'email': email}).count() == 0:

app = FastAPI()


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.post("/signup/{email}/{username}/{password}")
def singup(email, username: str, password: str):
    user_exists = False
    data = create_user(email, username, password)
    dict(data)

    if connection.db.demo.find({'email': data['email']}).count() > 0:
        user_exists = True
        print("User Exists")
        return {"message": "User Exists"}
    else:
        connection.db.users.insert_one(data)
        return {
            "message": "User Created",
            "email": data["email"],
            "name": data['name'],
            "pass": data['password']
        }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        reload=True,
        port=8000,
    )
