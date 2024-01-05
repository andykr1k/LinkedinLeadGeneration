import os
from supabase import create_client, Client
from dotenv import load_dotenv

def main(status, data):
	load_dotenv()
	url = os.getenv("SUPABASE_URL")
	key = os.getenv("SUPABASE_API_KEY")
	supabase: Client = create_client(url, key)

	for person in data:
		data, count = supabase.table('FoodServiceManagers').insert({"first_name": person['first_name'], "last_name": person['last_name'], "personal_email": person['personal_email'], "headline": person['headline'], "about": person['about'], "city": person['city'], "state": person['state'], "school": person['school'], "company": person['company'], "linkedin_public_id": person['public_id'], "job_title": person['job_title'], "linkedin_url": person['linkedin_url'], "location": person['location'], "personalized_dear": person['personalized_welcome_start'], "personalized_welcome": person['personalized_welcome_paragraph'], "added_to_newsletter": False, "welcome_sent": False}).execute()

	status['UpdateDatabase']['status'] = True
	
	return
