from bs4 import BeautifulSoup
import requests

url = "https://pokemondb.net/pokedex/"

fp = open("out.csv")
wp = open("desc.csv", "w+")
fp.readline()

count = 0

for line in fp:
    count+=1
    pokeline = line.strip().lower().split(",")
    
    response = requests.get(url+pokeline[0])

    print(url+pokeline[0])
    soup = BeautifulSoup(response.text, "html.parser")
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
        try:
            myrow= list(row.children)
            # print(len(myrow))
            th, td = myrow[1], myrow[3]
            # print(th.contents, td.contents)
            thdata = []
            for element in th.find_all("span"):
                thdata.append(element.contents[0])

            thdata = "&".join(thdata)
            string = thdata + ": "+td.contents[0]
            
            para.append(string)

        except Exception as e:
            print(e)
            para = "Error in scraping"
        # print("th", th,"td", td, "ok")
    # print(para)
    para = "^".join(para)
    data = line.strip()+","+para
    wp.write(data+"\n")
    if count==1:
        break
# number, name, descriptions (v:desc)

wp.close()
fp.close()