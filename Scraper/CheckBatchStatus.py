import requests

def CheckBatchStatus(API_KEY, id):
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/check-search-status"

    querystring = {"request_id":id}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print("Printing Batch Status Response")
    json_response = response.json()
    
    # print(json_response)
    status = json_response.get('status')

    if status == 'done':
        return True
    else:
        return False
