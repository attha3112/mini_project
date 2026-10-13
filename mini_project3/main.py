from database import user_data
from exception import Invalidlogerror, Wronglogerror, DataLogError
from signin import log_process, login
from reg import reg_proc, register

print(reg_proc.check_proc ('attha', 'attha123'))
