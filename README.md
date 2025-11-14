# Czech Election Results Scraper<br>

**Author:** Michaela Papadimitriu Ludvikova<br> 
**Email:** mludvik2@yahoo.com<br>
**Course:** Engeto Online Python Academy — Project 3<br> 

## Project Description<br>

This project is a **Python web scraper** that downloads and processes results from the **2017 Czech Parliamentary Elections**.
It retrieves data from the official election website [volby.cz](https://www.volby.cz/pls/ps2017nss/ps3?xjazyk=CZ) and saves the results for all municipalities in a selected district into a **CSV file**, which you can open in Excel.

## Installation of required libraries<br>
The libraries used in this project are listed in the `requirements.txt` file. It is recommended to install them inside a new virtual environment. After activating the environment, install the libraries using the following commands:<br>
>```
> $ pip3 --version                     # checks that pip is installed and shows its version
> $ pip3 install -r requirements.txt   # installs the libraries listed in requirements.txt
>```

## Run the Program<br>
Run the program `main.py` in the command line using 2 mandatory arguments:<br>
>```
> python main.py <district page URL> <output_filename>
>```

The program will download the results with a suffix `.csv `.

## An example of the project
The voting results for town of Jesenik:
1. argument: `https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101`
2. argument: `Jesenik_results`

Run program:
>```
> python main.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101" "Jesenik_results.csv"
>```

Download progress:
>```
> DOWNLOADING DATA FROM:  https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=12&xnumnuts=7101
> DATA SAVED SUCCESSFULLY TO: 'Jesenik_results.csv'
> EXITING Election-Scraper-2017
>```

Partial output:
>```
﻿> Code;Town;Registered;Envelopes;Valid;...
> 523917;Bělá pod Pradědem;1546;945;938;77;1;0;47;2;53;70;8;12;10;0;1;79;1;33;331;0;3;42;0;7;0;1;158;2
> 524891;Bernartice;703;344;343;24;0;0;25;1;6;38;1;1;1;0;0;15;0;5;149;2;1;13;1;0;1;1;58;0
> ...
>```






