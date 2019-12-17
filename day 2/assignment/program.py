import re

with open('genius club.txt') as file:
    content = file.read()
    pattern = '\+\d+-\d+'

    phones = re.findall(pattern, content)
    for phone in phones:
        print(phone)