# Czech Election Results Scraper

**Author:** Michaela Papadimitriu Ludvikova<br> 
**Email:** mludvik2@yahoo.com<br>
**Course:** Engeto Online Python Academy — Project 3<br> 

## Project Description

This project is a **Python web scraper** that downloads and processes results from the **2017 Czech Parliamentary Elections**.
It retrieves data from the official election website [volby.cz](https://www.volby.cz/) and saves the results for all municipalities in a selected district into a **CSV file**, which you can open in Excel.

The output file contains the following information for each municipality:
- Town code
- Town name
- Number of registered voters
- Number of envelopes issued
- Number of valid votes
- Number of votes for each political party

## How to Run the Program
**Step 1: Open the command line (CMD or Terminal)**
**Step 2: Go to the folder where your file is saved**
For example:
cd C:\Users\YourName\Documents\elections-scraper-2017
**Step 3: Run this command**
python main.py <URL> <output_file.csv>
python main.py "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xnumnuts=7101" "results_jesenik.csv"

**Command Line Arguments**
<URL> Link to the district overview page from volby.cz(do not use a single town page — it should be a list of towns).
<output_file.csv> Name of the CSV file where results will be saved

After the program finishes, you’ll see a message like:
Data saved successfully to 'results_jesenik.csv'


### Example Output
After running the program, a CSV file is created — for example:
**File name:** results_jesenik.csv
**Structure of the file**:
Code;Town;Registered;Envelopes;Valid;Občanská demokratická strana;...;ANO 2011;...
523917;Bělá pod Pradědem;1546;945;938;77;...;331;...
524891;Bernartice;703;344;343;24;...;149;...
...

Each row represents one municipality, and every political party appears as a separate column.
You can open this file in Excel to view and analyze the results.

### What you need
- Python 3 installed
- The following libraries:
	- requests
	- beautifulsoup4
in command prompt or terminalpip install requests beautifulsoup4


main_3.py      # main program file
README.md      # this documentation file

### Data Cleaning
Before saving the results:
- Extra spaces in numbers (e.g. 1 546) are automatically removed → 1546
- Missing values for a party are replaced by "0"
- The CSV file uses the **semicolon (;)** as a delimiter for better compatibility with Excel
- Czech characters are preserved using **utf-8-sig**

### Ethical and Legal Notice
- The scraper follows [volby.cz](https://www.volby.cz/)’s terms and robots.txt.**(Respect the website’s rules)**
- It sends a small number of requests and includes respectful pauses between them if needed.
- The scraped data comes from **publicly available election results** and is used strictly for **educational purposes**.

### Requirements
- Python 3.x
- Installed libraries:
	- requests
	- beautifulsoup4

#### Installation:
pip install requests beautifulsoup4

### Author
**Michaela Papadimitriu Ludvikova**<br>
**email:** mludvik2@yahoo.com<br>
Engeto Online Python Academy — Project 3<br>








### Structure of the file:


# Structure:

* main.py


write info for people who do or do not have: delimiter ","
  with open(filename, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.writer(f, delimiter=";"




\#Ethical reminder

\#Check and respect the site’s robots.txt.

\#Don’t send too many requests too fast.

\#Data from public elections is open, but you should scrape responsibly.





rows = soup.find\_all("tr")\[2:] # skip first 2 header rows





\#Base URL to build full links



\# Send request and parse HTML



&nbsp;   #find numbers of voters, envelopes, valid votes

&nbsp;   #these are inside <td> cells on the first table



&nbsp;   #return the results as a dictionary



1352587



23447817



the CSV file has wrong Czech characters (like Å½ulovÃ¡ instead of Žulová).



That’s an encoding issue, caused by Excel not reading UTF-8 properly.



Here’s how to fix it 👇



✅ Option 1 (best for Excel)



Change this line:



with open(filename, "w", newline="", encoding="utf-8") as f:





to this:



with open(filename, "w", newline="", encoding="utf-8-sig") as f:





That small change adds a UTF-8 signature (BOM) at the start of the file — Excel will then open it with correct Czech characters like Žulová, Červená, Šumperk, etc.



✅ Option 2 (open correctly in Excel)



If you keep utf-8, then open the CSV manually in Excel like this:



Open Excel



Go to Data → Get Data → From Text/CSV



Choose your file



In the import window, set File Origin = UTF-8



Click Load

