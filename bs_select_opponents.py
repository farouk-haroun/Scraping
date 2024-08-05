from bs4 import BeautifulSoup

def get_opponents(html):
    soup = BeautifulSoup(html, 'html.parser')
    tables = soup.select('table[class = "wikitable"]')

    matches = tables[0]
    trs = matches.select("tr")
    opponents = []
    links = [] 
    for tr in trs:
        opponent = {}
        opponent_node = tr.select_one("td:nth-child(3)")
        
        if not opponent_node:
            continue
        
        opponent_name = opponent_node.string
        opponent_link = None
        if not opponent_name:
            opponent_name = opponent_node.select_one("a").string
            opponent_link = f"https://en.wikipedia.org/{opponent_node.select_one("a").get('href')}"
            
            
        opponent['name'] =  opponent_name.strip('\n')
        opponent['link'] = opponent_link
        opponents.append(opponent)
    
    return opponents