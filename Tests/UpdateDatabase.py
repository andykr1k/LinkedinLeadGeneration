import os
from supabase import create_client, Client
from dotenv import load_dotenv

def UpdateDatabase():
    load_dotenv()
    url = os.getenv("SUPABASE_URL")
    key = os.getenv("SUPABASE_API_KEY")
    supabase: Client = create_client(url, key)

    data, count = supabase.table('FoodServiceManagers').insert({"first_name": 'Andrew', "last_name": 'Krikorian', "personal_email": 'akrikorian12@gmail.com', "headline": 'programmer', "about": 'programmer', "city": 'Riverside', "state": 'CA', "school": 'UCR', "company": 'Heirloom', "linkedin_public_id": 'andrew-krikorian', "job_title": 'programmer', "linkedin_url": 'https://www.linkedin.com/in/andrew-krikorian', "location": 'Riverside, California', "personalized_dear": 'Hello Andrew Krikorian', "personalized_welcome": 'Hello Andrew Krikorian', "added_to_newsletter": False, "welcome_sent": True, "company_size": '1-10', "corp_address": '1400 University Ave', "receive_address": '1400 University Ave', "distributor": 'Heirloom'}).execute()

    # print("Printing Data: \n", data)
    # print("Printing Count: \n", count)
    return