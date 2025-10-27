import sys
import requests
from bs4 import BeautifulSoup

def print_definition (word):
    url=f"https://dexonline.ro/definitie/{word}"
    headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error: Unable to fetch definition for '{word}'.")
        return  
    soup = BeautifulSoup(response.text, 'html.parser')
    definition_div = soup.find('span', class_='def')
    if definition_div:
        return definition_div.text.strip()
    else:
        print(f"No definition found for '{word}'.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ex06.py <word>")
        sys.exit(1)

    word = sys.argv[1]
    definition = print_definition(word)
    if definition:
        print(f"Definition of '{word}':\n{definition}")