import os
import mailchimp_transactional as MailchimpTransactional
from mailchimp_transactional.api_client import ApiClientError
from dotenv import load_dotenv
from supabase import create_client, Client
import pandas as pd
from datetime import datetime

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_API_KEY")
supabase: Client = create_client(url, key)

newsletter_start = "<html lang=\"en\"><head><meta charset=\"UTF-8\"><meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"><title>Draft Sample – Welcome to our newsletter</title><style>body {font-family: Arial, sans-serif;line-height: 1.6;margin: 20px;}h1 {color: #333;}p {color: #666;}.image-container {height: 200px;overflow: hidden;}img {width: 100%;height: 100%;object-fit: cover;object-position: top;display: block;}signature {font-style: italic;color: #666;}.button-container {margin-top: 20px;}.button {display: inline-block;padding: 10px 20px;font-size: 16px;text-align: center;text-decoration: none;background-color: #3498db;color: #fff;border-radius: 5px;transition: transform 0.3s;}.button:hover {transform: scale(1.1);}.button + .button {margin-left: 10px;}</style></head><body><div class=\"image-container\"><img src=\"background.webp\" alt=\"Heirloom Coffee Roasters\" /></div><h1>An Invitation To Our Newsletter - Heirloom Coffee Roaster's</h1>"

newsletter_end = "<h2>The future of sustainable coffee</h2><p>At Heirloom, we aim to revolutionize the foodservice industry by roasting 100% regeneratively farmed, organic coffees. Our award-winning culinary roasting style is changing the way competition-grade coffee is distributed on campus and proving that hyper-sustainable, culinary-style coffee can be served at scale.</p><h2>Changing the definition of quality on campus</h2><p>We created Heirloom Coffee Roasters to be a beacon of change in the coffee industry. Our commitment is twofold: to bring you an unrivaled coffee experience and to do it in a way that respects and rejuvenates the earth. Every bean we roast and every cup we brew is a testament to our dedication to quality, sustainability, and the art of true coffee craftsmanship.</p><h2>The road ahead</h2><p>As we embark on this journey together, our newsletters will serve as your monthly guide to the world of Heirloom Coffee Roasters. Expect to dive deep into topics like regenerative coffee practices, our efforts to reduce waste, and, of course, the rich, nuanced flavors of our award-winning coffee. We’ll share stories from our campuses, insights from the field, and exclusive tips on brewing the perfect cup.</p><p>We are thrilled to have you with us as we chart a course toward a more sustainable and delicious coffee future. Here’s to many great cups of coffee and impactful conversations!</p><p>Warm regards,</p><signature>Hovik Azadkhanian<br>CEO & Co-founder<br>Heirloom Coffee Roasters</signature><p>P.S. We love hearing from our community. Feel free to reply to this email with your thoughts, questions, or just to share your favorite coffee moment. Let\'s brew a better world together!</p><div class=\"button-container\"><a href=\"mailto:fsm@heirloomcoffeeroasters.com\" class=\"button\">Contact Me</a><a href=\"https://heirloomcoffeeroasters.com/\" class=\"button\" target=\"_blank\">Visit Website</a></div></body></html>"

def SendEmails(status):
    load_dotenv()
    key = os.environ.get("MAILCHIMP_API_KEY")

    mailchimp = MailchimpTransactional.Client(key)
    
    f = open(
        os.path.join(os.path.dirname(__file__), "../background.webp"), "rb"
    ).read()
    
    response = supabase.table('FoodServiceManagers').select("*").execute()
    df = response.data

    df['created_at'] = pd.to_datetime(df['created_at'])
    current_month = datetime.now().month

    f = open(
        os.path.join(os.path.dirname(__file__), "../background.webp"), "rb"
    ).read()

    for person in df:
        if df['welcome_sent'] == False and df['personal_email'] != None:
            message = {
                "from_email": "fsm@heirloomcoffeeroasters.com",
                "subject": "An Invitation To Our Newsletter - Heirloom Coffee Roaster's",
                "html": newsletter_start + "<p>" + df['personalized_dear'] + "</p>" + "<p>" + df['personalized_welcome'] + "</p>" + newsletter_end,
                "to": [
                    {
                        "email": "it@heirloomcoffeeroasters.com",
                        "type": "to"
                    }
                ],
                "attachments": [{"name": "background.webp", "type":"webp", "content": list(f)}]
            }
            data, count = supabase.table('FoodServiceManagers').update({'welcome_sent': True}).eq('personal_email', df['personal_email']).execute()

    status['SendEmails']['status'] = True
    
    return