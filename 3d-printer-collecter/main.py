from sql import sql
import time
from printer_calls import PrinterCalls
from printer_api import printer_api

# Starts the data collection process
printer=PrinterCalls()
sql=sql()
calls=printer_api(printer,sql)
# Writes data to sql
calls.write_data()
# Writes new data every 10 seconds
sleep=True
while sleep == True:
    time.sleep(10)
    calls.write_data()