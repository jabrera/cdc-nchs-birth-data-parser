import json
import mysql.connector
import time
import constants
import data_fields

def getValue(myString, start, end):
    return myString[start-1:end]

year = "2016"
readFile = year + ".txt"
writeFile = "parsed" + year + ".csv"
MAX_READ = 100

rfo = open(readFile, "r")
wfo = open(writeFile, "w").close()
wfo = open(writeFile, "a")
id = 0
START_TIME = time.clock()
for x in rfo:
    print("-=-=-=-=-=-=")
    id = id + 1

    

    print("ID ["+ str(id) +"]")
    print("Length is " + str(len(x)))
    print(x)

    columns = data_fields.columns[year]
    csvRow = ''
    colCount = 0
    for col in columns:
        colCount = colCount + 1

        columns[col]['value'] = getValue(x,columns[col]['start'],columns[col]['end'])

        if 'valueDefinition' in columns[col]:
            if columns[col]['value'] in columns[col]['valueDefinition']:
                columns[col]['definition'] = columns[col]['valueDefinition'][columns[col]['value']]
            else:
                found = False
                for tempCol in columns[col]['valueDefinition']:
                    if tempCol[0:2] == '__':
                        found = True
                        ifColumn = tempCol[2:]
                        if columns[ifColumn]['value'] in columns[col]['valueDefinition'][tempCol]:
                            columns[col]['definition'] = columns[col]['valueDefinition'][tempCol][columns[ifColumn]['value']][columns[col]['value']]
                if not found:
                    for tempCol in columns[col]['valueDefinition']:
                        if '-' in tempCol:
                            conditions = tempCol.split('-')
                            if columns[col]['value'] != '':
                                if int(columns[col]['value']) >= int(conditions[0]) and int(columns[col]['value']) <= int(conditions[1]):
                                    found = True
                                    columns[col]['definition'] = columns[col]['valueDefinition'][tempCol]
                    if not found:
                        if '*' in columns[col]['valueDefinition']:
                            columns[col]['definition'] =  columns[col]['valueDefinition']['*']
                        else:
                            columns[col]['definition'] = columns[col]['value']
        else:
            columns[col]['definition'] = columns[col]['value']

        columns[col]['definition'] = columns[col]['definition'].replace('[value]', str(columns[col]['value']).strip("0"))
        
        if colCount > 1:
            csvRow = csvRow + ','
        csvRow = csvRow + str(columns[col]['definition'])
    
    wfo.write(csvRow)
    wfo.write('\n')

    # print(json.dumps(columns,indent=2))



    if id == MAX_READ:
        break

END_TIME = time.clock()

print("Finished at " + str(END_TIME-START_TIME) + " seconds")

wfo.close()
rfo.close()