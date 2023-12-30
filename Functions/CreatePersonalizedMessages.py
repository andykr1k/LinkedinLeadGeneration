import os
from dotenv import load_dotenv
from openai import OpenAI

newsletter = "Welcome to the first edition of Heirloom Coffee Roasters' newsletter! As a valued member of our community, you're at the forefront of a revolution in the world of regenerative coffee - where exceptional taste and uncompromising sustainability go hand in hand.The future of sustainable coffee At Heirloom, we aim to revolutionize the foodservice industry by roasting 100% regeneratively farmed, organic coffees. Our award-winning culinary roasting style is changing the way competition-grade coffee is distributed on campus and proving that hyper-sustainable, culinary-style coffee can be served at scale.Changing the definition of quality on campus We created Heirloom Coffee Roasters to be a beacon of change in the coffee industry. Our commitment is twofold: to bring you an unrivaled coffee experience and to do it in a way that respects and rejuvenates the earth. Every bean we roast and every cup we brew is a testament to our dedication to quality, sustainability, and the art of true coffee craftsmanship. The road ahead As we embark on this journey together, our newsletters will serve as your monthly guide to the world of Heirloom Coffee Roasters. Expect to dive deep into topics like regenerative coffee practices, our efforts to reduce waste, and, of course, the rich, nuanced flavors of our award-winning coffee. We’ll share stories from our campuses, insights from the field, and exclusive tips on brewing the perfect cup.We are thrilled to have you with us as we chart a course toward a more sustainable and delicious coffee future. Here’s to many great cups of coffee and impactful conversations! Warm regards, Hovik Azadkhanian CEO & Co-founder Heirloom Coffee Roasters P.S. We love hearing from our community. Feel free to reply to this email with your thoughts, questions, or just to share your favorite coffee moment. Let\'s brew a better world together!"

def CreatePersonalizedMessages(status, data):
    load_dotenv()
    CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")
    
    client = OpenAI(api_key=CHATGPT_API_KEY)

    for idx, person in enumerate(data):
        content = "Newsletter: \n" + newsletter + "\n Profile: \n" + person

        response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant who takes in Linkedin profile data and creates a personalized welcome paragraph to Heirloom Coffee's monthly regenerative coffee newsletter."},
            {"role": "user", "content": content},
        ])

        res = response.choices[0].message.content.splitlines()

        # print(res[0])
        # print(res[2])
        data[idx]['personalized_welcome_start'] = res[0]
        data[idx]['personalized_welcome_paragraph'] = res[2]

    status['GetPersonalizedEmails']['status'] = True
    
    return data