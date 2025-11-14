# Czech Election Results Scraper

**Author:** Michaela Papadimitriu Ludvikova<br> 
**Email:** mludvik2@yahoo.com<br>
**Course:** Engeto Online Python Academy — Project 3<br> 

## Project Description

This project is a **Python web scraper** that downloads and processes results from the **2017 Czech Parliamentary Elections**.
It retrieves data from the official election website [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) and saves the results for all municipalities in a selected district into a **CSV file**, which you can open in Excel.

## What it does:<br>
When you run the program, it:<br>
1. Takes a district URL from the Czech election site.<br>
2. Downloads results for all towns in that district.<br>
3. Saves everything into a CSV file (which you can open in Excel).<br>

The output file contains the following information for each municipality:<br>
- Town code<br>
- Town name<br>
- Number of registered voters<br>
- Number of envelopes issued<br>
- Number of valid votes<br>
- Number of votes for each political party<br>

### What you need<br>
- Python 3 installed<br>
- A code editor (like VS Code)<br>

## Step-by-step instructions<br>
**Step 1: Download this project to your own computer so you can open and run it locally.**<br>
**Option 1: Download ZIP**<br>
1. Go to the project’s page on GitHub: [Election-Scraper-2017](https://github.com/mludvik2/elections-scraper-2017/tree/main)<br>
2. Find the green **“Code”** button near the top right.<br>
3. Click **“Download ZIP.”**<br>
4. A file like elections-scraper-2017.zip will download to your computer (usually in your Downloads folder).<br>
5. Right-click that ZIP file and choose **“Extract All…”** (Windows).<br>
6. You’ll now have a regular folder named elections-scraper-2017.<br>

Move that folder somewhere easy to find, such as: "C:\Users\YourName\Documents\elections-scraper-2017"<br>

**Option 2: Clone using Git**<br>
If you already have Git installed and know how to use the terminal, you can instead run:<br>
git clone https://github.com/mludvik2/elections-scraper-2017.git<br>

**Step 2: Open a terminal**<br>
Go to where you moved the file to eg. "C:\Users\YourName\Documents\elections-scraper-2017"<br>
Type in **"CMD"** where your file is listed and hit enter<br>

**Step 3: Create and activate a virtual environment**<br>
add in code **separately**:<br>
python -m venv .venv<br>
.venv\Scripts\activate<br>

You’ll see:<br>
(.venv) at the start of your line — that means it’s active.<br>

**Step 4: Install the required packages**<br>
Run:<br>
pip install -r requirements.txt<br>

This installs the libraries the project needs (requests and beautifulsoup4).<br>

**Step 5: Run the Program**<br>
Use this command format:<br>
python main.py "district page URL" "output_filename.csv"<br>

**Command Line Arguments**<br>
**District page URL:** The first part is the election district URL **(with many towns)**. Do not use a single town page — it should be a list of towns.<br>
**Output_file.csv:** The second part is the CSV file name you want to create.<br>

For example:<br>
python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101" "Jesenik_results.csv"<br>

**Step 6: Wait for the scraper to finish**<br>
After the program finishes, you’ll see a message like:<br>
Data saved successfully to 'Jesenik_results.csv'<br>

**Example CSV file:** [Jesenik_results.csv](https://github.com/mludvik2/elections-scraper-2017/blob/main/Jesenik_results.csv)<br>

**Step 7: Open the CSV file you have run**<br>
Open it with Excel.<br>
Each row represents one municipality, and every political party appears as a separate column.<br>

### Data Cleaning<br>
- Extra spaces in numbers (e.g. 1 546) are automatically removed → 1546<br>
- Missing values for a party are replaced by "0"<br>
- The CSV file uses the **semicolon (;)** as a delimiter for better compatibility with Excel<br>
- Czech characters are preserved using **utf-8-sig**<br>

### Notes<br>
- Use a district page URL (one that lists multiple towns), not a single-town page.<br>
- The program scrapes responsibly — it makes a few requests, not too fast.<br>
- Only public data is used (from official government pages).<br>

!!!add in links to other files



### Author<br>
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

