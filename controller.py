import bottle
import model

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
    states=database.getList("stateList")
    return bottle.template('localattorneysearch',dict(states=states))

@bottle.post('/docountysearch')
def docountysearch():
    searchTerm=bottle.request.forms.get("state")
    state=database.getState(searchTerm)
    return bottle.template('countysearchresults',state=state)

@bottle.post('/dolocalattorneysearch')
def dolocalattorneysearch():
    searchTerm=bottle.request.forms.get("county")
    state=bottle.request.forms.get("state")
    attorneys=database.getAttorneys('attorney', searchTerm, state)
    return bottle.template('localattorneysearchresults',attorneys=attorneys)

database=model.Database()
bottle.debug(True)
bottle.run(host='localhost', port=8080)
