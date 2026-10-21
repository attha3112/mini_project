class Invalidlogerror(Exception):
    """Data yang dimasukkan tidak valid"""
    pass

class Wronglogerror(Exception):
    """Username atau password salah"""
    pass

class DataLogError(Exception):
    """Username belum ada harap register terlebih dahulu"""
    pass

class AvailLogError(Exception):
    """username sudah ada harap pakai username lain"""
    pass

class PassLogError(Exception):
    """Minimal Panjang password 8 Karakter"""
    pass