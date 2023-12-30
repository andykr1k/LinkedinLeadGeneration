import requests

def GetBatchResults(API_KEY, id, page):
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/get-search-results"

    querystring = {"request_id":id, "page":page}

    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # print("Printing Batch Search Results")
    json_response = response.json()

    # print(json_response)

    return json_response
