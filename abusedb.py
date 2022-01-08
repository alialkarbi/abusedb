#####
# Abuseip-DB checking script
# Ali Alkarbi
# am.alkarbi@gmail.com
#
####
import requests
import json
import sys

fileName = sys.argv[1]
headers = {
    'Key': 'Your Key',
    'Accept': 'application/json'
}
with open(fileName) as ipList:
	for ipAddress in ipList.readlines():
		parameters = {"ipAddress": ipAddress,'maxAgeInDays': '1','verbose': ''}
		response = requests.get('https://api.abuseipdb.com/api/v2/check', params=parameters, headers=headers)
		rawData = json.loads(response.content.decode("utf-8"))
		country = rawData['data']['countryName']
		totalReports = rawData['data']['totalReports']
		isWhitelisted=str(rawData['data']['isWhitelisted'])
		if isWhitelisted == "False":
			isWhitelisted = "No"
		elif isWhitelisted == "True":
			isWhitelisted = "Yes"	
		elif isWhitelisted == "None":
			isWhitelisted = "No Information"
		abuseConfidenceScore=rawData['data']['abuseConfidenceScore']
		
		print ("IP-Address: " ,ipAddress.strip(), "| Country: ", country, "| Total-Reports: ", totalReports,"| White-List: ",isWhitelisted,"| Abuse-Score: ",abuseConfidenceScore)
		
