import json
import mysql.connector
import time
import constants
import data_fields

START_TIME = time.clock()

def getValue(myString, start, end):
    return myString[start-1:end]

year = "2018"
readFile = year + ".txt"
rfo = open(readFile, "r")

ROWS_PER_PART = 500000
MAX_READ = None
START_PART = 1 # MINIMUM OF 1


wfo = None
id = 0
currentPart = START_PART - 1
for x in rfo:
    if id >= (START_PART-1) * ROWS_PER_PART:
        if (id) % ROWS_PER_PART == 0:
            if wfo != None:
                wfo.close()
            currentPart = currentPart + 1
            wfo =  open("birth-data-" + str(year) + "-" + str(ROWS_PER_PART) + "-rows-part-"+str(currentPart)+".csv", "w")
    else:
        id = id + 1
        continue
    id = id + 1
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
        csvRow = csvRow + '"' + str(columns[col]['definition']) + '"'
    wfo.write(csvRow)
    wfo.write('\n')
    if MAX_READ != None:
        if id == MAX_READ:
            break
END_TIME = time.clock()
print("Finished at " + str(END_TIME-START_TIME) + " seconds")
wfo.close()
rfo.close()