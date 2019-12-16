import re

pattern = r'\w+@\w+\.\w+'

sequence = 'bibek_shah01@hotmail.com'

if re.match(pattern, sequence):
    print('email is valid')
else:
    print('email is not valid')