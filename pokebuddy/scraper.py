from bs4 import BeautifulSoup
import requests

response = requests.get("https://pokemondb.net/pokedex/ivysaur")
soup = BeautifulSoup(response.text, "html.parser")

fp = open("out.csv")

pe = soup.find("h2", string="Pokédex entries")
entries_div = pe.find_next_sibling("div", class_="resp-scroll")
table = list(entries_div.children)[0]
tbody = list(table.children)[0]
types = []
para = []
# print(type(tbody))
for row in tbody.children:
    # print(row, end="\n")
    # exit()
    myrow= list(row.children)
    # print(len(myrow))
    th, td = myrow[1], myrow[3]
    para.append(td.contents)
    print("th", th,"td", td, "ok")
print(para)