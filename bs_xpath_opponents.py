from bs4 import BeautifulSoup
from parsel import Selector

def get_opponents(html):
    selector = Selector(text = html )
    matches= selector.xpath('table[class = "wikitable"]')[0]

    
    trs = matches.xpath("tr")
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