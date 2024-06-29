#kimiya karami
import json
from bs4 import BeautifulSoup
import requests

json_data="""
{
    "bookstore":{
        "book1":{
            "_tag": "book",
            "attribute":[
                {
                    "category":"cooking"
                }
            ],
            "data":{
                "title":{
                    "_tag": "title",
                    "lang":"en",
                    "text":"everyday Italian"
                },
                "author":"Biade De Laurentiis",
                "year":"2005",
                "price":30
                
                
            }
        },
         "book2":{
            "_tag": "book",
            "attribute":[
                {
                    "category":"children"
                }
            ],
            "data":{
                "title":{
                    "_tag": "title",
                    "lang":"en",
                    "text":"Harry Potter"
                },
                "author":"J.K Rowling",
                "year":"2005",
                "price":29.99
        }        
    }
    
}"""
xml_data=""" ... """

def stocktwits_xml():
    response=requests.get(
        url="      ",
        headers={
            
            }
    )
    xml_data=response.text
    soup=BeautifulSoup(xml_data, features='lxml')
    location_list=soup.find_all('loc')
    coins_list=list()
    for location in location_list:
        text=location.text
        split_list=text.split('/') 
        coins_list.append(split_list[-1])
        # coins_list.append(location.text.split('/')[-1])
    if 'sags' in coins_list:
        print("match made!") 
        
if __name__ =='__main__':
    url="https://api.stocktwits.com/api/2/streams/suggested.json?filter=top&limit=20&max=578120474"
    headers={ "accept": "application/json" ,
     "accept-language": "en-US,en;q=0.9" ,
     "authorization": "OAuth 01cdb24a1fb940be715a3157403b00ffca29dc35" ,
     "origin": "https://stocktwits.com" ,
     "priority":" u=1, i" ,
     "referer": "https://stocktwits.com/" ,
     'sec-ch-ua': '"Google Chrome";v="125","Chromium"v="125", "Not.A/Brand";v="24"',
     "sec-ch-ua-mobile":" ?0" ,
     'sec-ch-ua-platform':'"Windows"' ,
     "sec-fetch-dest":" empty" ,
     "sec-fetch-mode": "cors" ,
     "sec-fetch-site": "same-site" ,
     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }
    data=requests.get(url,headers=headers)
    json_data= data.json()
    data={
        "book":{
            "title":"hello, world!!"
        }
    }
    print(json_data['bookstore']['book1']['attribute'][0]["category"])
    json_data=json.dumps(data)
    print(json_data)
    print()

 