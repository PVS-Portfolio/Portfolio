from DataCollection.kyucc import match_phone_number, match_email_address
from time import sleep
from copy import deepcopy
from bs4 import BeautifulSoup

CHARS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789().-@'

def scrape(source):
    results = {'phone': '',
               'email': '',
               'website': ''}
    candidates = {}
    soup = BeautifulSoup(source, 'html.parser')
    spans = soup.findAll('span')
    for s in spans:
        t = s.text
        # print(t)
        ph = match_phone_number(t)
        if ph:
            results['phone'] = ph[0]
        em = match_email_address(t)
        if em:
            results['email'] = em
        else:
            if any([suffix in t for suffix in ['.com', '.net', '.org']]):
                if t in candidates:
                    candidates[t] += 1
                else:
                    candidates[t] = 1
    results['website'] = get_most_likely_website(candidates)
    return results

def get_facebook_results(url, driver):
    results = {'phone': '',
               'email': '',
               'website': ''}

    try:
        driver.get(url)
    except:
        return results
    sleep(3)

    results = scrape(driver.page_source)
    return results



# def get_facebook_results(url, driver):
#     print('Retrieving: ', url + 'about')
#     driver.get(url + 'about')
#     sleep(3)
#
#     curr_url = driver.current_url
#     if 'about.meta.com' in curr_url:
#         results = get_facebook_info_personalpage(url, driver)
#     else:
#         results = get_facebook_info_businesspage(driver)
#     return results

def get_most_likely_website(candidates):
    maxcount = 0
    maxkey = ''
    for key in candidates:
        if candidates[key] > maxcount:
            maxcount = candidates[key]
            maxkey = key
    return maxkey

def get_facebook_info_personalpage(url, driver):
    print('Redirecting to: ', url + '?sk=about')
    driver.get(url + '?sk=about')
    sleep(3)

    error_elements = driver.find_elements('class name', '_7nyf')
    problem = False
    for elem in error_elements:
        if 'may be broken' in elem.accessible_text:
            problem = True
            break
    if problem:
        driver.get(url)
        sleep(2)

    results = {'phone': '',
               'email': '',
               'website': ''}
    potential_websites = {}

    elements = driver.find_elements('class name', 'm')
    buttons = []
    for e in elements:
        if e.aria_role == 'button':
            buttons.append(e)
    for b in buttons:
        name = ''
        for char in b.accessible_name:
            if char in CHARS:
                name += char
        name = name.lower()
        phone = match_phone_number(name)
        email = match_email_address(name)
        if phone:
            results['phone'] = phone
        if email:
            results['email'] = email
        if '.com' in name and '@' not in name:
            if name in potential_websites:
                potential_websites[name] += 1
            else:
                potential_websites[name] = 1

    results['website'] = get_most_likely_website(potential_websites)
    return results

def get_facebook_info_businesspage(driver):
    results = {'phone': '',
               'email': '',
               'website': ''}
    potential_websites = {}

    source = driver.page_source
    soup = BeautifulSoup(source, 'html.parser')

    spans = soup.findAll('span')
    h3s = soup.findAll('h3')
    divs = soup.findAll('div')

    elements = [e.text for e in spans + h3s + divs]

    # a = driver.find_elements('tag name', 'span')
    # a = [i.text for i in a if i.text]
    # b = driver.find_elements('tag name', 'a')
    # b = [i.text for i in b if i.text]
    # c = driver.find_elements('tag name', 'div')
    # c = [i.text for i in c if i.text]
    # d = driver.find_elements('tag name', 'h3')
    # d = [i.text for i in d if i.text]
    # elements = a + b + c + d

    # a = driver.find_elements('class name', 'a')
    # a = [i.text for i in a if i.text]
    # b = driver.find_elements('class name', 'm')
    # b = [i.text for i in b if i.text]
    # elements = a + b

    # elements = [e for e in elements if e.text not in ['Log In', '']]
    for text in elements:
        if 'http://' in text:
            text = text.replace('http://', '')
        if 'https://' in text:
            text = text.replace('https://', '')
        if 'www.' in text:
            text = text.replace('www.', '')
        text = text.lower()
        phone = match_phone_number(text)
        email = match_email_address(text)
        if phone:
            results['phone'] = phone
        if email:
            results['email'] = email
        if '.com' in text and '@' not in text and '\n' not in text:
            if text in potential_websites:
                potential_websites[text] += 1
            else:
                potential_websites[text] = 1

    results['website'] = get_most_likely_website(potential_websites)
    return results


# def get_facebook_info(url, driver, possible_links = []):
#     print('Retrieving: ', url + 'about')
#     results = {'phone': '',
#                'email': '',
#                'website': ''}
#     phone, email, website = '', '', ''
#     potential_websites = {}
#
#     driver.get(url + 'about')
#     sleep(2)
#     curr_url = driver.current_url
#     if 'about.meta.com' in curr_url:
#         print('Redirecting to: ', url + '?sk=about')
#         driver.get(url + '?sk=about')
#         sleep(2)
#
#         elements = driver.find_elements('class name', 'm')
#         buttons = []
#         for e in elements:
#             if e.aria_role == 'button':
#                 buttons.append(e)
#         for b in buttons:
#             name = ''
#             for char in b.accessible_name:
#                 if char in CHARS:
#                     name += char
#             name = name.lower()
#             phone = match_phone_number(name)
#             email = match_email_address(name)
#             if phone:
#                 results['phone'] = phone
#                 print('Phone:', phone)
#             if email:
#                 results['email'] = email
#                 print('Email:', email)
#             if '.com' in name and '@' not in name:
#                 if name in potential_websites:
#                     potential_websites[name] += 1
#                 else:
#                     potential_websites[name] = 1
#
#     else:
#         elements = driver.find_elements('tag name', 'span')
#         elements.extend(driver.find_elements('tag name', 'a'))
#         elements.extend(driver.find_elements('tag name', 'div'))
#         for element in elements:
#             text = element.text
#             if 'Log in' in text:
#                 pass
#                 # print('***' + element.aria_role + '***')
#             if 'http://' in text:
#                 text = text.replace('http://', '')
#             if 'https://' in text:
#                 text = text.replace('https://', '')
#             if 'www.' in text:
#                 text = text.replace('www.', '')
#             text = text.lower()
#             phone = match_phone_number(text)
#             email = match_email_address(text)
#             if phone:
#                 results['phone'] = phone
#                 # print('Phone:', phone)
#             if email:
#                 results['email'] = email
#                 # print('Email:', email)
#             if '.com' in text and '@' not in text:
#                 if text in potential_websites:
#                     potential_websites[text] += 1
#                 else:
#                     potential_websites[text] = 1
#         # if text in possible_links:
#         #     website = text
#         #     print('Company website:', website)
#
#     maxcount = 0
#     maxkey = ''
#     for key in potential_websites:
#         if potential_websites[key] > maxcount:
#             maxcount = potential_websites[key]
#             maxkey = key
#     results['website'] = maxkey
#     return results['phone'], results['email'], results['website']