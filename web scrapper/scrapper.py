import json
import requests
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:104.0) Gecko/20100101 Firefox/104.0"}

def html_to_json(content, indent=None):    
    rows = table.findAll("tr", {"class" : "tdcolumn"}) 
    
    headers = {}
    thead = soup.find("th")
    if thead:
        thead = soup.find_all("th")
        for i in range(len(thead)):
            headers[i] = thead[i].text.strip().lower()
    print(headers)
    data = []
    for row in rows:
        cells = row.find_all("td")
        if thead:
            items = {}
            if len(cells) > 0:
                for index in headers:
                    items[headers[index]] = cells[index].text
        else:
            items = []
            for index in cells:
                items.append(index.text.strip())
        if items:
            data.append(items)
    return json.dumps(data, indent=indent)

def _get_content_url(url):
    #url = "https://www.bseindia.com/markets/equity/EQReports/bulk_deals.aspx"
    html = requests.get(url, headers=headers)
    soup = BeautifulSoup(html.text)
    return soup

def _find_table(soup)
    table = soup.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="ContentPlaceHolder1_gvbulk_deals") 
    return table

    # tbl_json = html_to_json(table, 4)
    # print (tbl_json)