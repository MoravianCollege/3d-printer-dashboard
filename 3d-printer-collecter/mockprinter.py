class mockPrinter:
    def __init__(self,status):
        self.info=[]
        self.status=status
    def get_status(self):
        return self.status
    def get_job_info(self,printer_number):
        if self.get_status() == "idle":
            return ""
        else:
            return self.info
    def set_info(self,printer_number,datetime_started,datetime_finished,status,name,time_elapsed,ext1,ext2,bed):
        if printer_number=="155":
            self.info.append('gutenberg')
        if printer_number=="44":
            self.info.append('xerox')
        self.info.append(name)
        self.info.append(datetime_started)
        self.info.append(datetime_finished)
        self.info.append(time_elapsed)
        self.info.append(status)
        self.info.append(ext1)
        self.info.append(ext2)
        self.info.append(bed)

