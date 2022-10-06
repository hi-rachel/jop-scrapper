import requests
from requests import get
from bs4 import BeautifulSoup

def extract_remote_jobs(keyword):
    headers = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}
  
    base_url = "https://remoteok.com"

    final_url = f"{base_url}/remote-{keyword}-jobs"

    html = requests.get(final_url, headers=headers).text
  
    results = []
  
    print("Requesting", f"{base_url}-{keyword}-jobs")
    soup = BeautifulSoup(html, 'html.parser')
    jobs = soup.find_all('td', class_="company_and_position")
    print(len(jobs))
    filtered_jobs = list(filter(None, jobs))
    for job in filtered_jobs:
      anchors = job.find_all('a', class_='preventLink')
      location_area = job.find('div', class_='location')
      company_area = job.find_all('span', class_="companyLink")
      for company in company_area:
        company = company.find('h3').get_text()
      if anchors != None:
        for a in anchors:
          link = a['href']
          title = job.find('h2').get_text()
          job_data = {
            'link': f"{base_url}{link}",
            'company' : "".join(str(x) for x in company).replace(",", "").replace("\n", ""),
            'location' : "".join(str(x) for x in location_area).replace(",", ""),
            'position' : "".join(str(x) for x in title).replace("\n", ""),
          }
          results.append(job_data)
    return results