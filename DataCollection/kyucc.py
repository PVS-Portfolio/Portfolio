# Data harvesting functions for KY.

'''
Data to harvest:
    UCC
    Paycheck Protection
    BBB
'''
import googlesearch
from bs4 import BeautifulSoup
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import facepy
# from facebook_scraper import get_profile
import urllib.request
import requests
from googlesearch import search
import os
import re

SEARCH_TERM = 'b'
KY_URL = '(S(zdsihz4bpqxs3baa4vkh5n3w))'

def match_phone_number(input_string):
    input_string = input_string.replace(' ', '')
    pattern = r'\(\d{3}\)\d{3}-\d{4}?'

    # This one also seems to work, and may be more flexible.
    # pattern = r'(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})'

    result = re.findall(pattern, input_string)
    return result


def match_email_address(input_string):
    input_string = input_string.replace(' ', '')
    regex = re.compile(
        r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")
    if re.fullmatch(regex, input_string):
        return input_string

def get_ky_ucc_filings_text():
    # Note: KY website URL updates dynamically.  Need to grab a fresh URL when running this function.
    url = f'https://web.sos.ky.gov/ftucc/{KY_URL}/search.aspx'

    # The boilerplate here remains hard-coded.  Only need to change the search term.
    data = {"ctl00$ContentPlaceHolder1$SearchForm1$tOrgname": SEARCH_TERM,
            "ctl00$ContentPlaceHolder1$SearchForm1$bSearch": 'Search',
            "__VIEWSTATE": "/wEPDwUJMzQ1MjYzMTk4D2QWAmYPZBYCAgkPZBYCAgEPZBYEAgsPDxYCHgdWaXNpYmxlaGRkAg0PDxYCHwBoZGRk7+hUvc+Nf6LnERebHeOfhLsHmM0V6wPZ4kvvWfmPR1Q=",
            "__VIEWSTATEGENERATOR": "90EF923B",
            "__EVENTVALIDATION": "/wEdAAttTUHueSDf0taGo+AaqBOqLMwDBQbKz92Q549SXLXbuD6jwHdsd0xXMZV00FTIVczkNMK+90Ic77EqUA9zsCFm2ieFdJTbE4kzWBKcjtdLG6CMFUghtyCH9lsHjL1EFhzdxn/JBfahsDfW+UpblqA3FkkLbwPePhE13/FRLcmQBRcWugM+JRBsmB0ElzvmIrZoMag/3HBeJB9AhAIKR9lohacLQsSR/wCMATepgD6QmmFl4Z08FauHcJ/v+DTsqNHxrSwIorsfckMLkUNTx7x3"}

    response = None
    with requests.session() as s:
        s.get(url)
        response = s.post(url, data=data)
    return response.text


def get_ky_ucc_filings_entries():
    print('Getting raw search results from KY UCC database...')
    text = get_ky_ucc_filings_text()
    print('\tRetrieved.\nParsing results...')
    soup = BeautifulSoup(text, 'html.parser')

    result = []
    # This grabs all of the table rows from the search results.
    rows = soup.findAll('tr', {'class': 'Activebg'})

    for r in rows:
        row = []
        children = r.findChildren('td')
        for child in children:
            text = child.text.replace(',', '')
            row.append(text)
        children = r.findChildren('a')
        links = set()
        for child in children:
            href = child['href']
            links.add(href[href.find('?'):])
        for link in links:
            row.append(link)
        result.append(row)

    print('\tResults parsed.')

    return result


def get_ky_ucc_filing_data(number):
    url = f'https://web.sos.ky.gov/ftucc/{KY_URL}/search.aspx'

    pieces = number.split('-')
    assert len(pieces) == 3

    # The boilerplate here remains hard-coded.  Only need to change the search term.
    data = {"ctl00$ContentPlaceHolder1$SearchForm1$tYear": pieces[0],
            "ctl00$ContentPlaceHolder1$SearchForm1$tSeq": pieces[1],
            "ctl00$ContentPlaceHolder1$SearchForm1$tCkd": pieces[2],
            "ctl00$ContentPlaceHolder1$SearchForm1$bSearch": 'Search',
            "__VIEWSTATE": "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",
            "__VIEWSTATEGENERATOR": "90EF923B",
            "__EVENTVALIDATION": "/wEdAAvMAIDxKsg8MIc1lUXjx43WLMwDBQbKz92Q549SXLXbuD6jwHdsd0xXMZV00FTIVczkNMK+90Ic77EqUA9zsCFm2ieFdJTbE4kzWBKcjtdLG6CMFUghtyCH9lsHjL1EFhzdxn/JBfahsDfW+UpblqA3FkkLbwPePhE13/FRLcmQBRcWugM+JRBsmB0ElzvmIrZoMag/3HBeJB9AhAIKR9lohacLQsSR/wCMATepgD6QmlLI+F2aHpF9xgBLk5f1cmLknnTah6Gx6E9BZae/9XAm"}

    response = None
    with requests.session() as s:
        response = s.get(url)
    return response.text


def write_ky_ucc_data(filename, data):
    # cwd = os.getcwd()
    # datadir = os.path.join(cwd, 'Data')
    # if not os.path.exists(datadir):
    #     os.mkdir(datadir)
    # filename = os.path.join(datadir, filename)
    print(f'Writing to: {filename}')
    count = 0
    with open(filename, 'w') as f:
        f.write('Name,Filing Number,File Date,Lapse Date,Secured Party\n')
        for row in data:
            line = ''
            for item in row:
                line += item + ','
            f.write(line[:-1] + '\n')
            count += 1

    return count


def search_company_contact_info(filename, num):
    outfile = open('Data\\output.csv', 'w')
    f = open(filename, 'r')
    line = f.readline()
    outfile.write(line)
    count = 0
    for line in f:
        count += 1
        if count < 375:
            continue
        print(f'Processing {count} / {num}')
        line = line[:-1]
        splitline = line.split(',')
        name = splitline[0]
        name = name.replace(' ', '+')
        try:
            numbers = get_google_results(name)
        except:
            print(f'Error searching {name}')
            numbers = []
        if numbers:
            line += ','
            for number in numbers:
                line += number + ','
            line = line[:-1]
        line += '\n'
        outfile.write(line)
    f.close()


def get_google_results(keyword):
    r = None
    with requests.session() as s:
        r = s.get(f'https://www.google.com/search?q={keyword}')
    f = open('C:\\Users\\pvshe\\Desktop\\test.html', 'w')
    f.write(r.text)
    f.close()
    # print(r.text)
    return set(match_phone_number(r.text))
    # for res in result:
    #     print(res)
    # soup = BeautifulSoup(r.text, 'html.parser')
    # result = soup.find_all('span')

def aggregate_files(term):
    files = os.listdir('C:\\Users\\pvshe\\Desktop\\data_aggregation\\tempinput')
    outfile = open(f'C:\\Users\\pvshe\\Desktop\\data_aggregation\\kyucc_search={term}.csv', 'w')
    outfile.write('Name,Filing Number,File Date,Lapse Date,Secured Party,Page link\n')
    for f in files:
        name = os.path.join('C:\\Users\\pvshe\\Desktop\\data_aggregation\\tempinput', f)
        infile = open(name, 'r')
        data = infile.readlines()
        infile.close()
        os.remove(name)
        for line in data[1:]:
            outfile.write(line)
    outfile.close()
    print(f'Wrote output to kyucc_search={term}.csv.')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for letter1 in 'c':
        for letter2 in 'abcdefghijklmnopqrstuvwxyz':
            term = letter1 + letter2
            for letter3 in 'abcdefghijklmnopqrstuvwxyz':
                SEARCH_TERM = letter1 + letter2 + letter3
                result = get_ky_ucc_filings_entries()
                num = write_ky_ucc_data(f'C:\\Users\\pvshe\\Desktop\\data_aggregation\\tempinput\\kyucc_search={SEARCH_TERM}.csv', result)
            aggregate_files(term)
    # search_company_contact_info('Data\\testdata.csv', 12423)

    # facebook_test()