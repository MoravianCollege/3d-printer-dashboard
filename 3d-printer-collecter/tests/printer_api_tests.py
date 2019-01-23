import unittest
from printer_api import printer_api
from mockprinter import mockPrinter
from mocksql import sql
import json
import threading




class test_printer_api(unittest.TestCase):


    def test_idle(self):
        printer = mockPrinter("idle")
        SQL=sql()
        printer.set_info('155','2017-12-03T23:58:20','2017-12-03T23:56:20', 'printing', 'X_small-planter-reservoir','10','10','10','10')
        printerapi=printer_api(printer,SQL)
        printerapi.write_data()
        self.assertEqual(printerapi.gutenbergdata,"")

    def test_set(self):
        printer = mockPrinter("printing")
        SQL = sql()
        printer.set_info('155','2017-12-03T23:58:20','2017-12-03T23:56:20', 'printing', 'X_small-planter-reservoir','10','10','10','10')
        printerapi = printer_api(printer, SQL)
        printerapi.write_data()
        self.assertEqual(printerapi.gutenbergdata,(['gutenberg','X_small-planter-reservoir','2017-12-03T23:58:20','2017-12-03T23:56:20','10','printing','10','10','10']))