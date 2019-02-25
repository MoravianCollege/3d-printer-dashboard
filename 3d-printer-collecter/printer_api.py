from sql import sql
import time
from printer_calls import PrinterCalls
class printer_api:
    def __init__(self,printer,sql):
        self.sql=sql
        self.printer=printer
    # writes data for both printers to sql database
    def write_data(self):
            self.gutenbergdata = self.printer.get_job_info('155')
            self.xeroxdata = self.printer.get_job_info('44')

            if self.gutenbergdata != "":
                filein=self.sql.exists(self.gutenbergdata[1])
            # if printer exists then just update sql, if printer doesn't exist add stats to sql
                if filein==1:
                    self.sql.updatesql('endtime',self.gutenbergdata[2],self.gutenbergdata[1])
                    self.sql.updatesql('time_elapsed',self.gutenbergdata[4], self.gutenbergdata[1])
                    if self.gutenbergdata[3]=='wait_cleanup':
                        self.sql.updatesql('status','finished', self.gutenbergdata[1])
                    else:
                        self.sql.updatesql('status',self.gutenbergdata[3], self.gutenbergdata[1])

                if filein==0:
                    self.sql.insertsql('gutenberg',self.gutenbergdata[0],self.gutenbergdata[1],self.gutenbergdata[2],
                                       self.gutenbergdata[4],self.gutenbergdata[3],self.gutenbergdata[5],
                                       self.gutenbergdata[6],self.gutenbergdata[7])

            if self.xeroxdata != "":
                filein = self.sql.exists(self.xeroxdata[1])

            # if printer exists then just update sql, if printer doesn't exist add stats to sql
                if filein == 1:
                    self.sql.updatesql('endtime', self.xeroxdata[2], self.xeroxdata[1])
                    self.sql.updatesql('time_elapsed', self.xeroxdata[4], self.xeroxdata[1])
                    if self.xeroxdata[3] == 'wait_cleanup':
                        self.sql.updatesql('status', 'finished', self.xeroxdata[1])
                    if self.xeroxdata[3] == 'wait_user_action':
                        self.sql.updatesql('status', 'cancelled', self.xeroxdata[1])
                    else:
                        self.sql.updatesql('status', self.xeroxdata[3], self.xeroxdata[1])

                if filein == 0:
                    self.sql.insertsql('xerox', self.xeroxdata[0], self.xeroxdata[1], self.xeroxdata[2],
                                       self.xeroxdata[4], self.xeroxdata[3],self.xeroxdata[5],
                                       self.xeroxdata[6], self.xeroxdata[7])




