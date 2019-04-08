import requests
import json
from datetime import timezone

class PrinterCalls:

    # returns current status of a specified printer
    def get_status(self,printer_number):
        status=[]
        status.append(requests.get('http://172.31.228.'+printer_number+'/api/v1/printer/status'))
        status.append(status[0].text)
        return status

    # returns current data for a specified printer
    def get_job_info(self, printer_number):
        if self.get_status(printer_number)[1] == '"idle"':
            return ""
        if self.get_status(printer_number)[1] == '"maintenance"':
            return ""
        else:
            info = requests.get('http://172.31.228.'+printer_number+'/api/v1/print_job')
            info = json.loads(info.text)
            results = []
            results.append(info["name"])
            datestart = info['datetime_started']
            results.append(datestart)
            results.append(info["datetime_finished"])
            results.append(info["state"])
            time_elapsed=info['time_elapsed']
            results.append(time_elapsed)
            info = requests.get('http://172.31.228.'+printer_number+'/api/v1/printer')
            info = json.loads(info.text)
            results.append(info['heads'][0]['extruders'][0]['hotend']['temperature']['current'])
            results.append(info['heads'][0]['extruders'][1]['hotend']['temperature']['current'])
            results.append(info['bed']['temperature']['current'])

            return results

