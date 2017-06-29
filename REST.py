from requests import get
from requests import post
from os import path

class REST:

    VNF_ADDRESS = ''

#__init__: gets the VNF instance management info and set the address for RESTfull
#          requests.
    def __init__(self, managementVNF):

        self.VNF_ADDRESS = 'http://' + managementVNF

#getRunning: get request to check if a function is running in VNF.
#            [code, answer] ->
#               code - 200 if normal, other if error
#               answer - True or False
    def getRunning(self):

        if self.VNF_ADDRESS == '':
            return

        response = get(self.VNF_ADDRESS + '/click_plugin/running')
        return [str(response.status_code), response.text]

#getFunction: get the current function in the click file.
#            [code, answer] ->
#               code - 200 if normal, other if error
#               answer - file content.
    def getFunction(self):

        if self.VNF_ADDRESS == '':
            return

        response = get(self.VNF_ADDRESS + '/click_plugin/read_file')
        return [str(response.status_code), response.text]

#getIdentification: get the header of function in click file.
#            [code, answer] ->
#               code - 200 if normal, other if error
#               answer - file header data as a dictionary
    def getIdentification(self):

        if self.VNF_ADDRESS == '':
            return

        response = get(self.VNF_ADDRESS + '/click_plugin/vnf_identification')
        return [str(response.status_code), response.text]

#getMetrics: get VNF metrics such memory and cpu.
#            [code, answer] ->
#               code - 200 if normal, other if error
#               answer - VNF metrics as a dictionary
    def getMetrics(self):

        if self.VNF_ADDRESS == '':
            return

        response = get(self.VNF_ADDRESS + '/click_plugin/metrics')
        return [str(response.status_code), response.text]

#getLog: get the VNF current log file content.
#            [code, answer] ->
#               code - 200 if normal, other if error
#               answer - log file content.
    def getLog(self):

        if self.VNF_ADDRESS == '':
            return

        response = get(self.VNF_ADDRESS + '/click_plugin/log')
        return [str(response.status_code), response.text]

#postStart: start the function according to the click file.
#           code - 200 if normal, other if error
    def postStart(self):

        if self.VNF_ADDRESS == '':
            return

        response = post(self.VNF_ADDRESS + '/click_plugin/start')
        return response.status_code

#postStop: stop the function running.
#           code - 200 if normal, other if error
    def postStop(self):

        if self.VNF_ADDRESS == '':
            return

        response = post(self.VNF_ADDRESS + '/click_plugin/stop')
        return response.status_code

#postFunction: change the content of the click file according to the file path
#              received as argument, it must be a click function.
#              -1 - file does not exist
#              code - 200 if normal, other if error
    def postFunction(self, functionPath):

        if self.VNF_ADDRESS == '':
            return

        if not path.isfile(functionPath):
            return -1

        functionFile = open(functionPath)
        functionData = functionFile.read()

        response = post(self.VNF_ADDRESS + '/click_plugin/write_file?path=func.click&content=' + functionData)
        return response.status_code