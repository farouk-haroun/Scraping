from bs4 import BeautifulSoup
import requests
response = requests.get('https://www.scrapethissite.com/pages/simple/')


def get_countries(html):
    countries_list= []
    soup = BeautifulSoup(html, 'html.parser')
    countries = soup.find_all('h3')
    for country in countries:
        countries_list.append(country.get_text(strip=True))
    return countries_list


print(get_countries(response.text))


