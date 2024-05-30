import requests
from bs4 import BeautifulSoup

url = 'https://catalog.data.gov/dataset'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
names =[]
views = []
header = []
datas = []

answers = [f"<h1>exercise3</h1>"]
for dataset in soup.find_all('h3', class_ = 'dataset-heading'):
    name = dataset.find('a').text
    view_text = dataset.find('span').text
    view = view_text.split()[0]
    answer = f"<p>{name} - {view}</p>"
    answers.append(answer) 
    views.append (view)
    names.append (name)


for i in range(len(names)) :
    view = views[i]
    name = names[i]
    td1 = f"<td>{name} </td>"
    td2 = f"<td>{view} </td>"
    tr = f"<tr>{td1}{td2} </tr>"
    datas.append (tr)

header = f"<tr> <th>headers</th> <th>views</th> </tr>"

total = f"<h1>exercise4</h1>\n{header}\n"

for d in datas :
    total += f"{d}\n"

#Puting total string into table tag
total = f"<table>{total} </table>"

with open('catalog_data_gov_table.html', 'w') as file :
    file.write(total)

with open('catalog_data_gov.html', 'w') as file :
    for a in answers:
        file.write(a+'\n')
        
for name, view in zip(names, views):
    print(f"{name} - {view} views")