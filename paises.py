import json
import sys

import requests

URL_ALL = "https://restcountries.eu/rest/v2/all"
URL_NAME = "https://restcountries.eu/rest/v2/name"


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print("Erro de requisição em:", url)


def parsing(resposta_text):
    try:
        return json.loads(resposta_text) #parsing json => py
    except:
        print("Parsing error")


def country_counter():
    resposta = requisicao(URL_ALL)
    if resposta:    
        country_list = parsing(resposta)
        if country_list:
            return len(country_list)


def list_countries(country_list):
    for country in country_list:
        print(country['name'])
        

def pop_list(country_name):
    resposta = requisicao("{}/{}".format(URL_NAME, country_name))
    if resposta:    
        country_list = parsing(resposta)
        if country_list:
            for country in country_list:
                print("{}: {}".format(country['name'], country['population']))
    else:
        print("Country not found")        


def show_currencies(country_name):
    resposta = requisicao("{}/{}".format(URL_NAME, country_name))
    if resposta:    
        country_list = parsing(resposta)
        if country_list:
            for country in country_list:
                print("{} currency: ".format(country['name']))
                currencies = country['currencies']
                for currency in currencies:
                    print("{} - {}".format(currency['name'], currency['code']))
        else:
            print("Country not found")   


def country_name_reading():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print("Please, insert the country")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Welcome to the country API\n")
        print("How to: python paises.py <action> <country name>\n")
        print("Available actions:\ncounting, currencies, population")
    else:
        argument1 = sys.argv[1]
        
        if argument1 == 'counting':
           countries_number = country_counter()
           print("Total number of countries: {}".format(countries_number))
        elif argument1 == 'currencies':
            pais = country_name_reading()
            if pais:
                show_currencies(pais)
        elif argument1 == 'population':
            pais = country_name_reading()
            if pais:
                pop_list(pais)
        else:
            print("Invalid parameter")
            
            
