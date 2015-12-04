##cs361, fall 2015
##project b
##rishi bhandarkar, james carlin, joshua curtis
##robert erick, tyler koistinen, grant nakashima


import bottle
import model_v2

@bottle.route('/')
def home():
    return bottle.template('home')

@bottle.route('/caselawlookup')
def caselawlookup():
    return bottle.template('caselawlookup')

@bottle.post('/docaselawlookup')
def docaselawlookup():
    searchTerm=bottle.request.forms.get("searchTerm")
    state=bottle.request.forms.get("state")
    cases=database.getData('caselaw',state)
    cases=filter(lambda item:item['entryText'].find(searchTerm)>-1,cases)
    return bottle.template('caselawlookupresults',dict(cases=cases))

@bottle.route('/localattorneysearch')
def localattorneysearch():
##    states=database.getList("stateList")
    return bottle.template('localattorneysearch')

##@bottle.post('/docountysearch')
##def docountysearch():
##    searchTerm=bottle.request.forms.get("state")
##    state=database.getState(searchTerm)
##    return bottle.template('countysearchresults',state=state)

@bottle.post('/dolocalattorneysearch')
def dolocalattorneysearch():
    county=bottle.request.forms.get("county")
    state=bottle.request.forms.get("state")
##    attorneys=database.getAttorneys('attorney', searchTerm, state)
    attorneys=database.getData('attorney',state)
    return bottle.template('localattorneysearchresults',dict(attorneys=attorneys))
    
@bottle.route('/legalquestionsubmission')
def legalquestionsubmission():
    return bottle.template('legalquestionsubmission')

@bottle.post('/dolegalquestionsubmission')
def showlegalquestionsubmission():
    entryType='userquestion'
    state=bottle.request.forms.get("state")
    userquestion=bottle.request.forms.get("userquestion")
    #first save the question
    database.saveData(entryType,state,{'userquestion':userquestion})
    #save entire database
    database.save()
    #then retrieve and display the questions
    receivedquestions=database.getData('userquestion',state)
    
##    searchTerm=bottle.request.forms.get("userquestion")
##    state=bottle.request.forms.get("state")
##    receivedquestion=database.getQuestions('question',searchTerm,state)    
##    return bottle.template('legalquestionsubmission',dict(receivedquestion=receivedquestion))
    return bottle.template('showlegalquestionsubmission',dict(receivedquestions=receivedquestions))

@bottle.route('/statutelookup')
def statutelookup():
    return bottle.template('statutelookup')

@bottle.post('/dostatutelookup')
def statutelookupresults():
    state=bottle.request.forms.get("state")
    statutes=database.getData('statutelookup',state)
    return bottle.template('statutelookupresults',dict(statutes=statutes))

@bottle.route('/whatsmycharge')
def whatsmycharge():
    return bottle.template('whatsmycharge')

@bottle.post('/dochargelookup')
def statutelookupresults():
    state=bottle.request.forms.get("state")
    charges=database.getData('whatsmycharge',state)
    return bottle.template('whatsmychargeresults',dict(charges=charges))
	
@bottle.route('/whatsmyfine')
def caselawlookup():
    return bottle.template('whatsmyfine')

database=model_v2.Database()
bottle.debug(True)
bottle.run(host='localhost', port=8080)
