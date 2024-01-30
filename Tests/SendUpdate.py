import resend
import os
from dotenv import load_dotenv

def SendUpdate():
    load_dotenv()
    resend.api_key = os.getenv("RESEND_API_KEY")

    r = resend.Emails.send({
        "from": 'onboarding@resend.dev',
        "to": "it@heirloomcoffeeroasters.com",
        "subject": "Current Month FSM has been ran!",
        "html": "<p>Current Month FSM has been ran!<p>"
    })

    return