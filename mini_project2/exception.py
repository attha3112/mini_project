class Invalidlogerror(Exception):
    """Data yang dimasukkan tidak valid"""
    pass

class Wronglogerror(Exception):
    """Username atau password salah"""
    pass

class DataLogError(Exception):
    """Username belum ada harap register terlebih dahulu"""
    pass