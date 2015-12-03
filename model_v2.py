import os,inspect,csv

class Database(object):
    def __init__(self):
        self.getPath()
        self.database=[]
        self.getDatabase()
        self.fixUniques()

    def getPath(self):
        '''gets the application path'''
        self.path=os.path.dirname(inspect.getfile(inspect.currentframe()))
        self.datapath=os.path.join(self.path,'data')
##        self.databkuppath=os.path.join(self.databkuppath,'data')
        
    def getDatabase(self):
        '''looks in data subdirectory and adds information from there
        stores the name of the file in each dictionary'''
        csv.register_dialect('ourdialect',delimiter='|',lineterminator='\n',quoting=csv.QUOTE_NONE)
        slist=os.listdir(self.datapath)
        slist=filter(lambda f:f.endswith('.txt'),slist)
        
        llist=[os.path.join(self.datapath,f) for f in slist]
        for f in llist:
            sourcefile=os.path.basename(f)
            with open(f,'rb') as csvfile:
                reader=csv.DictReader(csvfile,dialect='ourdialect')
                for adict in reader:
                    adict.update({'sourcefile':sourcefile})
                    self.database+=[adict]

    def save(self):
        '''saves the data to various files in subdirectory'''
        sourcefiles=set() #a set of sourcefiles names
        header=set()
        for line in self.database:
            sourcefiles.add(line['sourcefile'])
            [header.add(k) for k in line.keys()]

        header=list(header)
        header.sort()
        header.reverse()
        for sf in sourcefiles:
            filelist=[]
            alist=filter(lambda x:x['sourcefile']==sf,self.database)
            for adict in alist:
                line=[adict.get(k,'') for k in [k for k in header]]
                line=[str(k) for k in line]
                line='|'.join(line)
                filelist+=[line]
            filelist.insert(0,'|'.join(header))
            filelist=['%s\n\n'%l for l in filelist]

            f=os.path.join(self.datapath,sf)
            with open(f,'wb') as fobj:
                fobj.writelines(filelist)

    def saveData(self,entrytype,state,adict):
        '''save an item, but only if unique'''
        adict.update({'state':state})
        adict.update({'entryType':entrytype})
        if not adict.has_key('sourcefile'):adict['sourcefile']='online.txt'#assumed online.txt if not present
        self.addHash(adict)
        try:#check to see if item already in the database
            sameitems=filter(lambda item:item['unique']==adict['unique'],self.database)
        except:#if error thrown, something is missing a unique...add them and recheck
            self.fixUniques()
            sameitems=filter(lambda item:item['unique']==adict['unique'],self.database)
        if len(sameitems)==0:self.database+=[adict]#add the item if it isn't already present

    def deleteData(self,unique):
        '''performs a delete based on the unique number given'''
        data=filter(lambda item:item['unique']==unique,self.database)
        for d in data:
            try:self.database.remove(d)
            except:pass

    def addHash(self,adict):
        '''adds a unique hash to a dictionary'''
        try:adict.pop('unique')
        except:pass
        ahash=hash(frozenset(adict.items()))
        adict.update({'unique':ahash})

    def fixUniques(self):
        '''adds unique numbers to each dictionary so that deletes can be performed'''
        for i in range(len(self.database)-1,-1,-1):
            item=self.database[i]
##            if not item.has_key('unique'):
            self.addHash(item)

    def getData(self,entrytype,state):
        '''retrieves data based on entrytype and state
       further filtering must be performed downstream'''
        data=filter(lambda item:item['entryType']==entrytype,self.database)
        data=filter(lambda item:item['state']==state,data)
        return data
        
if __name__=='__main__':
    d=Database()
    
##    print d.database
##    d=Database()
####    d.saveData('caselaw','OR',{'entryText':'entryText'})
####    print d.getData('caselaw','OR','search')
####    d.deleteData(6705027775516781702)
    d.save()
