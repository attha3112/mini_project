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

    def log_proc(self, nama, password):
        self.valid_proc(nama)
        for d in self.data:
            # Cek apakah nama dan password cocok dengan data yang sedang dibaca
            if d['nama'] == nama and d['password'] == password:
                return 'Login berhasil!'
            
    # Jika perulangan selesai sampai habis dan tidak ada yang cocok, baru lempar error
        raise Wronglogerror('username atau password salah')
log_process = login(user_data)