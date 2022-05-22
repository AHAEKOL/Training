import requests
import bs4
import sys

# global variable for catching parties names
all_parties_names = set()


def download_whole_html(link):
    """
    Downloads the page
    :param link: link_to_okrsek_page to the html page
    :return: html code as string or exception if error
    """
    print("Downloading " + link, end="")
    response = requests.get(link)
    if response.status_code != 200:
        raise Exception(f"Downloading of the html of the page has failed (status_code={response.status_code})!")
    print("     OK")
    return response.text


def get_county_data_from_page(link_to_county_page):
    """
    Downloads PSCs, names and links to more info of okrseks in of a county
    :param link_to_county_page: link_to_okrsek_page to county page
    :return: list of touples (PSC, name, link_to_okrsek_page to okrsek page)
    """
    html = download_whole_html(link_to_county_page)
    soup = bs4.BeautifulSoup(html, "html.parser")
    tables = soup.find_all('table')

    county_data = []
    for t in tables:
        rows = t.find_all("tr")
        for i in range(2, len(rows)):
            psc_a = rows[i].find_all("td")[0].find_all("a")
            # some table rows might be empty!
            if len(psc_a) != 0:
                psc = psc_a[0].text
                name = rows[i].find_all("td")[1].text
                okrsek_link = rows[i].find_all("td")[2].find_all("a")[0].attrs['href']
                okrsek_link = 'https://volby.cz/pls/ps2017nss/' + okrsek_link
                county_data.append((psc, name, okrsek_link))
    return county_data


def is_okrskova_page(soup):
    """
    Tells if the page contains more okrseks or if it is final page
    :param soup: soup object of the page
    :return: True if page contains okrseks
    """
    header = soup.find_all("table")[0].find_all("th")[0].text
    return header == "Okrsek"


def get_okrsek_links(soup):
    """
    Return a list of links to okrseks
    :param soup: Soup to page with okrseks
    :return: List of okrseks links
    """
    okrseks_links = []
    rows = soup.find_all('table')[0].find_all("tr")
    for i in range(1, len(rows)):
        cell = rows[i].find_all("td")
        for c in cell:
            a = c.find_all("a")
            # some table cells are empty - skip those
            if len(a) != 0:
                okrseks_links.append(a[0].attrs['href'])
    return okrseks_links


def remove_non_breaking_spaces(input_string):
    """
    Removes all non-breaking spaces from the string
    :param input_string: input string
    :return: input string without non-breaking spaces
    """
    non_break_space = u'\xa0'
    return input_string.replace(non_break_space, "")


def get_election_data_of_okrsek_page(link_to_okrsek_page):
    """
    Get election data of the okrsek page
    :param link_to_okrsek_page: sub link to the okrsek page
    :return: voters count, envelopes count, valid votes count, parties results
    """
    link_to_okrsek_page = 'https://volby.cz/pls/ps2017nss/' + link_to_okrsek_page
    html = download_whole_html(link_to_okrsek_page)
    soup = bs4.BeautifulSoup(html, "html.parser")
    tables = soup.find_all('table')

    voters_count = int(remove_non_breaking_spaces(tables[0].find_all('tr')[1].find_all('td')[0].text))
    envelopes_count = int(remove_non_breaking_spaces(tables[0].find_all('tr')[1].find_all('td')[1].text))
    valid_votes_count = int(remove_non_breaking_spaces(tables[0].find_all('tr')[1].find_all('td')[4].text))

    parties_results = {}
    for i in range(1, len(tables)):
        table = tables[i]
        rows = table.find_all("tr")
        for i2 in range(2, len(rows)):
            party_name = rows[i2].find_all("td")[1].text
            if party_name != "-":
                party_valid_votes = int(remove_non_breaking_spaces(rows[i2].find_all("td")[2].text))
                parties_results[party_name] = party_valid_votes
                all_parties_names.add(party_name)

    return voters_count, envelopes_count, valid_votes_count, parties_results


def get_election_data_of_final_page(soup):
    """
    Get election data of the final page that doesn't contain okrseks
    :param soup: soup of the final page
    :return: touple of voters_count, envelopes_count, valid_votes_count and
    parties_results (dict: key=party_name,value=valid_votes_count)
    """
    tables = soup.find_all('table')
    voters_count = int(remove_non_breaking_spaces(tables[0].find_all('tr')[2].find_all('td')[3].text))
    envelopes_count = int(remove_non_breaking_spaces(tables[0].find_all('tr')[2].find_all('td')[4].text))
    valid_votes_count = int(remove_non_breaking_spaces(tables[0].find_all('tr')[2].find_all('td')[7].text))

    parties_results = {}
    for i in range(1, len(tables)):
        table = tables[i]
        rows = table.find_all("tr")
        for i2 in range(2, len(rows)):
            party_name = rows[i2].find_all("td")[1].text
            if party_name != "-":
                party_valid_votes = int(remove_non_breaking_spaces(rows[i2].find_all("td")[2].text))
                parties_results[party_name] = party_valid_votes
                all_parties_names.add(party_name)

    return voters_count, envelopes_count, valid_votes_count, parties_results


def add_parties_results(parties_results, okrsek_parties_results):
    """
    Sum parties results. The result is stored in the first dictionary
    :param parties_results: first dictionary
    :param okrsek_parties_results: second dictionary
    :return: the second dictionary is added to the first
    """
    for party in parties_results.keys():
        parties_results[party] += okrsek_parties_results[party]


def get_election_data(link_to_county_page):
    """
    Download and scrap election data of the county
    :param link_to_county_page: link of the county web page
    :return: touple of voters_count, envelopes_count, valid_votes_count, parties_results
    """
    html = download_whole_html(link_to_county_page)
    soup = bs4.BeautifulSoup(html, "html.parser")
    voters_count = 0
    envelopes_count = 0
    valid_votes_count = 0
    parties_results = None

    if is_okrskova_page(soup):
        # if okrskova page then aggregate results of each okrsek
        okrsek_links = get_okrsek_links(soup)

        for okrsek_link in okrsek_links:
            okrsek_voters, okrsek_envelopes, okrsek_valid_votes, okrsek_parties_results = \
                get_election_data_of_okrsek_page(okrsek_link)
            voters_count += okrsek_voters
            envelopes_count += okrsek_envelopes
            valid_votes_count += okrsek_valid_votes
            if parties_results is None:
                parties_results = okrsek_parties_results
            else:
                add_parties_results(parties_results, okrsek_parties_results)

        return str(voters_count), str(envelopes_count), str(valid_votes_count), parties_results
    else:
        voters_count, envelopes_count, valid_votes_count, parties_results = get_election_data_of_final_page(soup)
        return str(voters_count), str(envelopes_count), str(valid_votes_count), parties_results


def scrap_election_results_to_file(county_link, output_file_path):
    """
    Scrap election results into a CSV file
    :param county_link: linke to the selected county webpage
    :param output_file_path: path to the output csv file
    """
    global all_parties_names

    city_data = get_county_data_from_page(county_link)

    csv_data = []
    index = 0
    # download the election data for each city in the county
    for cd in city_data:
        link_to_city = cd[2]
        psc = city_data[index][0]
        city_name = city_data[index][1]
        voter_count, envelop_count, valid_votes_count, parties_results = get_election_data(link_to_city)
        values = [psc, city_name, voter_count, envelop_count, valid_votes_count, parties_results]
        csv_data.append(values)
        index += 1

    # turn this set of all parties names into a sorted list
    all_parties_names = sorted(list(all_parties_names))

    # replace parties_results dictionary with values, missing parties have 0 votes
    for i in range(len(csv_data)):
        parties_results = csv_data[i].pop(5)
        for party in all_parties_names:
            if party in parties_results:
                csv_data[i].append(str(parties_results[party]))
            else:
                csv_data[i].append("0")

    with open(output_file_path, "w") as csv_file:
        # Write CSV header to the csv file
        csv_file.write("psc;nazev;pocet volicu;vydane obalky;platne hlasy;" + ";".join(all_parties_names) + "\n")

        # Writing election data to the csv file
        for csv_line_data in csv_data:
            csv_file.write(";".join(csv_line_data) + "\n")


def main():
    """
    Main function of the scrapper program. Parses input arguments and call the scrapper function.
    """
    if len(sys.argv) != 3:
        print("Wrong number of arguments (expected 2)!")
        exit(-1)

    county_link = sys.argv[1]
    output_file_path = sys.argv[2]

    print("Link to the county webpage is: " + county_link)
    print("CSV output file path is: " + output_file_path)

    scrap_election_results_to_file(county_link, output_file_path)

    print("Done!")


if __name__ == "__main__":
    main()
