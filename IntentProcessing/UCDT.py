import requests
from requests.auth import HTTPBasicAuth
import random

auth = HTTPBasicAuth(username='restUser', password='Cisco123!')
ucdt_url = 'https://localhost:8443/UCSPT-CE/rest/ucdt'
headers = {'Content-Type': 'application/xml'}

def createBranch(branchxml):

    r = requests.post(url=ucdt_url + '/enterprise/16/branch', verify=False, auth=auth, data=branchxml, headers=headers)
    rcreateb = r.json()
    branchdetails = rcreateb['object']
    branchId = branchdetails['branchId']
    #print ('create url:',rcreateb.url)
    return (branchId)

def addServerToBranch(branchId):
    r = requests.get(url=ucdt_url+'/enterprise/16/branch/'+str(branchId)+'/assignServer/1', verify=False,auth=auth)
    #print('add server url:',r.url)
    return r.status_code

def addDatatoBranch(branchdataxml,branchId,templateId):
    r = requests.post(url=ucdt_url+'/template/'+str(templateId)+'/branch/'+str(branchId)+'/data',verify=False,auth=auth,headers=headers, data=branchdataxml)
    #print('Add data URL: ',r.url)
    #print (r.text)
    return r.status_code

def provisionBranch(templateId,branchId):
    r = requests.get(url=ucdt_url+'/template/'+str(templateId)+'/branch/'+str(branchId)+'/provision',verify=False,auth=auth)
    rdata = r.json()
    provisionId=rdata['object']['provisionTaskId']

    #print(provisionId)
    return r.url,provisionId

