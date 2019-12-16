import bs4
import requests
import csv

page = requests.get('https://fabpedigree.com/james/mathmen.htm')

soup = bs4.BeautifulSoup(page.content, 'html.parser')

lis = soup.find_all('li')

with open('mathematicians.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, ['sn', 'name'])
    writer.writeheader()

    sn = 1
    for li in lis:
        name = li.a.string
        if not name:
            name = li.a.small.string

        d = {
            'sn': sn,
            'name': name
        }

        writer.writerow(d)

        sn = sn + 1