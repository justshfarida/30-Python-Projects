import csv
import requests
from fake_useragent import UserAgent
from http import HTTPStatus
from typing import List

def get_websites(csvpath: str) -> List[str]:
    websites: list[str] = []
    with open(csvpath, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if "https://" not in row[1]:
                websites.append("https://" + row[1])
            else:
                websites.append(row[1])
    return websites

def get_user_agent() -> str:
    ua = UserAgent()
    return ua.chrome

def get_status_description(statuscode: int) -> str:
    try:
        return f"({statuscode} {HTTPStatus(statuscode).name}) {HTTPStatus(statuscode).description}"
    except ValueError:
        return f"Unknown status code {statuscode}"

def check_website(website: str, user_agent: str):
    try:
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f"Could not get information about: {website}")

def main():
    sites = get_websites('websites.csv')
    user_agent = get_user_agent()

    for site in sites:
        check_website(site, user_agent)

if __name__ == '__main__':
    main()
