import requests
import bs4
import sys

def download_whole_html(link):
    print("Downloading " + link, end="")
    response = requests.get(link)
    if response.status_code != 200:
        raise Exception(f"Downloading of the html of the page has failed (status_code={response.status_code})!")
    print("     OK")
    return response.text

def get_county_data_from_page(link):
    html = download_whole_html(link)
    soup = bs4.BeautifulSoup(html, "html.parser")
    tables = soup.find_all('table')

    data = []
    for t in tables:
        rows = t.find_all("tr")
        for i in range(2, len(rows)):
            psc_a = rows[i].find_all("td")[0].find_all("a")
            if len(psc_a) != 0:
                psc = psc_a[0].text
                name = rows[i].find_all("td")[1].text
                link2 = rows[i].find_all("td")[2].find_all("a")[0].attrs['href']
                link2 = 'https://volby.cz/pls/ps2017nss/' + link2
                data.append((psc, name, link2))
    return data

def is_okrskova_page(soup):
    header = soup.find_all("table")[0].find_all("th")[0].text
    return header == "Okrsek"

def get_okrsek_links(soup):
    links = []
    rows = soup.find_all('table')[0].find_all("tr")
    for i in range(1, len(rows)):
        cell = rows[i].find_all("td")
        for c in cell:
            a = c.find_all("a")
            if len(a) != 0:
                links.append(a[0].attrs['href'])
    return links


def get_election_data_internal(link, get_parties):
    parties = []
    link = 'https://volby.cz/pls/ps2017nss/' + link
    html = download_whole_html(link)
    soup = bs4.BeautifulSoup(html, "html.parser")
    tables = soup.find_all('table')
    nonBreakSpace = u'\xa0'
    voters = tables[0].find_all('tr')[1].find_all('td')[0].text.replace(nonBreakSpace, "")
    envelopes = tables[0].find_all('tr')[1].find_all('td')[1].text.replace(nonBreakSpace, "")
    valid_votes = tables[0].find_all('tr')[1].find_all('td')[4].text.replace(nonBreakSpace, "")

    if get_parties:
        for i in range(1, len(tables)):
            table = tables[i]
            rows = table.find_all("tr")
            for i2 in range(2, len(rows)):
                parties.append(rows[i2].find_all("td")[1].text)

    return voters, envelopes, valid_votes, parties


def get_election_data_internal2(soup):
    parties = []
    tables = soup.find_all('table')
    nonBreakSpace = u'\xa0'
    voters = tables[0].find_all('tr')[2].find_all('td')[3].text.replace(nonBreakSpace, "")
    envelopes = tables[0].find_all('tr')[2].find_all('td')[4].text.replace(nonBreakSpace, "")
    valid_votes = tables[0].find_all('tr')[2].find_all('td')[6].text.replace(nonBreakSpace, "")

    for i in range(1, len(tables)):
        table = tables[i]
        rows = table.find_all("tr")
        for i2 in range(2, len(rows)):
            parties.append(rows[i2].find_all("td")[1].text)

    return voters, envelopes, valid_votes, parties



def get_election_data(link):
    html = download_whole_html(link)
    soup = bs4.BeautifulSoup(html, "html.parser")
    voters = 0
    envelopes = 0
    valid_votes = 0
    parties = None
    if is_okrskova_page(soup):
        links = get_okrsek_links(soup)
        is_first = True
        for l in links:
            v, e, vv, p = get_election_data_internal(l, is_first)
            if is_first:
                parties = p
                is_first = False
            voters += int(v)
            envelopes += int(e)
            valid_votes += int(vv)
        return str(voters), str(envelopes), str(valid_votes), parties
    else:
        return get_election_data_internal2(soup)


if len(sys.argv) != 3:
    print("Wrong number of arguments (expected 2)!")
    exit()

link = sys.argv[1]
output_file = sys.argv[2]

print("Link to the webpage is: " + link)
print("CSV output file name is: " + output_file)

city_data = get_county_data_from_page(link)

csv_data = []
index = 0
for cd in city_data:
    link_to_city = cd[2]
    election_data = get_election_data(link_to_city)
    csv_data.append((city_data[index][0], city_data[index][1], election_data[0], election_data[1], election_data[2], election_data[3]))
    index += 1

with open(output_file, "w") as file:
    # Writing data to a file
    file.write("psc,nazev,pocet volicu,vydane obalky,platne hlasy,strany\n")
    for d in csv_data:
        line = ""
        for i in range(5):
            line += d[i] + ","
        for x in d[5]:
            line += x + ",."
        file.write(line + "\n")

