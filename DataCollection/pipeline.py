from DataCollection.database import Database, Record
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from DataCollection.facebook import get_facebook_results

DRIVERPATH = "C:\\Users\\pvshe\\Desktop\\msedgedriver.exe"

def init_driver():
    service = Service(executable_path=DRIVERPATH)
    driver = webdriver.Edge(service=service)
    return service, driver

def main():

    print('Welcome to Data Harvester 0.?')
    print('We will now harvest data.\n')

    print('Creating database....')
    DB = Database()
    print('\tBlank database created.')

    # Read in database file
    filename = 'C:\\Users\\pvshe\\Desktop\\database_writetest.csv'
    print(f'Reading data from {filename}...')
    DB.read(filename)
    print(f'\tGot {len(DB.records)} entries.')

    # Only use this when you are putting new names into the DB from UCC filings output
    # print('Adding entries from file...')
    # DB.add_entries_from('C:\\Users\\pvshe\\PycharmProjects\\DataHarvester\\DataCollection\\Data\\kyucc_search=a.csv')
    # print(f'Database has {len(DB.records)} records.')

    print('Checking records for links...')
    links, names = DB.check_for_links()
    DB.check_no_links()
    print(f'\tFound {len(names)} entries with links but no contact info.')

    # Gather any new links possible

    if names:
        print('Initiating contact info search.')

        blacklistfile = open('C:\\Users\\pvshe\\Desktop\\blacklist.csv', 'r')
        blacklist = [line[:-1] for line in blacklistfile]
        blacklistfile.close()

        print('\tInitializing web Driver and Service.')
        server, driver = init_driver()
        for name in names:
            print('Processing: ', name)
            if name in blacklist:
                print('Name on blacklist: ', name)
                continue
            DB.fetch_contact_info(name, set(links[name]), driver, blacklist=blacklist)
        driver.quit()

    print('Writing database.')
    DB.write('C:\\Users\\pvshe\\Desktop\\newresults3.csv')
    print('\tDatabase written successfully.')

main()