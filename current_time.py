from datetime import datetime
import time
def current_time():
    c_time = [time.ctime().split(" ")[0] , time.ctime().split(" ")[3]]
    c_date = str(datetime.now()).split(" ")[0]
    return [c_time[0] , c_time[1] , c_date]

