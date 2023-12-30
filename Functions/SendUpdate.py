import resend
import os 
from dotenv import load_dotenv

def SendUpdate():
    load_dotenv()
    resend.api_key = os.getenv("RESEND_API_KEY")

    r = resend.Emails.send({
        "from": 'onboarding@resend.dev',
        "to": "fsm@heirloomcoffeeroasters.com",
        "subject": "Current Month Newsletter",
        "html": "<p>Current Month's Newsletter has been Sent!<p>"
    })

    return
