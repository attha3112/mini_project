from database import user_data
from exception import Invalidlogerror, Wronglogerror, DataLogError

class data:
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password

class login:
    def __init__(self, log_data):
        self.data = log_data

    def valid_proc(self, nama):
        if nama == '':
            raise Invalidlogerror('Data yang diinput tidak valid')

    def check_proc(self,nama, password):
        self.valid_proc(nama)
        for d in self.data:
            if d['nama'] == nama:
                if d['password'] != password:
                    raise Wronglogerror('username atau password salah')
                return f'Login berhasil'
        raise DataLogError('username tidak ditemukan')

log_process = login(user_data)