import requests
import os
import json

class IncidentFinder:
    @staticmethod
    def get_incident(incidentNumber):
        
        # Eg. User name="admin", Password="admin" for this code sample.
        user = 'janevit.j@kbtg.tech'
        pwd = 'P@ssw0rd_Dev'
        
        try:
            url = f"https://kasikornbankdev.service-now.com/api/now/table/incident?sysparm_limit=1&number={incidentNumber}"
            
            # Set proper headers
            headers = {"Content-Type":"application/json","Accept":"application/json"}
            
            # Do the HTTP request
            response = requests.get(url, auth=(user, pwd), headers=headers)
            
            # Check for HTTP codes other than 200
            #if response.status_code != 200: 
            #    print('Status:', response.status_code, 'Headers:', response.headers, 'Error Response:',response.json())
            #    exit()
            
            # Decode the JSON response into a dictionary and use the data
            data = response.json()
            #temp_max = data['main']['temp_max']
            #temperature = data['main']['temp']
            #humidity = data['main']['humidity']
            description = data['description']
            print(data)

            return {
                #"currentTemperature": temperature,
                #"maxTemperature": temp_max,
                #"humidity": humidity,
                "description": description
            }

        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            return {"error": "HTTP error occurred while retrieving incident data."}

