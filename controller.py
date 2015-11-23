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
    cases=database.getData('caselaw',state,searchTerm)
    return bottle.template('caselawlookupresults',dict(cases=cases))


database=model.Database()
bottle.debug(True)
bottle.run(host='localhost', port=8080)
