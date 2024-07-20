from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=ft&searchTextText=&txtKeywords=Python&txtLocation=').text
# print(html_text)
soup = BeautifulSoup(html_text,'lxml')
# print(soup)
# jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
# print(jobs)

# job = soup.find('li',class_='clearfix job-bx wht-shd-bx')
# print(job)
# company_name = job.find('h3',class_='joblist-comp-name').text.strip().title()
# print(company_name)

# skills = job.find('span',class_='srp-skills').text.strip().replace(" ","").title()
# print(skills)

# published_date = job.find('span',class_='sim-posted').span.text
# print(published_date)


jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
company_list = []
skills_list = []
for job in jobs:
    published_date = job.find('span', class_='sim-posted').span.text
    try:
        days = int(published_date.split()[1])
        # print(days, type(days))
    except ValueError:
        print(end='')

    if days < 10:
        company_name = job.find('h3', class_='joblist-comp-name').text.strip().title()
        company_list.append(company_name)

        skills = job.find('span',class_='srp-skills').text.strip().replace(" ","").title()
        skills_list.append(skills)

        more_info = job.header.h2.a['href']

        print(f"Company Name : {company_name}")
        print(f"Required Skills : {skills}")
        print(f"Published Date : {published_date}")
        print(more_info)
        print(end='\n')

# print(len(company_list))
# print(len(skills_list))



