import requests

def lista_paises(url):
    paises = requests.get(url)
    paises = paises.json()


    for p in paises:
        print(f"Nombre Oficial en Español: {p['translations']['spa']['official']}")
        print(f"La capital es: {p['capital'][0]}")
        moneda = p['currencies']
        for m in moneda.values():
            print(f"El nombre de la moneda es: {m['name']} y su símbolo es: {m['symbol']}")
        ctele = p['idd']['root'] + p['idd']['suffixes'][0]
        print(f"El Código Telefónico es: {ctele}")

url = 'https://restcountries.com/v3.1/independent?status=true&fields=translations,capital,currencies,idd'
lista_paises(url)
