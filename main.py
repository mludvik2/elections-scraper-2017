#Ethical reminder
#Check and respect the site’s robots.txt.
#Don’t send too many requests too fast.
#Data from public elections is open, but you should scrape responsibly.
##can you see this?

"""project_3.py: 
third project for Engeto Online Python Academy

Author: Michaela Papadimitriu Ludvikova
email: mludvik2@yahoo.com
"""

from bs4 import BeautifulSoup
import requests
import sys

def parse_args(argv):
    """Checks if the user gives 2 arguments:
    1. The district URL
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
### we want not both to have an issue but if one then other is ok
    if not url.startswith("http") or not filename.endswith(".csv"):
        print("Error: The first argument must be a web link (URL).")
        print("Error: The second argument must end with .csv")
        sys.exit(1)

    return url, filename

def download_page(url):
    """Downloads and returns the HTML of the given URL."""
    print("Downloading data from :", url)
    call_server = requests.get(url)

    if call_server.status_code != 200:
        print("Error: Cannot download code.")
        sys.exit()

    return call_server.text

if __name__ == "__main__":
    url, filename = parse_args(sys.argv)
    #print("URL:", url)
    #print("File name:", filename)
    #download page
    html = download_page(url)
    #parse with beautifulsoup
    soup = BeautifulSoup(html, "html.parser")
    #just show the page title to test
    title = soup.find("title").get_text()
    print("Page title:", title)


