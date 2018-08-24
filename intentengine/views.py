from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login, authenticate
from nltk.corpus import stopwords
from IntentProcessing import IntentProcessor as IP
from intentengine.models import branchxmlfiles, provisioningstatus
from IntentProcessing import UCDT
import xml.etree.ElementTree as ET
import random

# Create your views here.
randnum= random.randint(500,1500)
useCaseError = 'Currently allowed actions are: "associate","remove","create","delete","add","provision","create" \n Please contact your administrator for assistance with your use case'
sentenceError = 'Please input more than one word'

def login(request):
    return render(request, 'login.html',{})

@csrf_exempt
def enterIntent(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(request, username=username,password=password)
    #print(user,username,password)

    if user is not None:
        if user.is_active:
            login(request)
            return render(request, 'Intent.html',{})
        else:
            return HttpResponse('Disabled')
    else:
        return HttpResponse('Incorrect credentials, please contact your system administrator')

@csrf_exempt
def submit(request):
    # User Intent
    intent = request.POST.get('Intent')
    updatemodel, created = provisioningstatus.objects.update_or_create(intent=intent)
    pkid = updatemodel.pkid
    request.session['pkid'] =pkid
    #print('pkid',pkid)

    #print(intent)
    #print(type(intent))
    # List of words in user intent

    try:
        inpstr = intent.split(' ')
    except AttributeError:
        return HttpResponse(sentenceError)
    # Set of stopwords in English
    ToRemove = set(stopwords.words('english'))

    # Remove stopwords to get set of keywords
    keywrds = list(filter(lambda x: x not in ToRemove, list(map(lambda x: x.lower(), inpstr))))
    keywrds = list(map(lambda x: x.replace(' ', ''), keywrds))
    #print (keywrds,type(keywrds))

    action = IP.findverb(keywrds)
    #print(action,type(action))

    entities = IP.findentities(keywrds)
    #print(entities)

#Get template/script mappings
    if type(action) is str:
        try:
            #print(action, type(action))
            if action in ('associate','update'):
                finalaction = 'update'
                st = IP.updateapimapping(entities)
            elif action in ('remove', 'delete'):
                finalaction = 'remove'
                st = IP.removeapimapping(entities)
            elif action in ('add', 'provision', 'create'):
                finalaction = 'provision'
                #print('Here')
                st = IP.provisionapimapping(entities)
                #print(api, type(api))
            else:
                return HttpResponse(useCaseError)
        except Exception as e:
            return HttpResponse(e)
    else:
        return HttpResponse(useCaseError)

    templateId = st[1]

#for provisioning, get list of mandatory parameters
    if finalaction == 'provision':
        requireddata= list(IP.mandatoryoperands(st))

        for i in range(len(inpstr)-len(requireddata)*2+1):
            try:
                requireddata.append(inpstr[inpstr.index(requireddata[-1])+2])
            except Exception:
               pass
        print('Required Data:', requireddata)
        config={}
        for field in requireddata:
            try:
                config[field] = inpstr[inpstr.index(field) + 1]
            except ValueError:
                return HttpResponse("Required field value %s not provided" %(field))
        #print(config)

#for removing, continue to UCDT execution
    elif finalaction == 'remove':
        config[entities[0]] = inpstr[inpstr.index(entities[0] + 1)]

#for update, get which parameters to update
    elif finalaction == 'update':
        pass

    else:
        HttpResponse(useCaseError)

#send to UCDT
    branchcreatetemplate = ('<branch><branchName>%s%s</branchName></branch>' % (finalaction, randnum))
    branchxml = branchxmlfiles.objects.get(template=templateId).xml
    #print(branchxml, type(branchxml))
    root = ET.fromstring(branchxml)
    for key in config:
        try:
            root[0][0].find(key).text = config.get(key)
        except:
            return HttpResponse('You\'ve added parameters that are not currently configurable. Please contact your administrator')
    branchdataxml = ET.tostring(root, method='xml').decode('utf-8')

    branchId = UCDT.createBranch(branchcreatetemplate)
    stat = UCDT.addServerToBranch(branchId)
    #print('add server status'+str(stat))
    datastatus = UCDT.addDatatoBranch(branchdataxml, branchId, templateId)
    #print ('Add Data STatus'+ str(datastatus))

    pURL, provisionId = UCDT.provisionBranch(templateId, branchId)
    obj = provisioningstatus.objects.filter(pkid=request.session.get('pkid')).update(provisionTaskId=provisionId)
    #print(provisionId)
    request.session['provisioningurl']=pURL
    request.session['provisionId']=provisionId
    return render(request,'SentToProvision.html',{})


def status(request):
    provisioningurl = request.session.get('provisioningurl')
    pid = request.session.get('provisionId')
    return render(request,'status.html',{'purl':provisioningurl,'pid': pid})