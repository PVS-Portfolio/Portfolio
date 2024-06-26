# Module to represent data entries
from DataCollection.links import read_links
from DataCollection.facebook import get_facebook_results
from bs4 import BeautifulSoup
from DataCollection.kyucc import match_phone_number, match_email_address
from time import sleep


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from DataCollection.facebook import get_facebook_results

DRIVERPATH = "C:\\Users\\pvshe\\Desktop\\msedgedriver.exe"

def init_driver():
    service = Service(executable_path=DRIVERPATH)
    driver = webdriver.Edge(service=service)
    return service, driver


class Database:

    def __init__(self):
        self.records = {}
        self.fields = ['website', 'phone', 'email',
                       'ucc_filing', 'ucc_start', 'ucc_lapse',
                       'secured_party', 'ucc_suffix']

    def insert(self, rec):
        if rec.fields['name'] in self.records:
            myrec = self.records[rec.fields['name']]
            for field in rec.fields:
                # If the field is the name or the links boolean, just move on
                if field in ['name', 'links']:
                    continue
                # Compare email, phone, or website to existing one
                elif field in ['email', 'phone', 'website']:
                    # If there is none already, just insert it
                    if not myrec.fields[field]:
                        self.records[rec.fields['name']].fields[field] = rec.fields[field]
                    elif myrec.fields[field] == rec.fields[field]:
                        continue
                    elif not rec.fields[field]:
                        continue
                    else:
                        self.records[rec.fields['name']].fields[field] += f'#{rec.fields[field]}'
                elif myrec.fields[field] != '':
                    self.records[rec.fields['name']].fields[field] += f'#{rec.fields[field]}'
                else:
                    self.records[rec.fields['name']].fields[field] = rec.fields[field]
        else:
            self.records[rec.fields['name']] = rec

    def read(self, filename):
        f = open(filename, 'r')
        f.readline()
        for line in f:
            tokens = line[:-1].split(',')
            name = tokens[0]
            email = tokens[1].replace('#', '')
            phone = tokens[2].replace('#', '')
            website = tokens[3].replace('#', '')
            secured = tokens[4]
            filingno = tokens[5]
            filingstart = tokens[6]
            filinglapse = tokens[7]
            filinglink = tokens[8]

            r = Record()
            r.fields['name'] = name
            r.fields['email'] = email
            r.fields['phone'] = phone
            r.fields['website'] = website
            r.fields['secured_party'] = secured
            r.fields['filing_number'] = filingno
            r.fields['filing_start'] = filingstart
            r.fields['filing_lapse'] = filinglapse
            r.fields['filing_link'] = filinglink

            self.insert(r)

        f.close()

    def write(self, filename):
        with open(filename, 'w') as outfile:

            outfile.write('name,email,phone,website,secured_party,ucc_filing_number,ucc_file_date,ucc_lapse_date,filing_link\n')
            keys = sorted(self.records.keys())
            for key in keys:
                mystring = ''
                mystring += key + ','
                mystring += self.records[key].fields['email'] + ','
                mystring += self.records[key].fields['phone'] + ','
                mystring += self.records[key].fields['website'] + ','
                mystring += self.records[key].fields['secured_party'] + ','
                mystring += self.records[key].fields['filing_number'] + ','
                mystring += self.records[key].fields['filing_start'] + ','
                mystring += self.records[key].fields['filing_lapse'] + ','
                mystring += self.records[key].fields['filing_link'] + '\n'
                outfile.write(mystring)

    def check_no_links(self):
        links = read_links()
        recs = [i for i in self.records.keys() if i not in links]
        print(f'\tFound {len(recs)} entries that have no links.')
        return recs

    def check_for_links(self):
        links = read_links()
        need_data = []
        done = 0
        for name in links:
            if name not in self.records:
                continue
            rec = self.records[name]
            ph = rec.fields['phone']
            em = rec.fields['email']
            wb = rec.fields['website']
            if ph or em or wb:
                done += 1
                continue
            else:
                need_data.append(name)
        print(f'\tFound {done} entries that have already been scraped.')
        return links, need_data

    def fetch_contact_info(self, name, links, driver, blacklist=[]):
        for link in links:
            if 'http://' in link:
                link = link.replace('http://', '')
            if 'https://' in link:
                link = link.replace('https://', '')
            if 'www.' in link:
                link = link.replace('www.', '')

            if 'facebook.com' in link:
                link = link[link.index('facebook'):]
                for tag in ['story', 'photo', 'video', 'event']:
                    if tag in link:
                        link = link[:link.index(tag)]
                if link[:2] == 'm.':
                    link = link[2:]
                link = 'https://www.' + link
                if link in blacklist:
                    print(f'{link} on blacklist.')
                    continue
                print(f'{link}', end='... ')
                results = get_facebook_results(link, driver)
                update = False
                if results['phone']:
                    update = True
                    if self.records[name].fields['phone']:
                        if self.records[name].fields['phone'] != results['phone']:
                            self.records[name].fields['phone'] += '#' + results['phone']
                    else:
                        self.records[name].fields['phone'] = results['phone']
                if results['email']:
                    update = True
                    if self.records[name].fields['email']:
                        if self.records[name].fields['email'] != results['email']:
                            self.records[name].fields['email'] += '#' + results['email']
                    else:
                        self.records[name].fields['email'] = results['email']
                if results['website']:
                    update = True
                    if self.records[name].fields['website']:
                        if self.records[name].fields['website'] != results['website']:
                            self.records[name].fields['website'] += '#' + results['website']
                    else:
                        self.records[name].fields['website'] = results['website']
                if update:
                    print('Updated contact information.')
                else:
                    print()

    def fb_tester(self):

        s, d = init_driver()
        links = ['https://www.facebook.com/p/AS-Electric-Supply-Inc-100069563383021/?sk=about',
                 'https://www.facebook.com/p/AR-Contractor-homes-100064644235342/?sk=about',
                 'https://www.facebook.com/p/A-R-Auto-Sales-and-Services-100057147322401/?sk=about',
                 'https://www.facebook.com/profile.php?id=106416339424256']
        for link in links:
            print('Visiting: ', link)
            d.get(link)
            sleep(3)
            text = d.page_source
            soup = BeautifulSoup(text, 'html.parser')
            elements = soup.findAll('span')
            for e in elements:
                ph = match_phone_number(e.text)
                if ph:
                    print('ph: ', e.text)
                em = match_email_address(e.text)
                if em:
                    print('em: ', e.text)


    def add_entries_from(self, filename):
        f = open(filename, 'r')
        data = f.readlines()
        f.close()

        for line in data[1:]:
            tokens = line[:-1].split(',')
            name = sanitize_name(tokens[0])

            filingno = tokens[1]
            filingstart = tokens[2]
            filinglapse = tokens[3]
            if len(tokens) == 6:
                secured = tokens[4]
                filinglink = tokens[5]
            elif len(tokens) == 5:
                secured = ''
                filinglink = tokens[4]

            r = Record()
            r.fields['name'] = name
            r.fields['filing_number'] = filingno
            r.fields['filing_start'] = filingstart
            r.fields['filing_lapse'] = filinglapse
            if len(tokens) == 6:
                r.fields['secured_party'] = secured
            else:
                r.fields['secured_party'] = ''
            r.fields['filing_link'] = filinglink

            self.insert(r)


    def print(self):
        for rec in self.records:
            print(f'Record: {rec}')
            print(self.records[rec])

class Record:

    def __init__(self):
        self.fields = {}

        # general fields
        self.fields['name'] = ''
        self.fields['website'] = ''
        self.fields['phone'] = ''
        self.fields['email'] = ''
        self.fields['links'] = 'F'

    def __str__(self):
        mystring = ''
        mystring += 'Name:' + self.fields['name'] + '\n'
        for f in self.fields:
            if f == 'name':
                continue
            else:
                try:
                    mystring += '\t' + f + ': ' + self.fields[f] + '\n'
                except:
                    mystring =  f'Error creating string from {mystring} {f} {self.fields[f]}'
        return mystring

    def get(self, field):
        return self.fields[field]

    def set(self, field, value):
        self.fields[field] = value

def sanitize_name(name):
    name = name.lower()
    name = name.replace('.', '')
    name = name.replace('\'', '')
    name = name.replace('&', 'and')
    return name

if __name__ == '__main__':
    # d = create_database('Data\\kyucc_search=a.csv')
    # d = Database()
    # d.read('C:\\Users\\pvshe\\Desktop\\database.csv')
    # d.write()
    pass