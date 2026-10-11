class Invalidlogerror(Exception):
    """Memicu error saat invalid tentang data"""
    pass

class Wronglogerror(Exception):
    """Memicu error saat Username atau password tidak sesuai"""
    pass

class Minimumlogerror(Exception):
    """Minimal Password 8 Karakter"""
    pass