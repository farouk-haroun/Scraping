from bs4 import BeautifulSoup
def get_opponents(html):
    soup = BeautifulSoup(html, 'html.parser')
# print(soup.title.string)
    tables  = soup.find_all("table", class_ = "wikitable")

    matches = tables[1]
    trs = matches.find_all("tr")
    opponents = []
    for tr in trs:
        tds = tr.find_all("td")
        if not tds:
            continue
        opponent_node = tds[2]
        opponent_name = opponent_node.string
        if not opponent_name:
            opponent_name = opponent_node.a.string
        
        opponents.append(opponent_name.strip('\n'))
    return opponents