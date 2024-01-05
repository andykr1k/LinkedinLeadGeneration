import requests

def BatchSearch(API_KEY):
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/search-employees"

    payload = {
        "geo_codes": [103644278],
        "geo_codes_exclude": [],
        "title_keywords": [],
        "title_keywords_exclude": [],
        "industry_codes": [],
        "industry_codes_exclude": [],
        "current_company_ids": [],
        "past_company_ids": [],
        "company_headcounts": [],
        "profile_languages": ["English"],
        "functions": [],
        "functions_exclude": [],
        "seniority_levels": [],
        "activity_and_share_experiences": [],
        "keywords": "food service manager",
        "limit": 1
    }

    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "fresh-linkedin-profile-data.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
    
    # print("Printing Batch Search Response")
    json_response = response.json()

    # print(json_response)
    request_id = json_response.get('request_id')

    return request_id
