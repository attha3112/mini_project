from fastapi import FastAPI
import signin
import reg
import exception



app = FastAPI(title='Login & Register')
#SIGN IN PROC
sing_proc = signin.login
#REGISTER PROC
regist = reg.register


@app.post("/")
def home():
    return ('Login & Register')

@app.post('/login')
def checkvalid():
    

