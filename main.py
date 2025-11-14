#Ethical reminder
#Check and respect the site’s robots.txt.
#Don’t send too many requests too fast.
#Data from public elections is open, but you should scrape responsibly.


"""project_3.py: 
third project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""
from bs4 import BeautifulSoup
import requests
import sys
from urllib.parse import urljoin
import csv

def parse_args(argv):
    """Checks if the user gives 2 arguments:
    1. The URL
    2. The name of the output CSV file
    Returns both as a tuple (url, filename).
    If something is wrong , it prints out an error and stops the program.
    """
    if len(argv) != 3:
        print("Error: You must give 2 arguments!")
        print("Example: python main.py <url> <output_file.csv>")
        sys.exit(1)
    
    url = argv[1]
    filename = argv[2]
    if not url.startswith("http") or not filename.endswith(".csv"):
        print("Error: Please give a valid URL and a file ending with .csv.")
        sys.exit(1)

    return url, filename

def download_page(url):
    """Downloads and returns the HTML of the given URL."""
    print("DOWNLOADING DATA FROM: ", url)
    call_server = requests.get(url)

    if call_server.status_code != 200:
        print("Error: Cannot download code.")
        sys.exit()

    return call_server.text

def find_all_links(html, base_url):
    """
    Finds all municipal rows in the main table
    and returns a list of dictionaries with code, location and link
    """
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("tr")[2:] # skip first 2 header rows

    all_links = []

    for row in rows:
        cells = row.find_all("td")
        if len(cells) > 0:
            number_link = cells[0].find("a")
            location = cells[1].get_text(strip=True)

            if number_link:
                detail_href = number_link.get("href")
                full_link = urljoin(base_url, detail_href)
                code = number_link.get_text(strip=True)

                all_links.append({
                    "code": code,
                    "location": location,
                    "link": full_link
            })

    
    return all_links

#Base URL to build full links

# Send request and parse HTML
def scrape_town_results(url):
    """
    Gets basic election results (registered, envelopes, valid, parties)
     from one town page.
    """
    #download the page
    response = requests.get(url)
    if response.status_code != 200:
        print("Error loading page:", url)
        return None
    
    #parse the page
    soup = BeautifulSoup(response.text, "html.parser")
    #find numbers of voters, envelopes, valid votes
    #these are inside <td> cells on the first table
    tables = soup.find_all("table")
    first_table = tables[0]
    all_td = first_table.find_all("td")

    try:
        registered = "".join(all_td[3].get_text(strip=True).split())
        envelopes = "".join(all_td[4].get_text(strip=True).split())
        valid = "".join(all_td[7].get_text(strip=True).split())
    except IndexError:
        print("Warning: could not read vote summary for ", url)
        return None

    #Find all political parties and their votes

    parties = {}
    party_tables = soup.find_all("table", {"class": "table"})
    for table in party_tables:
        rows = table.find_all("tr")[2:]  #skip 2 header rows
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 3:
                party_name = cells[1].get_text(strip=True)
                votes = "".join(cells[2].get_text(strip=True).split())

                if party_name and party_name[0].isalpha():
                    parties[party_name] = votes

    #return the results as a dictionary
    return{
        "registered": registered,
        "envelopes": envelopes,
        "valid": valid,
        "parties": parties
    }

#save everything to csv
def save_to_csv(data, filename):
    """Save results to a CSV file"""
    #get all the unique party names across all towns
    all_parties = []
    for town in data:
        for party in town["parties"].keys():
            if party not in all_parties:
                all_parties.append(party)

    #create csv header
    header = ["Code", "Town", "Registered", "Envelopes", "Valid"] + all_parties

    with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";")
        writer.writerow(header)

        for town in data:
            row = [
                town["code"],
                town["location"],
                town["registered"],
                town["envelopes"],
                town["valid"]
            ]
            for party in all_parties:
                if party in town["parties"]:
                    row.append(town["parties"][party])
                else:
                    row.append("0")
            writer.writerow(row)
    print(f"DATA SAVED SUCCESSFULLY TO: '{filename}'")

if __name__ == "__main__":
    url, filename = parse_args(sys.argv)
    base_url = "https://www.volby.cz/pls/ps2017nss/" 
    
   
    #download page
    html = download_page(url)
    #find links
    links = find_all_links(html, base_url)
    

     # Test: scrape first 3 towns only
    all_data = []
    for town in links:
        result = scrape_town_results(town["link"])

        if result is not None:
            town_data = {
                "code": town["code"],
                "location": town["location"],
                "registered": result["registered"],
                "envelopes": result["envelopes"],
                "valid": result["valid"],
                "parties": result["parties"]
            }
            all_data.append(town_data)
                
    save_to_csv(all_data, filename)
    print("EXITING Election-Scraper-2017")



