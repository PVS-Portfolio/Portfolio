# Module to handle scraping internet search results

from bs4 import BeautifulSoup
import random
import requests
from googlesearch import search
from DataCollection.database import sanitize_name
import eventlet
from DataCollection.links import read_links, write_links

def get_header():
    UASTRINGS = ['Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
                 'Mozilla/5.0 (X11; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',
                 'Mozilla/5.0 (X11; Linux x86_64; rv:10.0) Gecko/20100101 Firefox/10.0',
                 'Mozilla/5.0 (Android; Mobile; rv:40.0) Gecko/40.0 Firefox/40.0',
                 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0',
                 'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Mobile Safari/537.36',
                 'Mozilla/5.0 (Linux; Android 7.0) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Focus/1.0 Chrome/59.0.3029.83 Safari/537.36',
                 'Mozilla/5.0 (Android 7.0; Mobile; rv:62.0) Gecko/62.0 Firefox/62.0']
    return random.choice(UASTRINGS)

def get_google_links(term, num_results=20):

    response = search(term, num_results=num_results)
    return response

def get_links_with_selenium(term, num_results = 20):
    pass

def get_company_names():
    filename = 'Data\\output.csv'
    data = []
    f = open(filename, 'r')
    f.readline()
    for line in f:
        splitline = line[:-1].split(',')
        name = splitline[0]
        name = name.replace('.', '')
        name = name.replace(',', '')
        name = name.replace('\'', '')
        data.append(name)
    f.close()
    return data

def search_bizapedia(url):
    s = requests.session()
    response = s.get(url, headers=get_header())
    soup = BeautifulSoup(response.text, 'html.parser')
    rows = soup.findAll('tr')

def main():
    # Get company names from database
    print('Retrieving company names...')
    names = [sanitize_name(n) for n in get_company_names()]
    s = '''action group inc
action home improvements llc
action landscape inc
action logoz
action overhead door inc
action petroleum co llc
action real estate llc
action remanufactured engines and accessories llc
action rental company and hardware llc
action scs llc
action tree pros inc
activate ad llc
activate america llc
activate birmingham llc
activate buckhead llc
activate gatlinburg llc
activate katy llc
activate lexington llc
activate oakbrook llc
activate oakley llc
activate overland park llc
active auto sales llc
active body chiropractic and injury center of richmond pllc
active heroes inc
active imaginations child development center llc
active impact llc
active sports agency llc
active therapy systems llc
active trucking llc
actons lawn service inc
actons limited liability company
actons llc
actors guild of lexington inc
actors theatre of louisville inc
acts 2 and 38 lawn care llc
acts of kindness llc a ky limited liability company dba miners bucket
acu archery usa llc
acuff acres llc
acuity packaging and logistics solutions llc
acuity title
acumantra solutions inc
acumen real properties llc
acura at oxmoor
acute care llc
acutia inc
acw partners llc
ad color inc
ad cucina llc
ad home improvements inc
ad plus inc
ad porter and sons inc
ad porter and sons inc
ad porter and sons south-east llc
ad-ios digital media co llc
ad-venture promotions llc
ada llc
adair automotive supply
adair county animal hospital and laser center psc
adair county conservation district
adair county hospital district
adair county of
adair county school district
adair drug llc
adair family (owenton ltd)
adair family medical center
adair pharmacy inc
adair place ii llc
adair place llc
adair progress inc
adair progress inc and donna r hancock
adairmark llc
adairville arms sp llc
adairville bp inc
adalberto rosario rivera trademark/tradename
adalyn-ridge trucking llc
adam and sons lawncare llc
adam bell farms llc
adam blondell dba blondell transport
adam d stowe dmd psc
adam davis towing and recovery llc
adam draizin
adam freight llc
adam gross inc
adam hendricks llc
adam hjermenrud
adam keys homes
adam legate and associates
adam matthews baking co llc
adam matthews inc
adam ray pe
adam s perkins llc
adam s ray pe
adam teater
adam thompson dmd pllc
adam w mosley sole proprietor
adam wright concrete and construction
adam wright concrete and construction llc
adam wright concreteand construction llc
adama jean cora - cestui que trust
adamleigh farm llc
adams affordable homes inc
adams and morton enterprises inc
adams and morton enterprises inc d/b/a gba commerical printing
adams and morton enterprises inc d/b/a gba office solutions
adams and sin lawncare and mobile washing
adams appliance installation llc
adams auto sales
adams auto sales llc
adams buick gmc inc
adams building and contracting llc
adams cabinetry inc
adams carpet cleaning 2 llc
adams constracting llc
adams construction and hauling limited liability company
adams contracting llc
adams corine organization/trade name/trade mark - debtor
adams corine organization/trade name/trade mark-debtor
adams dino laurie organization/trade name/trade mark - debtor
adams dino laurie organization/trade name/trade mark-debtor
adams engineering pllc
adams express tax
adams express tax inc
adams family distributing company inc
adams family farms  llc
adams family farms llc
adams farms
adams general contracting llc
adams group llc
adams heating and air conditioning inc
adams hill town houses council of co-owners inc
adams hill town houses counsil of co-owners inc
adams law pllc
adams legal group pllc
adams lpl financial advisors llc
adams marine services llc
adams nash and haskell inc
adams pharmacy
adams place llc
adams plumbing and mechanical inc
adams plumbing llc
adams pontiac buick gmc inc
adams realty
adams realty :organization/tradename/trademark-debtor
adams refrigeration heating and air conditioning llc
adams restoration and construction llc
adams services llc
adams stepner woltermann and dusing pllc
adams tammy suzanne  cestui que trust
adams tax
adams tax inc
adams tool company llc
adams trucking
adams-robinson enterprises inc
adams/clark electrical contractors llc
adamson holding company inc
adamson james edwin  cestui que trust
adamson law pllc
adamson propertiesllc
adamson services llc
adans hill town houses council of co-owners inc
adapt for life
adaptec solutions llc
adaptive community support services inc
adaptive enterprises llc
adaptive network services llc d/b/a ice guys llc
adaptive nursin and healthcare services inc'''
    names = s.split('\n')

    print(f'\tFound {len(names)} names.')

    mylinks = {}
    linkdata = read_links()
    for line in linkdata:
        name = sanitize_name(line)
        name = name.lower()
        mylinks[name] = linkdata[line]
    print('*************************************')

    # for name in mylinks:
    #     print(name)
    # print('...............................')

    limit = len(names)
    # limit = 100
    # eventlet.monkey_patch()
    for name in names[:limit]:
        if name in mylinks:
            print(f'{name} already has links!')
            continue
        print(f'Fetching Google results for: {name}')
        links = []
        try:
            links = list(get_google_links(name))
            mylinks[name] = links
        except Exception as e:
            if '429 Client Error' in str(e):
                print('Cooldown still active.')
                break
        write_links([name] + links)


if __name__ == "__main__":

    main()

    # # Read in retrieved links from links.csv
    # linkdata = read_links()
    #
    # # For each company, categorize links
    # for entry in linkdata:
    #     name = entry[0]
    #     links = entry[1:]
    #     s = requests.session()
    #     for link in links:
    #         if '.pdf' in link:
    #             continue
    #         response = s.get(link)
    #         print(name, link)
    #         soup = BeautifulSoup(response.text, 'html.parser')
    #         pagelinks = soup.findAll('a')
    #         for i in pagelinks:
    #             if 'contact' in i.text.lower():
    #                 print(i)
    #     s.close()
