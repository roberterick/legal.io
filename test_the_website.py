##cs361, fall 2015
##project b
##rishi bhandarkar, james carlin, joshua curtis
##robert erick, tyler koistinen, grant nakashima
import time
import urllib2


def testPageExists(page=None):
    pagedesc='home page' if page==None else page
    print 'testing %s'%pagedesc
    pth=''
    if page==None:
        path='http://localhost:8080/'
    else:
        path='http://localhost:8080/%s'%page
    try:
        response=urllib2.urlopen(path)
    except:
        print '*'*25,'the website is not running or the %s page is broken'%pagedesc
        return
    html=response.read()
    if html.find('Error: ')>-1:
        print '*'*25,'the website is not running or the %s page is broken'%pagedesc
    else:
        print 'the %s page exists'%pagedesc




def performTests():
    print '*'*25
    print 'testing the website'
    pages=[None,'caselawlookup','statutelookup','understandyourcharge',
           'whatsmyfine','localattorneysearch','legalquestionsubmission',
##           'docaselawlookup','dostatutelookup','dolocalattorneysearch',
##           'dolegalquestionsubmission',
           ]
    for page in pages:
        testPageExists(page)


performTests()
    
