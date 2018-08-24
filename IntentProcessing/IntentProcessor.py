

def findverb(wordlist):
    #Define all allowed actions
    try:
        AllActions = ('associate', 'add', 'remove', 'update', 'delete','create','provision')
        #print(AllActions)
        for word in wordlist:
            if word in AllActions:
                #print(str(word))
                return str(word)
    except:
        return('Currently allowed actions are: "associate","remove","create","delete","add","provision","create" \n Please contact your administrator for assistance with your use case')

#def translator(action):
#    return entitymapping.get(action)

def findentities(entlist):
    #Universal set of all possible entities
    MasterEntitySet = {'axlerror', 'sipprofile', 'listsipprofile', 'sipprofile', 'sipprofileoptions', 'siptrunksecurityprofile', 'timeperiod', 'timeschedule', 'todaccess', 'voicemailpilot', 'processnode', 'callerfilterlist', 'routepartition', 'routepartition', 'css', 'callmanager', 'callmanager', 'mediaresourcegroup', 'mediaresourcelist', 'region', 'aargroup', 'physicallocation', 'routegroup', 'devicepool', 'devicepool', 'devicemobilitygroup', 'location', 'softkeytemplate', 'softkeytemplate', 'transcoder', 'commondeviceconfig', 'resourceprioritynamespace', 'resourceprioritynamespace', 'resourceprioritynamespacelist', 'resourceprioritynamespacelist', 'devicemobility', 'cmcinfo', 'credentialpolicy', 'facinfo', 'huntlist', 'ivruserlocale', 'linegroup', 'recordingprofile', 'routefilter', 'callmanagergroup', 'usergroup', 'dialplan', 'dialplantag', 'ddi', 'mobilesmartclientprofile', 'processnodeservice', 'mohaudiosource', 'dhcpserver', 'dhcpsubnet', 'callpark', 'directedcallpark', 'meetme', 'conferencenow', 'mobilevoiceaccess', 'routelist', 'user', 'appuser', 'siprealm', 'phonentp', 'datetimegroup', 'presencegroup', 'geolocation', 'srst', 'srst', 'mlppdomain', 'cumaserversecurityprofile', 'applicationserver', 'applicationusercapfprofile', 'endusercapfprofile', 'serviceparameter', 'userphoneassociation', 'geolocationfilter', 'voicemailprofile', 'voicemailprofile', 'voicemailport', 'voicemailport', 'gatekeeper', 'gatekeeper', 'phonebuttontemplate', 'phonebuttontemplate', 'commonphoneconfig', 'messagewaiting', 'ipphoneservices', 'ctiroutepoint', 'ctiroutepoint', 'transpattern', 'transpatternoptions', 'callingpartytransformationpattern', 'siproutepattern', 'huntpilot', 'routepattern', 'applicationdialrules', 'directorylookupdialrules', 'phonesecurityprofile', 'sipdialrules', 'conferencebridge', 'annunciator', 'interactivevoice', 'mtp', 'fixedmohaudiosource', 'aargroupmatrix', 'remotedestinationprofile', 'line', 'line', 'lineoptions', 'defaultdeviceprofile', 'h323phone', 'mohserver', 'h323trunk', 'phone', 'wipephone', 'lockphone', 'phoneoptions', 'h323gateway', 'deviceprofile', 'deviceprofileoptions', 'remotedestination', 'vg224', 'gateway', 'gatewayendpointanalogaccess', 'gatewayendpointdigitalaccesspri', 'gatewayendpointdigitalaccessbri', 'gatewayendpointdigitalaccesst1', 'ciscocatalyst600024portfxsgateway', 'ciscocatalyst6000e1voipgateway', 'ciscocatalyst6000e1voipgateway', 'ciscocatalyst6000t1voipgatewaypri', 'ciscocatalyst6000t1voipgatewayt1', 'ciscocatalyst6000t1voipgatewayt1', 'callpickupgroup', 'routeplan', 'geolocationpolicy', 'siptrunk', 'regionmatrix', 'calledpartytransformationpattern', 'externalcallcontrolprofile', 'safsecurityprofile', 'safforwarder', 'ccdhosteddn', 'ccdhosteddngroup', 'ccdrequestingservice', 'interclusterserviceprofile', 'remotecluster', 'ccdadvertisingservice', 'unitstogateway', 'gatewaysubunits', 'ldapdirectory', 'emccfeatureconfig', 'safccdpurgeblocklearnedroutes', 'vpngateway', 'vpngroup', 'vpnprofile', 'imeserver', 'imeroutefiltergroup', 'imeroutefilterelement', 'imeclient', 'imeenrolledpattern', 'imeenrolledpatterngroup', 'imeexclusionnumber', 'imeexclusionnumbergroup', 'imefirewall', 'imee164transformation', 'transformationprofile', 'fallbackprofile', 'ldapfilter', 'appserverinfo', 'tvscertificate', 'featurecontrolpolicy', 'mobilityprofile', 'enterprisefeatureaccessconfiguration', 'handoffconfiguration', 'calledpartytracing', 'sipnormalizationscript', 'customuserfield', 'gatewaysccpendpoints', 'billingserver', 'lbmgroup', 'announcement', 'serviceprofile', 'ldapsynccustomfield', 'audiocodecpreferencelist', 'ucservice', 'lbmhubgroup', 'importeddirectoryuricatalogs', 'vohserver', 'sdptransparencyprofile', 'featuregrouptemplate', 'dirnumberaliaslookupandsync', 'localroutegroup', 'advertisedpatterns', 'blockedlearnedpatterns', 'ccaprofiles', 'universaldevicetemplate', 'userprofileprovision', 'presenceredundancygroup', 'assignedpresenceservers', 'unassignedpresenceservers', 'assignedpresenceusers', 'unassignedpresenceusers', 'wifihotspot', 'wlanprofilegroup', 'wlanprofile', 'universallinetemplate', 'networkaccessprofile', 'licenseduser', 'httpprofile', 'elingroup', 'secureconfig', 'unassigneddevice', 'registrationdynamic', 'infrastructuredevice', 'ldapsearch', 'wirelessaccesspointcontrollers', 'executesqlquery', 'executesql', 'authenticateuser', 'devicelogin', 'devicelogout', 'devicereset', 'osversion', 'numdevices', 'mobility', 'enterprisephoneconfig', 'ldapsystem', 'ldapauthentication', 'applicationtosoftkeytemplate', 'ccmversion', 'imefeatureconfig', 'fallbackfeatureconfig', 'imelearnedroutes', 'ldapsync', 'ldapsyncstatus', 'softkeyset', 'remotecluster', 'syslogconfiguration', 'phonetypedisplayinstance', 'interclusterdirectoryuri', 'ilsconfig', 'snmpcommunitystring', 'snmpuser', 'snmpmib2list', 'ccdfeatureconfig', 'routepartitionsforlearnedpatterns', 'pagelayoutpreferences', 'assignpresenceuser', 'unassignpresenceuser', 'credentialpolicydefault', 'selfprovisioningchange', 'changedndstatus', 'licenseusage', 'serviceparametersreset', 'enterpriseparametersreset'}
    #print(len(MasterEntitySet))
    return list(set(entlist).intersection(MasterEntitySet))

def removeapimapping(entities):
    mapping = {('user',):('template','TBD'),('phone',):('template','TBD'),('line',):('template','TBD')}
    return mapping.get(sorted(entities))

def provisionapimapping(entities):
    mapping ={('user',):('template',277),('phone','user'):('script','TBD'),('phone',):('template',275),('line',):('template',276)}

    return mapping.get(tuple(sorted(entities)))

def updateapimapping(entities):
    mapping = {('user'):('template','TBD'),('phone'):('template','TBD')}
    return mapping.get(sorted(entities))

def mandatoryoperands(script):
    operanddictionary = {('template',277):('userid','lastname'),('template',275):('type','location'),('template',276):('pattern','routePartitionName')}
    #print(operanddictionary[script])
    return operanddictionary.get(script)



