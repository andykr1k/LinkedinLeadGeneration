import os
import requests
from dotenv import load_dotenv

def GetPersonalEmails(status, data):
    load_dotenv()
    PPROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")

    headers = {'Authorization': 'Bearer ' + PPROXYCURL_API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/v2/linkedin'

    for idx, person in enumerate(data):
        url = person['linkedin_url']

        headers = {'Authorization': 'Bearer ' + PPROXYCURL_API_KEY}
        api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-email'
        response = requests.get(api_endpoint,
                                params={'linkedin_profile_url': url,
                                        'page_size': '1'},
                                headers=headers)

        res = response.json()

        email = res.get('emails')[0]

        data[idx]['personal_email'] = email

    status['GetPersonalEmails']['status'] = True

    print(data)
    return data