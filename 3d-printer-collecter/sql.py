import pymysql

class sql:
    def __init__(self):
        server = 'localhost'
        database = 'printer'
        user = 'root'

        # database connection
        conn = pymysql.connect(host=server, user=user, db=database)
        if (conn):
            print('Connection to MySQL database', database, 'was successful!')
        self.cursor = conn.cursor()
        conn.autocommit(True)
        self.sql='INSERT INTO job_history VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        self.updatesql1='UPDATE job_history SET endtime=%s WHERE starttime=%s'
        self.updatesql2 = 'UPDATE job_history SET time_elapsed=%s WHERE starttime=%s'
        self.updatesql3 = 'UPDATE job_history SET status=%s WHERE starttime=%s'
    def updatesql(self,type,data,starttime):
        if type=='endtime':
            self.cursor.execute(self.updatesql1,(data,starttime))
        if type=='time_elapsed':
            self.cursor.execute(self.updatesql2, (data, starttime))
        if type=='status':
            self.cursor.execute(self.updatesql3, (data, starttime))
        else:
            return

    def insertsql(self,printer,filename,starttime,endtime,timeelapsed,status,ext1,ext2,bed):
        self.cursor.execute(self.sql,(printer,filename,starttime,endtime,timeelapsed,status,ext1,ext2,bed))
    def exists(self,starttime):
        self.cursor.execute('select count(1) from job_history where starttime="' + starttime + '";')
        filein=self.cursor.fetchone()[0]
        return filein
    def query(self):
        self.cursor.execute('SELECT * FROM job_history;')
        row = self.cursor.fetchone()
        results = []
        while row:
            results.append({'filename': row[1],
                            'details': {'printer': row[0], 'starttime': row[2], 'endtime': row[3],
                                        'time_elapsed': row[4], 'status': row[5], 'ext1_temp':row[6],
                                        'ext2_temp':row[7],'bedtemp':row[8]}})
            row = self.cursor.fetchone()
        results.reverse()
        return results