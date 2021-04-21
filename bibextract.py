import os

def strip(string):
    string = string.rstrip()
    if string.endswith('"'):
        firstquote = string.find('"')
        string = string[firstquote+1:-1]
    if string.endswith('}'):
        firstrcb = string.find('{')
        string = string[firstrcb+1:-1]
    string = string.lstrip()
    return string
        

class bibtex(object):
    
    def __init__(self, file):
        self.filename = file
        lines = ''.join(list(open(file, 'r'))).replace('\n','')
        entries = [ln for ln in lines.split('@') if ln]
        self.entries = {}
        self.duplicate_entries = []
        if not entries: 
            return
        for i,ent in enumerate(entries):
            entkey = ent[ent.find('{')+1:ent.find(',')]
            if entkey in self.entries:
                self.duplicate_entries.append(entkey)
                continue
            lastcurlybrace = ent[::-1].find('}')+1
            ent = ent[ent.find(',')+1:-lastcurlybrace]
            entsplit = ent.split('=')
            if len(entsplit)==1: 
                self.entries[entkey] = {}
                continue
            keys = [entsplit[0].strip()]
            values = []
            for es in entsplit[1:-1]:
                lastcomma = es[::-1].find(',')+1
                keys.append(es[-lastcomma+1:].strip())
                values.append(strip(es[:-lastcomma]))
            values.append(strip(entsplit[-1]))
            self.entries[entkey] = dict(zip(keys,values))
            
    def open_doi(self, *args, browser='default'):
        if browser == 'default': browser = 'xdg-open'
        for arg in args:
             for entry in arg.split(','):
                entry = entry.strip()
                if entry in self.entries:
                    doiurl = self.entries[entry].get('doi','')
                    if doiurl:
                        print(doiurl)
                        os.system(browser+" https://doi.org/'" + doiurl + "' &")
    
    def open_ads(self, *args, browser='default'):
        if browser == 'default': browser = 'xdg-open'
        for arg in args:
            for entry in arg.split(','):
                entry = entry.strip()
                if entry in self.entries:
                    adsurl = self.entries[entry].get('adsurl','')
                    if adsurl:
                        print(adsurl)
                        os.system(browser+" '" + adsurl + "' &")
                        
           
