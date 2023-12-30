import requests

def BatchSearch(API_KEY):
    url = "https://fresh-linkedin-profile-data.p.rapidapi.com/search-employees"

    payload = {
        "geo_codes": [103644278],
        "geo_codes_exclude": [],
        "title_keywords": ["Director", "Manager", "Ambassador", "Head"],
        "title_keywords_exclude": [],
        "industry_codes": [144, 57, 68, 1594, 6, 1810],
        "industry_codes_exclude": [],
        "current_company_ids": [],
        "past_company_ids": [],
        "company_headcounts": ["51-200"],
        "profile_languages": ["English"],
        "functions": ["Administrative"],
        "functions_exclude": [],
        "seniority_levels": [],
        "activity_and_share_experiences": [],
        "keywords": "system",
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
