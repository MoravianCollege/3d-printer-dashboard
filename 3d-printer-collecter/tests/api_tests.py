import unittest
import api
import json
from mocksql import sql



class Testapi(unittest.TestCase):
    def setUp(self):
        api.app.testing = True
        SQL=sql()
        api.sql=SQL
        self.app = api.app.test_client()


    def test01_no_job(self):
        results = self.app.get('/get_jobs')
        result = json.loads(results.data)
        self.assertEqual([], result)


    def test02_one_job(self):
        api.sql.insertsql('gutenberg','ball.text','10:10','12:10','10','success')
        results=self.app.get('/get_jobs')
        result=json.loads(results.data)
        self.assertEqual([{'filename': 'ball.text',
                           'details': {'printer': 'gutenberg', 'starttime': '10:10', 'endtime': '12:10','time_elapsed':'10', 'status': 'success'}}],result)

    def test03_multiple_jobs(self):
        api.sql.insertsql('gutenberg', 'ball.text', '10:10', '12:10', '10', 'success')
        api.sql.insertsql('xerox', 'basket', '10:10', '12:10', '15', 'printing')
        results=self.app.get('/get_jobs')
        result=json.loads(results.data)
        self.assertListEqual([
    {'filename': 'ball.text',
    'details': {
        'printer': 'gutenberg',
        'starttime': '10:10',
        'endtime': '12:10',
        'time_elapsed': '10',
         'status': 'success'
    }
     },
  {
    'filename': 'basket',
    'details': {
      'printer': 'xerox',
      'starttime': '10:10',
      'endtime': '12:10',
      'time_elapsed':'15',
      'status': 'printing'
    }
  }
],result)

    def test04_update(self):
        api.sql.insertsql('gutenberg', 'ball.text', '10:10', '12:10', '10', 'success')
        api.sql.insertsql('xerox', 'basket', '10:15', '12:10', '15', 'printing')
        results = self.app.get('/get_jobs')
        result = json.loads(results.data)
        self.assertListEqual([
                {'filename': 'ball.text',
                 'details': {
                     'printer': 'gutenberg',
                     'starttime': '10:10',
                     'endtime': '12:10',
                     'time_elapsed': '10',
                     'status': 'success'
                 }
                 },
                {
                    'filename': 'basket',
                    'details': {
                        'printer': 'xerox',
                        'starttime': '10:15',
                        'endtime': '12:10',
                        'time_elapsed': '15',
                        'status': 'printing'
                    }
                }
            ], result)
        api.sql.updatesql('time_elapsed', '150', '10:15')
        results = self.app.get('/get_jobs')
        result = json.loads(results.data)
        self.assertListEqual([
            {'filename': 'ball.text',
             'details': {
                 'printer': 'gutenberg',
                 'starttime': '10:10',
                 'endtime': '12:10',
                 'time_elapsed': '10',
                 'status': 'success'
             }
             },
            {
                'filename': 'basket',
                'details': {
                    'printer': 'xerox',
                    'starttime': '10:15',
                    'endtime': '12:10',
                    'time_elapsed': '150',
                    'status': 'printing'
                }
            }
        ], result)


