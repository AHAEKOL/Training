# Election Scrapper
Election Scrapper is library for extraction of election results from a na official website and its presentation in a form of csv file, which is then ready for further analysis.
The file contains postal code of the town of interest, its name and then aggregated numbers over the whole county i.e. its towns and villages.
The numbers contain overall no. of voters in the area, the used envelopes, the valid votes and a list of all parties. If there were more then one local vote area, that the numer represents sum of the numbers for each.


## Installation

Use the package manager [pip] and install all the libraries mentioned in the requirements file

## Usage
How to run the script in command line in Ubuntu OS:
1) create virtual environment: virtualenv venv_jan_fridrich_scrapper
2) nainstalujte potrebne moduly pip install -r requirements.txt
3) activate virtual environment: source venv_jan_fridrich_scrapper/bin/activate
4) start the skript based on required arguments( e.g: python3 main.py "https://volby.cz/pls/ps2017/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2101" output_benesov.csv)
5) output of the scrapping can you find in the upper defined csv file





