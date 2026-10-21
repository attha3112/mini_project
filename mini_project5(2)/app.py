import signin
import reg
from fastapi import FastAPI
from exception import Invalidlogerror, DataLogError

#set fastapi
app = FastAPI(title='Login & Register')

#SIGN IN PROC
signin_proc = signin.login

#REGISTER PROC
register_proc = reg.register



@app.post("/")
def home():
    return ('Login & Register')


@app.post("/login")
def api_signin(nama, password):
    try:
        signin_proc.check_proc(nama, password)
        return{'status' : 'succes', 'messages' : 'login berhasil'}

    except Exception:
        raise Invalidlogerror('data tidak valid')

    

@app.post('/register')
def api_register(nama, password):
    try:
        register_proc.main_proc(nama, password)
        return{'status' : 'success', 'messages' : 'Register berhasil'}

    except Exception :
        raise DataLogError('register gagal')