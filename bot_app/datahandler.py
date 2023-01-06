import re
import requests
from bs4 import BeautifulSoup

LINK = "https://bitinfocharts.com/cryptocurrency-prices/"

def _get_crypto_currencies():
    data = requests.get(LINK)
    rows = BeautifulSoup(data.content, 'html.parser').find_all('tr')
    r = {}
    for el in rows[1:10]:
        p = el.text.split(' ')
        if (len(p) > 2):
            r[p[1]] = {
                'full_name': p[2] if p[3] == '' else p[2] + ' ' + p[3], 
                'in_usd': p[6] if p[5] == '$' else p[5],
            }
    return _pretty_print_dict(r)

def _pretty_print_dict(d: dict) -> str:
    result = ""
    for key, value in d.items():
        result = result + "<b>" + key + "</b> (" + value["full_name"] + "): $" + value["in_usd"] + "\n"
    return result


def _get_conversion(message) -> str:
    request = "https://www.google.com/search?q={}&hl=en".format(
        message.replace(" ", "+")
        )
    data = requests.get(request)
    page_soup = BeautifulSoup(data.text, "html.parser")
    result = page_soup.findAll("div",{"class":"BNeawe iBp4i AP7Wnd"})
    if result:
        result = result[0].text
    else:
        result = page_soup.findAll("div",{"class":"Gx5Zad xpd EtOod pkphOe"})
        result = result[0].get_text('\n').replace('\n,', ',')
        r = re.compile(r".*\n(\w+\.com).*")
        link = re.findall(r, result)
        result = re.sub(
            r'\n\w+\.com.+', 
            '\n\n<b>Taken from: ' + link[0] + ' through Google Search</b>', 
            result
            )
        result = result.replace('About Featured Snippets', '')
    return result

# request = ['convert', 'water', 'to', 'wine']
# google = "https://www.google.com/search?q={}&hl=en".format('+'.join(request))

# data = requests.get(google)

# page_soup = BeautifulSoup(data.text, "html.parser") 
 
# nasdaqValue = page_soup.findAll("div",{"class":"Gx5Zad xpd EtOod pkphOe"})

# result = nasdaqValue[0].get_text(';')
# r = re.compile(r".*;(\w+\.com).*")
# link = re.findall(r, result)
# result = re.sub(r';\w+\.com.+', ';result: ' + link[0], result)

# print(result)
