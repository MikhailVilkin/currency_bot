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
    return pretty_print_dict(r)

def pretty_print_dict(d: dict) -> str:
    result = ""
    for key, value in d.items():
        result = result + "<b>" + key + "</b> (" + value["full_name"] + "): $" + value["in_usd"] + "\n"
    return result

# # regexp = re.compile(r"<a onclick=\"update_hash\(&#\d+;.+&#\d+;\);\" href=\"javascript:void\(0\);\">(.*)</a>")
# link = "https://bitinfocharts.com/cryptocurrency-prices/#CNY"

# data = requests.get(link)

# soup = BeautifulSoup(data.content, 'html.parser')
# res = soup.find_all('tr')
# # res[1].find('td')
# # for el in res[1:]:
# #     print(el.text)

# # # regexp = r"(\w+)\s+(\w+)\s+\$\s+([\d,\.]+)\s+(.+)\s+in"
# # # pattern = re.compile(regexp)
# # r = {}
# for el in res[1:10]:
#     # p = el.text.split(' ')
#     print(el.text)

# # print(r)
