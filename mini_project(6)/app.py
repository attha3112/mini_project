import signin
import reg
from fastapi import FastAPI, Body
from exception import Invalidlogerror, DataLogError
from pydantic import BaseModel
from database import user_data

#set fastapi
app = FastAPI(title='Login & Register')

#SIGN IN PROC
signin_proc = signin.login(user_data)

#REGISTER PROC
register_proc = reg.register(user_data)

class userlog_reg(BaseModel):
    nama : str
    password : str

@app.get("/")
def home():
    return {'status' : 'online', 'messages' : 'Login & register API'}


@app.post("/login")
def api_signin(data : userlog_reg):
    try:
        signin_proc.log_proc(data.nama, data.password)
        return{'status' : 'succes', 'messages' : 'login berhasil'}

    except Exception as e:
        print(f'error aslinya adalah {e}')
        raise e

    

@app.post('/register')
def api_register(data: userlog_reg):
    try:
        register_proc.main_proc(data.nama, data.password)
        return{'status' : 'success', 'messages' : 'Register berhasil'}

    except Exception :
        raise DataLogError('register gagal')