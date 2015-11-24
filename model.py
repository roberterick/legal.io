import os,inspect

class Database(object):
    def __init__(self):
        self.getPath()
        self.getDatabase()
        self.fixUniques()

    def getPath(self):
        self.path=os.path.dirname(inspect.getfile(inspect.currentframe()))
        self.path=os.path.join(self.path,'database.txt')
        
    def getDatabase(self):
        fobj=open(self.path,'r')
        self.database=eval(fobj.read())
        fobj.close()

    def save(self):
        s=str(self.database)
        s=s.replace('}, ','},\n')
        s=s.replace('[{','[\n{')
        s=s.replace('}]','}\n]')
        fobj=open(self.path,'wb')
        fobj.write(s)
        fobj.close()

    def saveData(self,entrytype,state,adict):
        adict.update({'state':state})
        adict.update({'entryType':entrytype})
        self.addHash(adict)
        try:
            sameitems=filter(lambda item:item['unique']==adict['unique'],self.database)
        except:
            self.fixUniques()
            sameitems=filter(lambda item:item['unique']==adict['unique'],self.database)
        if len(sameitems)==0:self.database+=[adict]

    def deleteData(self,unique):
        data=filter(lambda item:item['unique']==unique,self.database)
        for d in data:self.database.remove(d)

    def addHash(self,adict):
        try:adict.pop('unique')
        except:pass
        ahash=hash(frozenset(adict.items()))
        adict.update({'unique':ahash})

    def fixUniques(self):
        for i in range(len(self.database)-1,-1,-1):
            item=self.database[i]
            if not item.has_key('unique'):
                self.addHash(item)

    def getData(self,entrytype,state):
        data=filter(lambda item:item['entryType']==entrytype,self.database)
        data=filter(lambda item:item['state']==state,data)
        return data
        
if __name__=='__main__':
    d=Database()
##    d.saveData('caselaw','OR',{'entryText':'entryText'})
##    print d.getData('caselaw','OR','search')
##    d.deleteData(6705027775516781702)
    d.save()
