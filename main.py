from Scraper.main import main as Scraper
from Database.main import main as Database
from Functions.GetPersonalEmails import GetPersonalEmails
from Functions.CreatePersonalizedMessages import CreatePersonalizedMessages
from Functions.SendEmails import SendEmails
from Functions.Status import status
from Functions.SendUpdate import SendUpdate

class Workflow:
    def __init__(self):
        self.status = status
        self.data = None

    def run_workflow(self):
        self.scrape_linkedin()
        self.get_personal_emails()
        self.create_personalized_emails()
        self.update_database()
        self.send_emails()
        self.check_email_status()

    def scrape_linkedin(self):
        self.data = Scraper(self.status)

    def get_personal_emails(self):
        if self.status['ScrapeLinkedin']['status'] == True:
            self.print_success_message('ScrapeLinkedin')
            self.data = GetPersonalEmails(self.status, self.data)
        else:
            self.print_error_message('ScrapeLinkedin')

    def create_personalized_emails(self):
        if self.status['GetPersonalEmails']['status'] == True:
            self.print_success_message('GetPersonalEmails')
            self.data = CreatePersonalizedMessages(self.status, self.data)
        else:
            self.print_error_message('GetPersonalEmails')

    def update_database(self):
        if self.status['GetPersonalizedEmails']['status'] == True:
            self.print_success_message('GetPersonalizedEmails')
            Database(self.status, self.data)
        else:
            self.print_error_message('GetPersonalizedEmails')

    def send_emails(self):
        if self.status['UpdateDatabase']['status'] == True:
            self.print_success_message('UpdateDatabase')
            SendEmails(self.status, self.data)
        else:
            self.print_error_message('UpdateDatabase')

    def check_email_status(self):
        if self.status['SendEmails']['status'] == True:
            self.print_success_message('SendEmails')
            SendUpdate()
        else:
            self.print_error_message('SendEmails')

    def print_success_message(self, step):
        print(self.status[step]['success_message'])

    def print_error_message(self, step):
        print(self.status[step]['error_message'])


def main():
    workflow = Workflow()
    workflow.run_workflow()
    return


if __name__ == "__main__":
    main()
