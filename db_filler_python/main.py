import json
from async_requests_by_list import Async_req_from_list as as_req

#file = open('./cities_data.json')

#data = json.load(file)

#print(data[1]['monumenti'][1]['Opere'][0]['Autore']['periodi'][2])

BASE_GOOGLE_URL = ""
BASE_NODE_API_URL = "http://localhost:3001/api/insert/"
                
                
"""
open 
1. citta
2. sedi
3. autori
4. correnti
5. opere

"""

def main():
    
    urls = []
    
    citta = json.load(open('./JSONs/citta.json', 'r'))
    sedi = json.load(open('./JSONs/sedi.json', 'r'))
    autori = json.load(open('./JSONs/autori.json', 'r'))
    correnti = json.load(open('./JSONs/correnti.json', 'r'))

    for c in citta:
        urls.append({
            "url": f"{BASE_NODE_API_URL}citta",
            "data": c
        })
        
    for a in autori:
        urls.append({
            "url": f"{BASE_NODE_API_URL}autore",
            "data": a
        })
        
    for c in correnti:
        urls.append({
            "url": f"{BASE_NODE_API_URL}corrente",
            "data": c
        })   
    as_req.post(urls)
    urls = []
    for s in sedi:
        urls.append({
            "url": f"{BASE_NODE_API_URL}sede",
            "data": s
        })
    as_req.post(urls)   

def test():
    for s in sedi:
        print(s)
        print("\n")

if __name__ == "__main__":
    main()
    #test()