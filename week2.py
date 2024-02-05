import csv
from datetime import datetime


corruptedRecords = []
usersData = {}


def displayPerson(id, personData):
    try:
        data = personData[id]
        print("This ID belongs to " + data[0] + " born on " + data[1])
    except:
        print("User not found")    

def processData(data): 
    csvReader = csv.reader(csv_file)
    counter = 0

    for row in csvReader:
        if counter == 0:
            counter+=1
            continue
        else:
            try:
                dateObject = datetime.strptime(row[2], '%d/%m/%Y')
                convertedDate = dateObject.strftime('%Y-%m-%d')
              
                usersData[row[0]] = (row[1], convertedDate)
            except:
                corruptedRecords.append(row)
                with open('error_log.txt', 'a') as file:
           
                    file.write("Error processing line #" + row[0] + " for " + row[1] + " \n")
                # logging.error("Error processing line #" + row[0] + " for " + row[1])
        

   

with open("./birthdays100.csv", 'r') as csv_file:
        processData(csv_file)


while True:
    id = int(input("Enter the ID"))

    if id == 0 or id < 0:
        print("Program closed")
        break
    else:
        displayPerson(str(id), usersData)