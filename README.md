# Flask MongoDB API
## Description
A test REST API Flask server for CRUD operations in MongoDB. This application will accept HTTP requests to several routes and respond to those requests with either a Create, Read, Update, or Delete (CRUD) operation from the connected MongoDB database.

## How to install and run this application
Make sure Python is installed in your system. Navigate to the express-mongodb-api folder and use terminal to run the following command to build the application:

```bash
pip install -r requirements.txt
```

Once the application is built, run the application using the following command:

```bash
python src/main.py
```

## The Database
The connected MongoDB database consistes of a collection ```users``` which contains documents with the following schema:

```
{
    first_name: STRING
    last_name:  STRING,
    email:  STRING,
    age: INTEGER,
    interest: [
        {
            name:  STRING,
            priority:  STRING
        }
    ]
}
```

All data outputted from this application will follow the above format as a JSON object.

## Routes
The following are the list of routes and HTTP requests that can be sent to perform CRUD operation on the database:

|     Routes       |     HTTP   Method    |     Description                           |
|------------------|----------------------|-------------------------------------------|
|     /user        |     POST             |     Create a new user data                |
|     /user        |     GET              |     Display all user data                 |
|     /user        |     DELETE           |     Delete all user data                  |
|     /user/:id    |     GET              |     Display a user data specified by id   |
|     /user/:id    |     PUT              |     Update a user data specified by id    |
|     /user/:id    |     DELETE           |     Delete a user data specified by id    |

### Notes
- The id of a user data can be found by sending a GET request to ```/user```. Copy the ID on top of the document and paste it to the address bar of the request in order to access the last three routes of the above table
-- Example:
```
http://localhost:3000/user/60e3bcb8d5f9a8002283f201
```
- For POST requests, input the new user data with the specified schema above inside the BODY of the POST request
-- Example:
```
{
    "first_name": "Ibrahim",
    "last_name": "Fadhil",
    "email": "ibrafdj@gmail.com",
    "age": 23,
    "interest":[
      {
        "name": "Gaming",
        "priority": "High"
      },
      {
        "name": "Engineering",
        "priority": "High"
      },
      {
        "name": "Politics",
        "priority": "Medium"
      }
    ]
}
```
- For PUT requests, input only the properties to be updated inside the BODY of the POST request 
-- Example:
```
{
  "age": 24
}
```

## Remote API
This API is available online hosted on Heroku at https://express-mongodb-api-test.herokuapp.com/
