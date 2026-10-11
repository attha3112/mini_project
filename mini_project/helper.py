from database import user_data
from exception import Invalidlogerror, Wronglogerror, Minimumlogerror

class data:
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password

class login:
    def __init__(self, log_data):
        self.data = log_data

    def log_proc(self, nama, password):
        for log in self.data:
            if log['nama'] != nama:
                raise Invalidlogerror(f'format tidak valid')
            return (f'Login berhasil')

    def log_pass(self, username, password):
        for log in self.data:
            if log['password'] != password:
                raise Wronglogerror (f'username atau password salah')
            return (f'Login berhasil')
    
    def min_pass(self, username, password):
        for log in self.data:
            if log['nama'] == username:
                if len(password) < 8:
                    raise Minimumlogerror('Minimal password 8 karakter')
                return f'Login berhasil'
        raise Wronglogerror('Username tidak ditemukan')


log_process = login(user_data)