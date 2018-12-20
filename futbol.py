#############################################################################################################################
#API key: 78b11f075e39478ca4d95729a8da7271
#Import http.client for the API connection, json for the json files we are messing with
#############################################################################################################################
import http.client, json
#############################################################################################################################
#right now we are going to traverse the dictionary
#first for loop gives us the empty set and the header of info
#second for loop gives us
#############################################################################################################################
def getPLTable():
    connection = http.client.HTTPConnection('api.football-data.org')
    headers = { 'X-Auth-Token': '78b11f075e39478ca4d95729a8da7271' }
    connection.request('GET', '/v2/competitions/PL/standings?', None, headers )
    trash = json.loads(connection.getresponse().read().decode())
    print(trash)

    tableList = []

    for firstIter in trash:
        for secondIter in trash[firstIter]:
                if type(secondIter) is dict:
                    tableVal = 0
                    for tableVal in range(20):
                        if secondIter.get('type') == "TOTAL":
                            teamInfo = []
                            table = secondIter.get('table')
                            teamInfo.append(str(table[tableVal].get('position')))
                            teamName = table[tableVal].get('team').get('name')
                            teamInfo.append(teamName)
                            teamInfo.append(str(table[tableVal].get('playedGames')))
                            teamInfo.append(str(table[tableVal].get('won')))
                            teamInfo.append(str(table[tableVal].get('draw')))
                            teamInfo.append(str(table[tableVal].get('lost')))
                            teamInfo.append(str(table[tableVal].get('points')))
                            teamInfo.append(str(table[tableVal].get('goalsFor')))
                            teamInfo.append(str(table[tableVal].get('goalsAgainst')))
                            teamInfo.append(str(table[tableVal].get('goalDifference')))
                            tableList.append(teamInfo)
                            tableVal += 1
    return tableList

#############################################################################################################################
#We will now create a method to write our data from the API to a  JSON file
#I chose JSON because we want to use JavaScript with our website to access the data
#We take in the PL table that we defined with dictionaries for the team team info
#############################################################################################################################
def writeJSON(tableList):
    i = 0
    for team in tableList:
        d = {k: v for k, v in team}
        if i == 0:
            with open("pltable.json", 'w') as writeFile:
                json.dump(d, writeFile)
                i += 1
        else:
                with open("pltable.json", 'a') as writeFile:
                    json.dump(d, writeFile)

#############################################################################################################################
#
#############################################################################################################################
def couplizer(tableList):
    newList = []
    for team in tableList:
        kee = ["position", "name", "matches", "wins", "draws", "losses", "points", "goalsFor", "goalsAgainst", "goalDiff"]
        zipper = list(zip(kee, team))
        newList.append(zipper)
    return newList

#############################################################################################################################
#We want to call the methods we created now so we can grab the table from the API and use it on our website
#First we want to retrieve the table from the API
#Next we want to touple the data with a label for the data
#Then we want to write our data to a JSON file
#############################################################################################################################
def main():
    pltable = getPLTable()
    dictTable = couplizer(pltable)
    writeJSON(dictTable)

#############################################################################################################################
#Define the main method in our program
#############################################################################################################################
if __name__ == "__main__":
    main()
