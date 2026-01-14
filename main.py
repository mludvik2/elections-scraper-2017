"""project_3.py: 
third project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""
import sys
import csv
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

def parse_args(argv):
    """
    Checks if the user gives 2 arguments:
    1. The URL
    2. The name of the output CSV file
    Returns both as a tuple (url, filename).
    If something is wrong , it prints out an error and stops the program.
    Possible extensions:
    - Validate that the URL belongs specifically to the volby.cz domain
    - Check that the URL points to a district overview page (not a single town)
    - Prevent overwriting an existing output file
    - Validate that the filename does not contain invalid characters
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
    """
    Downloads and returns the HTML of the given URL.
    """
    print("DOWNLOADING DATA FROM: ", url)
    call_server = requests.get(url)

    if call_server.status_code != 200:
        print("Error: Cannot download code.")
        sys.exit(1)

    return call_server.text

def find_all_links(html, base_url):
    """
    Finds all municipal rows in the main election results table
    and returns a list of dictionaries with code, location, and link.

    Note:
    The first two <tr> rows on the district page contain table headers,
    not municipality data. Therefore, these two rows are skipped using
    a fixed offset (rows[2:]).
    """
    soup = BeautifulSoup(html, "html.parser")
    rows = soup.find_all("tr")[2:]

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

def scrape_town_results(url):
    """
    Gets basic election results (registered, envelopes, valid, parties)
    from one town page.

    Safety check:
    The function verifies that at least one table is present on the page
    before accessing table data.

    Note:
    The election summary table on volby.cz has a fixed structure.
    Specific values are always stored at fixed <td> positions:
    - td[3] → number of registered voters
    - td[4] → number of envelopes issued
    - td[7] → number of valid votes
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("Error loading page:", url)
        return None
    
    soup = BeautifulSoup(response.text, "html.parser")
    tables = soup.find_all("table")
    if not tables:
        print("Warning: No tables found on page:", url)
        return None
    first_table = tables[0]
    all_td = first_table.find_all("td")

    try:
        registered = "".join(all_td[3].get_text(strip=True).split())
        envelopes = "".join(all_td[4].get_text(strip=True).split())
        valid = "".join(all_td[7].get_text(strip=True).split())
    except IndexError:
        print("Warning: could not read vote summary for ", url)
        return None

    parties = {}
    party_tables = soup.find_all("table", {"class": "table"})
    for table in party_tables:
        rows = table.find_all("tr")[2:]
        for row in rows:
            cells = row.find_all("td")
            if len(cells) >= 3:
                party_name = cells[1].get_text(strip=True)
                votes = "".join(cells[2].get_text(strip=True).split())

                if party_name and party_name[0].isalpha():
                    parties[party_name] = votes

    return {
        "registered": registered,
        "envelopes": envelopes,
        "valid": valid,
        "parties": parties
    }

def save_to_csv(data, filename):
    """
    Save results to a CSV file using utf-8-sig and semicolon 
    delimiter for for Excel/Czech locales
    """
    all_parties = []
    for town in data:
        for party in town["parties"].keys():
            if party not in all_parties:
                all_parties.append(party)

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
    """
    Main program execution flow:
    1. Read and validate command-line arguments (district URL and output filename).
    2. Download the main district page with the list of municipalities.
    3. Extract links to individual town result pages.
    - If no links are found, the program prints a warning and exits.
    4. Scrape election results for each town (voters, votes, parties).
    5. Store all collected data in memory.
    6. Save the complete results into a CSV file.
    7. End the program.
    """
    url, filename = parse_args(sys.argv)
    base_url = "https://www.volby.cz/pls/ps2017nss/" 
    html = download_page(url)
    links = find_all_links(html, base_url)
    if not links:
        print("Warning: No links found on the page, exiting.")
        sys.exit(1)

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