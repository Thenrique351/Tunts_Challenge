import requests
import json

def request_url(url):
    request = requests.get(url)
    data = request.json()#Json open 

    country_list = []

    for i in data:
        x = i.get('name')
        country = x.get('common','-')
        
        #print(y)
        x = i.get('capital','-')
        capital = x[0]
        #print(y)
        area = i.get('area','-')
        #print(x)
        x = i.get('currencies','-')
        if(x != '-'):
            #currencies = str(list(x.keys())).strip('[]')
            currencies = ', '.join((list(x.keys())))#convert the dict type in list type
        else:
            currencies = '-' 
        dicionario = {'Name': country, 'Capital': capital, 'Area': area, 'Currencies': currencies}
        country_list.append(dicionario)#Add object in list, on format {Name, Capital, Area, Currencies}
    
    return country_list #Return  Json objects by name, capital, area and currencies in list of  dictionary python format
