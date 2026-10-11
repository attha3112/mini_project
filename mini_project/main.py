from database import user_data
from exception import Invalidlogerror, Wronglogerror, Minimumlogerror
from helper import log_process, login

print(log_process.log_proc('attha' , 'attha123'))
print(log_process.min_pass('attha', 'attha123'))   # password 8 karakter → OK
print(log_process.min_pass('kartika', 'kartika'))  # password 7 karakter → ERROR
