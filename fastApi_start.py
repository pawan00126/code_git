from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        'Author' : 'Pawan Bhati',
        'message' : 'hello visitor, new here ? welcome....'
    }


@app.get("/user")
def format_user():
    return {
        'Author' : 'Pawan Bhati',
        'Message' : 'Just for new API endpoint , No worry for this :)'
    }


@app.get("/greet")
def greet():
    return {
        'Author' : 'pawan00126',
        'message' : 'I am welcoming yoU here ... :)'
    }

@app.post("/")
def user_format(name:str, age:int):
    return {
        'Author' :'pawan00126',
        'message' : f'hello {name}, you entered this age : {age}'
    }
