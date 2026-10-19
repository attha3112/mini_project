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

    def check_proc(self, nama):
        self.validation_proc(nama)
        for r in self.reg_database:
            if r['nama'] == nama:
                raise AvailLogError('username sudah terpakai')
        return None

    def check_pw(self, nama, password):
        self.check_proc(nama)
        if len(password) <= 8:
            raise PassLogError('Password minimal 8 Karakter')

        new_acc = {'nama' : nama, 'password' : password}
        self.reg_database.append(new_acc)
        return f'Akun berhasil ditambahkan'

reg_proc = register(user_data)