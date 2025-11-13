Czech Election Results Scraper

Author: Michaela Papadimitriu Ludvikova
Email: mludvik2@yahoo.com

Course: Engeto Online Python Academy — Project 3

# Project Description

This project is a Python web scraper that downloads and processes results from the 2017 Czech Parliamentary Elections.
It retrieves data from the official election website volby.cz and saves the results for all municipalities in a selected district into a CSV file.

The output file contains the following information for each municipality:
- Municipality code
- Municipality name
- Number of registered voters
- Number of envelopes issued
- Number of valid votes
- Number of votes for each political party

# How to Run the Program
The program is executed from the command line with two arguments:
(command line in python or open virtual environment??????????)

python project_3.py <URL> <output_file.csv>

## Example Command
python project_3.py "https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xnumnuts=7101" "results_jesenik.csv"

## Command Line Arguments

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

