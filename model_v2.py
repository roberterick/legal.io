##cs361, fall 2015
##project b
##rishi bhandarkar, james carlin, joshua curtis
##robert erick, tyler koistinen, grant nakashima

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
        sourcefiles={} #a set of sourcefiles names
        for line in self.database:
            sf=line['sourcefile']
            if not sourcefiles.has_key(sf):
                sourcefiles[sf]={'header':set()}
                [sourcefiles[sf]['header'].add(k) for k in line.keys()]

        for sf in sourcefiles.keys():
            header=list(sourcefiles[sf]['header'])
            header.sort()
            header.reverse()
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
        return adict #helpful for testing

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
            self.addHash(item)

    def getData(self,entrytype,state):
        '''retrieves data based on entrytype and state
       further filtering must be performed downstream'''
        data=filter(lambda item:item['entryType']==entrytype,self.database)
        data=filter(lambda item:item['state']==state,data)
        return data

#######################################################################################
    def performTests(self):
        print '*'*25
        print 'performing model tests'

        print '\ntesting the path'
        testpath=os.path.dirname(inspect.getfile(inspect.currentframe()))
        if testpath==self.path:
            print 'test path ok'
        else:
            print '*'*25+'test path is not ok'

        print '\ntesting loading of data from files'
        data=filter(lambda item:item['entryType']=='testdata',self.database)
        if len(data)>=2:
            errorflag=False
            for adict in data:
                if adict.has_key('entryType') and adict.has_key('state'):
                    pass
                else:
                    errorflag=True
            if errorflag==False:
                print 'data load from files looks ok'
            else:
                print '*'*25+'test of data load from files failed'
        else:
            print '*'*25+'test of data load from files failed'

        print '\ntesting data save'
        #delete old data
        for i in range(len(self.database)-1,-1,-1):
            adict=self.database[i]
            if adict['entryType']=='testdata' and adict['entryText']=='test entry 3':
                self.database.pop(i)
        #save a test entry
        adict={'entryType':'testdata','state':'CA','entryText':'test entry 3'}
        returndict=self.saveData(adict['entryType'],adict['state'],adict)
        #did it save
        data=filter(lambda item:item['entryType']=='testdata',self.database)
        data=filter(lambda item:item['entryText']=='test entry 3',data)
        if len(data)>0:
            print 'data save looks ok'
        else:
            print '*'*25,'data save test failed'

        print '\ntesting data delete'
        #use returndict from above
        unique=returndict['unique']
        #perform delete
        self.deleteData(unique)
        data=filter(lambda item:item['unique']==unique,self.database)
        if len(data)==0:
            print 'data delete looks ok'
        else:
            print '*'*25,'data delete test failed'

        print '\ntesting addHash function'
        testdict={'key1':'one','key2':'two'}
        self.addHash(testdict)
        if testdict['unique']==3209478279599810223:
            print 'test of addHash looks ok'
        else:
            print '*'*25,'addHash function test failed'

        print '\ntesting the fixUniques function'
        testdict={'entryType':'testdata','state':'CA','test':'uniques test'}
        #add testdict
        self.database+=[testdict]
        #call function
        self.fixUniques()
        #did it add the unique?
        errorflag=False
        for i in range(len(self.database)-1,-1,-1):
            adict=self.database[i]
            if adict.has_key('unique'):
                pass
            else:
                errorflag=True
            try:
                if adict['test']=='uniques test':#delete the test data
                    self.database.pop(i)
            except:pass
        if errorflag==False:
            print 'test of fixUniques function looks ok'
        else:
            print '*'*25,'test of fixUniques failed'

        print '\ntesting the getData function'
        #use function to get some test data
        adicts=self.getData('testdata','OR')
        data=filter(lambda item:item['entryType']=='testdata' and item['state']=='OR',self.database)
        errorflag=False
        for adict in adicts:
            if adict in data:
                pass
            else:
                errorflag=True
        if errorflag==False:
            print 'test of getData function looks ok'
        else:
            print '*'*25,'test of getData function failed'
            
        print '\ntesting the save function'
        slist=os.listdir(self.datapath)
        #choose a file
        apath=os.path.join(self.datapath,slist[0])
        #get last modification stats
        lastmodification=os.stat(apath)
        #call save
        self.save()
        #get new modification
        newmodification=os.stat(apath)
        #did it change
        if lastmodification!=newmodification:
            print 'test of save function looks ok'
        else:
            print '*'*25,'test of save function failed'
        print '*'*25
        
if __name__=='__main__':
    d=Database()
    d.performTests()
