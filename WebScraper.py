from bs4 import BeautifulSoup
import requests

URL = "https://sfbay.craigslist.org/d/artists/search/ats"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html_parser")
results = soup.find(id="search-results")
result_element = results.find_all("li", class-"result-row")

for result in result_element:
    title = result.find("h3", class="result-heading")
    print(title.text.strip())