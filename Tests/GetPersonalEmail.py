import os
import requests
from dotenv import load_dotenv


def GetPersonalEmail(url):
    load_dotenv()
    PPROXYCURL_API_KEY = os.getenv("PROXYCURL_API_KEY")

    headers = {'Authorization': 'Bearer ' + PPROXYCURL_API_KEY}
    api_endpoint = 'https://nubela.co/proxycurl/api/contact-api/personal-email'
    response = requests.get(api_endpoint,
                            params={'linkedin_profile_url': url,
                                    'page_size': '1'},
                            headers=headers)

    data = response.json()

    print(data.get('emails')[0])

    return


GetPersonalEmail("https://www.linkedin.com/in/elizbas/")
