from bs4 import BeautifulSoup
import requests
import json

page = requests.get('https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population')
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')
all_tr = table.find_all('tr')

countries = []
populations = []
proportions = []
for i in all_tr[2:]:
    countries.append(i.find('a').string)
    populations.append(int(i.find_all('td')[2].string.replace(',', '')))
    for j in i.find_all('td')[3].strings:
        proportions.append(float(j.strip('\n').strip('%%')))

population_dict = {}
for i in range(len(countries)):
    population_dict[countries[i]] = [populations[i], proportions[i]]

with open('world_population.json', 'w') as f:
    json.dump(population_dict, f, indent=4)