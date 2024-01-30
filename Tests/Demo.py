from SendEmail import SendEmail
from UpdateDatabase import UpdateDatabase
from SendUpdate import SendUpdate

def Demo():
    print("Scraping Linkedin with specified params...")
    print("Linkedin Scraping Completed found 1/1.")
    print("Getting Personal Email...")
    print("Email Scraping Completed found 1/1.")
    print("Creating Personalized Welcome Starter..")
    print("Personalized Starter Generated 1/1.")
    print("Sending Email and Updating Database...")
    UpdateDatabase()
    SendEmail()
    print("Linkedin Process Finished.")
    SendUpdate()

Demo()