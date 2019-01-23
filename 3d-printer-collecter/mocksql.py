
class sql:
    def __init__(self):
        self.results=[]
    def updatesql(self,type,data,starttime):
        if type=='endtime':
            for thing in self.results:
                if thing['details']['starttime']==starttime:
                    thing['details']['endtime']=data

        if type=='time_elapsed':
            for thing in self.results:
                if thing['details']['starttime']==starttime:
                    thing['details']['time_elapsed']=data
        if type=='status':
            for thing in self.results:
                if thing['details']['starttime']==starttime:
                    thing['details']['status']=data
        else:
            return

    def insertsql(self,printer,filename,starttime,endtime,timeelapsed,status,ext1,ext2,bed):
        self.results.append(({'filename': filename,
                            'details': {'printer': printer, 'starttime': starttime, 'endtime': endtime,
                                        'time_elapsed': timeelapsed, 'status': status,'ext1':ext1,'ext2':ext2,'bed':bed}}))

    def exists(self,starttime):
        if len(self.results)>0:
            for data in self.results:
                if data['details']['starttime']==starttime:
                    return 1
        return 0
    def query(self):
        return self.results