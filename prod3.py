#!usr/bin/env python3
import gzip

prod1 = open("./prod1.txt")
prod2 = open("./prod2.txt")

prod1dict = {}
prod2dict = {}

line = prod1.readline() #read in prod1.txt
while line: #for each line
    cur = line.split("|")
    prod1dict[cur[0]] = cur[1]#in the dict make the key be zip and data the #corp
    line = prod1.readline()
prod1.close()

line = prod2.readline() #read in prod2.txt
while line: #for each line
    cur = line.split("|")
    prod2dict[cur[0]] = [cur[1],cur[2],cur[3]]#in next dict make key the zip and data = #persians,#koreans,#newcorp
    line = prod2.readline()
prod2.close()


for key in prod1dict:
    if key in prod2dict:
        numPersians =  prod2dict[key][0]
        numKoreans  =  prod2dict[key][1]
        totPop =       prod2dict[key][2]
        newCorp =      prod1dict[key]
         #making sure we have valid values to work with:
        if (numPersians != "" and int(numPersians) > 0) \
           and (numKoreans != "" and int(numKoreans) > 0) \
           and (totPop != "" and int(totPop) > 0) \
           and (newCorp != "" and int(newCorp) > 0):
            #calculation of persian,korean,corp ratio over totpop in the zip
            ratio1 =int(numPersians) / int(totPop)
            ratio2 =int(numKoreans) / int(totPop)
            ratio3 =int(newCorp) / int(totPop)
            print( key + "|" + str(ratio1) + "|" + str(ratio2) + "|" + str(ratio3))
            #outputting thr ratios: zip|persianratio|koreanratio|newcorpratio


            
                        
            
            
            
            
            

            
            
        
        
