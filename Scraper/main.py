import os
import pandas as pd
from dotenv import load_dotenv
from Scraper.GetBatchResults import GetBatchResults
from Scraper.CheckBatchStatus import CheckBatchStatus
from Scraper.BatchSearch import BatchSearch

def main(status):
	load_dotenv()
	API_KEY = os.getenv('RAPID_API_KEY')
	
	req_id = BatchSearch(API_KEY)
	
	checkbatchstatus = CheckBatchStatus(API_KEY, req_id)

	if checkbatchstatus:
		json_response = GetBatchResults(API_KEY, req_id, 1)
		status['ScrapeLinkedin']['status'] = True
	else:
		status['ScrapeLinkedin']['status'] = False
		raise Exception()

	# print(json_response.get("data"))
	return json_response.get("data")
