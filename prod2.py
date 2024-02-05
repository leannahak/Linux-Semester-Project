
import gzip
f = gzip.open("acs.gz", "rt")
line = f.readlines()

for lines in line:
    fields = lines.split('|') #the file is pipe delimited
    totPop = fields[2] #total pop field
    zip_code = fields[1] #zip field 
    test = fields[1].split() #split zip field 
    if len(test) > 1:
        zipCode = test[1]
        numPersians = fields[238] #number of people from iran within the zip in this field
        numKoreans  = fields[214] #number of people from korea within the zip in this field
        
        print (zipCode + "|" + numPersians + "|" + numKoreans + "|" + totPop)
        #print zip|#persians|#koreans|totalpop
