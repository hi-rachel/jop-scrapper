from requests import get
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def extract_wanted_jobs(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)
  
  base_url = "https://www.wanted.co.kr/search?query="
  
  browser.get(f"{base_url}{keyword}")
  
  print("Requesting", f"{base_url}{keyword}")
  soup = BeautifulSoup(browser.page_source, 'html.parser')
  results = []
  jobs = soup.find_all('ul', class_="clearfix")
  for list in jobs:
    job_list = list.find_all('li', recursive=False)
    print(len(job_list))
    for anchors in job_list:
      anchors = list.find_all('a')
      for a in anchors:
        link = a['href']
        title = a.find('div', class_="job-card-position").get_text(),
        company = a.find('div', class_="job-card-company-name").get_text(),
        location = a.find('div', class_="job-card-company-location").get_text()
        job_data = {
          'link' : f"https://www.wanted.co.kr{link}",
          'company' : " ".join(str(x) for x in company).replace(",", " "),
          'location' : " ".join(str(x) for x in location).replace(",", " "),
          'position' : " ".join(str(x) for x in title).replace(",", " "),
        }
        results.append(job_data)
  return results