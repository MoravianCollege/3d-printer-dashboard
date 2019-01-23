from sql import sql
import time
from printer_calls import PrinterCalls
from printer_api import printer_api

printer=PrinterCalls()
sql=sql()
calls=printer_api(printer,sql)
calls.write_data()
sleep=True
while sleep == True:
    time.sleep(20)
    calls.write_data()