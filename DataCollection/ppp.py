from bs4 import BeautifulSoup
import os

DRIVERPATH = "C:\\Users\\pvshe\\Desktop\\msedgedriver.exe"

def main():

    folder = 'C:\\Users\\pvshe\\Desktop\\CapitalSense\\PPP_HTML'
    for name in os.listdir(folder):
        print(f'Processing {name}...')
        f = open(os.path.join(folder, name), 'r')
        soup = BeautifulSoup(f.read(), 'html.parser')
        f.close()
        temps = soup.findAll('template')
        for t in temps:
            if t.has_attr('v-if') and t['v-if'] == 'firstload':
                rows = t.findChildren('tr')
                for row in rows:
                    data = {'name': '',
                            'amount': '',
                            'workers': '',
                            'industry': ''}
                    elements = row.findChildren('td')
                    for element in elements:
                        if 'Name' in element['data-title']:
                            a = element.findChildren('a')[0].contents[0]
                            data['name'] = a
                        if 'PPP Loan' in element['data-title']:
                            data['amount'] = element.contents[0].strip()
                        if 'Industry' in element['data-title']:
                            a = element.findChildren('a')[0].contents[0]
                            data['industry'] = a
                        if 'Jobs' in element['data-title']:
                            data['workers'] = element.contents[0].strip()
                    print(data)
        # rows = soup.findAll('tr')
        # for row in rows:
        #     children = row.findChildren('td')
        #     badrow = False
        #     for c in children:
        #         c_str = str(c)
        #         if 'line-number' in c_str or 'line-content' in c_str:
        #             badrow = True
        #             break
        #     if badrow:
        #         continue
        #     print(children)
        break

main()