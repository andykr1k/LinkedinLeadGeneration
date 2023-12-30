import os
from dotenv import load_dotenv
from openai import OpenAI

newsletter = "Welcome to the first edition of Heirloom Coffee Roasters' newsletter! As a valued member of our community, you're at the forefront of a revolution in the world of regenerative coffee - where exceptional taste and uncompromising sustainability go hand in hand.The future of sustainable coffee At Heirloom, we aim to revolutionize the foodservice industry by roasting 100% regeneratively farmed, organic coffees. Our award-winning culinary roasting style is changing the way competition-grade coffee is distributed on campus and proving that hyper-sustainable, culinary-style coffee can be served at scale.Changing the definition of quality on campus We created Heirloom Coffee Roasters to be a beacon of change in the coffee industry. Our commitment is twofold: to bring you an unrivaled coffee experience and to do it in a way that respects and rejuvenates the earth. Every bean we roast and every cup we brew is a testament to our dedication to quality, sustainability, and the art of true coffee craftsmanship. The road ahead As we embark on this journey together, our newsletters will serve as your monthly guide to the world of Heirloom Coffee Roasters. Expect to dive deep into topics like regenerative coffee practices, our efforts to reduce waste, and, of course, the rich, nuanced flavors of our award-winning coffee. We’ll share stories from our campuses, insights from the field, and exclusive tips on brewing the perfect cup.We are thrilled to have you with us as we chart a course toward a more sustainable and delicious coffee future. Here’s to many great cups of coffee and impactful conversations! Warm regards, Hovik Azadkhanian CEO & Co-founder Heirloom Coffee Roasters P.S. We love hearing from our community. Feel free to reply to this email with your thoughts, questions, or just to share your favorite coffee moment. Let\'s brew a better world together!"

person = [{'about': 'David Wei is an intrapreneur in digital era. He is passionate about creating client values, unlocking internal & external business opportunities, and delivering customer outcomes through digital transformation and innovations. Over the past 20+ years, David has served globally across various sectors including Finance, Manufacturing, Healthcare, Life Science, ICT, Consumer Goods, Natural Resources, and Logistics. He is focused on organizational transition, IT planning & operation, digital strategy & execution, modeling, and digital technologies (AI, big data, cloud, interactive, analytics, etc).', 'city': 'Overland Park', 'company': 'PING AN INSURANCE(GROUP) COMPANY OF CHINA,LTD', 'company_domain': 'property.pingan.com', 'company_employee_range': '10000+', 'company_id': '41507535', 'company_industry': 'Insurance', 'company_linkedin_url': 'https://www.linkedin.com/company/pingan-property-insurance-company', 'company_logo_url': 'https://media.licdn.com/dms/image/C560BAQFKgfXtN55wLA/company-logo_400_400/0/1630667341307/pingan_property_insurance_company_logo?e=1710979200&v=beta&t=9WAQ-I_bvGHwxv-20g2YeDm5-Nk0-2yO4BIKfbnJ3_8', 'company_website': 'https://property.pingan.com', 'company_year_founded': 1988, 'country': 'United States', 'current_company_join_month': 8, 'current_company_join_year': 2020, 'educations': [{'activities': '', 'date_range': '', 'degree': 'Master', 'description': '', 'eduId': 7673104, 'end_month': '', 'end_year': '', 'field_of_study': 'Computer Science', 'grade': '', 'school': 'University of Illinois', 'school_id': '', 'school_linkedin_url': '', 'start_month': '', 'start_year': ''}, {'activities': '', 'date_range': '', 'degree': 'BS', 'description': '', 'eduId': 55922577, 'end_month': '', 'end_year': '', 'field_of_study': 'Electrical Engineering', 'grade': '', 'school': "Xi'an Jiaotong University", 'school_id': '424280', 'school_linkedin_url': 'https://www.linkedin.com/company/424280/', 'start_month': '', 'start_year': ''}, {'activities': '', 'date_range': '', 'degree': 'Ph.D Candidate', 'description': '', 'eduId': 81482802, 'end_month': '', 'end_year': '', 'field_of_study': 'Electrical Engineering - Signal/Image Processing', 'grade': '', 'school': "Xi'an Jiaotong University", 'school_id': '424280', 'school_linkedin_url': 'https://www.linkedin.com/company/424280/', 'start_month': '', 'start_year': ''}], 'experiences': [{'company': 'PING AN INSURANCE(GROUP) COMPANY OF CHINA,LTD', 'company_id': '41507535', 'company_linkedin_url': 'https://www.linkedin.com/company/41507535', 'current_company_join_month': 8, 'current_company_join_year': 2020, 'date_range': 'Aug 2020 - present', 'description': '• Lead develop & execute group\'s digital transformation strategy, serving marketing & sales divisions, agents, and customers;\n• Build the Enterprise Sales & Agency Operations Platform to serve a million agents crossing sales distribution channels;\n• Define an overall technical data strategy based on DAMA to ensure high performance of data management and utilizations;\n• Lead AIGC, LLM technology initiatives as "AIGC Follow Me", "AI Screening", "AI Sales Assistant" to foster business growth;\n• Lead 4 IT departments of software developments, big data, AI, and 3rd party players, a total of 1,000 resources at peak time;', 'duration': '3 yrs 5 mos', 'end_month': '', 'end_year': '', 'is_current': True, 'location': '', 'start_month': 8, 'start_year': 2020, 'title': 'Head Office Director of R&D'}, {'company': 'Ping An Technology', 'company_id': '10881605', 'company_linkedin_url': 'https://www.linkedin.com/company/10881605', 'date_range': 'Apr 2020 - Jul 2020', 'description': "• Lead develop & execute group's digital transformation strategy, serving marketing & sales divisions, agents, and customers;\n• Partner with business leadership to implement the Omni-channel Innovation Program, supporting corporate objectives", 'duration': '4 mos', 'end_month': 7, 'end_year': 2020, 'is_current': False, 'location': '', 'start_month': 4, 'start_year': 2020, 'title': 'Chief Director of Digital Platform'}, {'company': 'Dian Diagnostics Group Co., Ltd. (300244.SZ)', 'company_id': '', 'company_linkedin_url': '', 'date_range': 'Aug 2016 - Mar 2020', 'description': '• Develop corporate digital strategy and programs, lead digital innovations, build core competencies & digital platforms;\n• Serve as key member of Governance Committee, Technology Innovation Committee, Culture & Stewardship Committee;\n• Lead oversea biotech technology transfer and localization practices, lead diagnostic analytics and smart healthcare initiatives;\n• Lead a world-leading genomic profiling and molecular insights cloud platform\'s transfer to China & unlocked a new business;\n• Lead development of "AI Aided TCT Screening System" and "AI Aided Pathology Dissection/Accessioning System";\n• Shift a traditional & "linear" shadowing IT organization to a fast-failing & continuous-learning organization with purpose;', 'duration': '3 yrs 8 mos', 'end_month': 3, 'end_year': 2020, 'is_current': False, 'location': 'China', 'start_month': 8, 'start_year': 2016, 'title': 'CIO & Group Vice President'}, {'company': 'Accenture', 'company_id': '1033', 'company_linkedin_url': 'https://www.linkedin.com/company/1033', 'date_range': 'Oct 2014 - Jul 2016', 'description': '• Set up from scratch DDI as an integral part of Accenture Digital, design offerings and growth strategy, build capabilities;\n• Took charge of DDI budgeting, forecasting, staffing, etc, monitor DDI client engagements, lead deliver key client projects;\n• Defined and execute the new direct-to-market collaboration model with industry teams, expand key partner alliances;\n• Oversaw pipeline, discover client opportunities, funnel value propositions through digital solutions, engage client C-levels;', 'duration': '1 yr 10 mos', 'end_month': 7, 'end_year': 2016, 'is_current': False, 'location': '', 'start_month': 10, 'start_year': 2014, 'title': 'Founder of Digital Delivery Interactive (DDI) | Accenture (Greater China)'}, {'company': 'Accenture', 'company_id': '', 'company_linkedin_url': '', 'date_range': 'Jun 2007 - Oct 2014', 'description': '• Co-lead eCommerce practices and drive digital revenue growth through eCommerce/digital marketing/content offerings;\n• Provide technical leadership and business development services to digital projects across countries, industries, and units;\n• Build digital capabilities, serve as corporate eCommerce SME (subject matter expert), strengthen tech-firm partnerships;\n• Lead deliver a variety of eCommerce projects to help clients go live omni-channel strategies and digital transformations;', 'duration': '7 yrs 5 mos', 'end_month': 10, 'end_year': 2014, 'is_current': False, 'location': '', 'start_month': 6, 'start_year': 2007, 'title': 'Sr. Manager - USA'}, {'company': 'IT Consulting (Capgemini E&Y...)', 'company_id': '', 'company_linkedin_url': '', 'date_range': 'Jan 2000 - Jun 2007', 'description': '• Analyze, design, integrate, and develop Internet technology based order management systems, billing systems, CRM systems, BPM systems, and finance reporting systems. Focus on enterprise solution, service-oriented architecture, and large scale complex system implementation. Most of clients are from Fortune 500 companies in ICT, entertainment, retail industry sectors;', 'duration': '7 yrs 6 mos', 'end_month': 6, 'end_year': 2007, 'is_current': False, 'location': 'Various', 'start_month': 1, 'start_year': 2000, 'title': 'PM, Lead, Consultant - USA'}], 'first_name': 'David', 'full_name': 'David Wei', 'headline': 'Advisory Consultancy | AI | Digital Transformation | Innovations | IT Services & Enterprise Architecture', 'hq_city': 'Guangzhou', 'hq_country': 'CN', 'hq_region': '', 'job_title': 'Head Office Director of R&D', 'last_name': 'Wei', 'linkedin_url': 'https://www.linkedin.com/in/david-wei-9099823', 'location': 'Overland Park, Kansas, United States', 'profile_id': '', 'profile_image_url': 'https://media.licdn.com/dms/image/D5603AQHsb137SYKsOg/profile-displayphoto-shrink_800_800/0/1691652106961?e=1708560000&v=beta&t=f6PtFH8aEXTuIXUFBeXB8M-4yFjBUkmvNe3P5vXHxvo', 'public_id': 'david-wei-9099823', 'school': 'University of Illinois', 'state': 'Kansas', 'personal_email': 'david.wei@accenture.com'}]

def CreatePersonalizedMessages(person):
    load_dotenv()
    CHATGPT_API_KEY = os.getenv("CHATGPT_API_KEY")

    client = OpenAI(api_key=CHATGPT_API_KEY)

    content = "Newsletter: \n" + newsletter + "\n Profile: \n" + str(person)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Act as a confident marketing writer with extensive experience in writing newsletters that catch someone’s attention from the first few sentences. Use “We” instead of “I” where needed. I will give you a newsletter called Newsletter and a json object called Profile with linkedin profile data. You start by writing Dear [Full Name], and then write one paragraph tying them to why they should join this newsletter. This will be appended to the beginning of the newsletter. Make sure to keep it at 100 words maximum."},
            {"role": "user", "content": content},
        ])

    res = response.choices[0].message.content.splitlines()

    print(res[0])
    print(res[2])

    return

CreatePersonalizedMessages(person)