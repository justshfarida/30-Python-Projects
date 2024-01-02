import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus
from typing import List

def get_websites(csvpath: str) -> List[str]:
    websites: list[str]=[]
    with open (csvpath, 'r') as file:
        reader=csv.reader(file)
        for row in reader:
            if "https://" not in row[1]:
                websites.append("https://"+row[1])
            else:
                websites.append(row[1])
    return websites
print(get_websites("websites.csv"))
def get_user_agent()->str:
    ua=UserAgent
    return ua.firefox
print(get_user_agent())