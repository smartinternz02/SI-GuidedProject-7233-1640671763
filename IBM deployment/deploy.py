import requests

# NOTE: you must manually set API_KEY below using information retrieved from your IBM Cloud account.
API_KEY = "_Dr5CuiOCUQstT23oXHgy0tAX8A55VGcUvlcjUwxR_ux"
token_response = requests.post('https://iam.cloud.ibm.com/identity/token', data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'})
mltoken = token_response.json()["access_token"]

header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}

# NOTE: manually define and pass the array(s) of values to be scored in the next line
payload_scoring = {"input_data": [{"field": [["CountryName","CountryCode","IndicatorName","IndicatorCode","Year",
                                              "Value"]], "values": [[1,4,5,6]]}]}
#"Arab World","ARB","Arms imports (SIPRI trend indicator values)","MS.MIL.MPRT.KD","1960","538000000"

response_scoring = requests.post('https://us-south.ml.cloud.ibm.com/ml/v4/deployments/ed3a14d4-5269-4555-9a22-7e560620dab2/predictions?version=2022-02-02', json=payload_scoring, headers={'Authorization': 'Bearer ' + mltoken})
print("Scoring response")
print(response_scoring.json())