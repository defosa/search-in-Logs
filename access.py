#!/usr/bin/python3


import re

file = open('shop.bacelona.ru.access_log', 'r')
# open the text file
search = "85.174.200.24"
check_list = []
for line in file:
    if search in line:
        time_pattern = re.search('(\d{2}:\d{2})', line)
        check_list.append(time_pattern.group(0))


unique = dict(zip(list(check_list),[check_list.count(i) for i in check_list]))
print(f"Found {search} by minutes : ",unique)