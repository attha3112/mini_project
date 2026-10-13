from database import user_data
from exception import Invalidlogerror, AvailLogError, PassLogError


class reg_database:
    def __init__(self, nama, password):
        self.nama = nama
        self.password = password

class register:
    def __init__(self, reg_database):
        self.reg_database = reg_database

    def validation_proc (self, nama):
        if nama == '':
            raise Invalidlogerror ('Data yang diinput tidak valid')

    def check_proc(self, nama, password):
        self.validation_proc(nama)
        for r in self.reg_database:
            if r['nama'] == nama:
                if len(password) <= 8:
                    raise AvailLogError('username sudah terpakai')
                return f'Login Berhasil'
        raise PassLogError('password minimal 8 karakter')

    #def check_password(self, password):
       #if len(password) <= 8:
           #raise PassLogError('password minimal 8 karakter')
       


reg_proc = register(user_data)