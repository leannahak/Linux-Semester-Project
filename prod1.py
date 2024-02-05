import gzip
f = gzip.open("corp.gz", "rt")
line = f.readlines()


zipsCount = {}
for lines in line:
    fields = lines.split('\t') #the data set is tab delimited
    zip_code = fields[11][0:5]  # Assuming the zip code is in the 12th field
    date = fields[2]
    #for each zip code count how many dates there are from past 5 years(2018)
    if date[-4:] in {'2018', '2019', '2020', '2021', '2022', '2023'}:
        if zip_code not in zipsCount.keys():
            zipsCount[zip_code] = 1
        else:
            zipsCount[zip_code] += 1
for z in zipsCount.keys():
    print(str(z) + "|" + str(zipsCount[z])) #print zip and number of corp created in that zip from past 5 years
    

