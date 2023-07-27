
import requests

def lista_paises(url):
    paises = requests.get(url)
    paises = paises.json()
    lista_areas = []
    lista_poblacion = []
    lista_countries = []
    lista_pais_pob = []


    for p in paises:
        n_pais = p['translations']['spa']['official']
        print(f"Nombre Oficial en Español: {n_pais}")
        area = p['area']
        print(f"El área es de: {area}")
        poblacion = p['population']
        print(f"La población es de: {poblacion} habitantes")

        lista_countries.append(n_pais)
        lista_areas.append(area)
        lista_poblacion.append(poblacion)
    lista_pais_pob.append(lista_countries)
    lista_pais_pob.append(lista_poblacion)

    def mayor_pa(lista):
        return max(lista)

    def poblacion_total(lista):
        return sum(lista)

    def media(lista):
        return sum(lista)/len(lista)

    def mediana(lista):
        lista_ordenada = sorted(lista)
        im_par = len(lista_ordenada)//2
        if len(lista) % 2 != 0:
            return lista_ordenada[im_par]

        return (lista_ordenada[im_par - 1] + lista_ordenada[im_par]) / 2

    def moda(lista):
        frecuencia = {}
        for value in lista:
            frecuencia[value] = frecuencia.get(value, 0) + 1
        mayor_frecuencia = max(frecuencia.values())
        modas = [key for key, value in frecuencia.items()
                    if value == mayor_frecuencia]
        return modas

    print("\nEstadísticas")
    print(f"El país con mayor población es: {mayor_pa(lista_poblacion)}")
    print(f"El país de mayor área es: {mayor_pa(lista_areas)}")
    print(f"La población total es: {poblacion_total(lista_poblacion)} habitantes.")
    print(f"La media de la población es: {media(lista_poblacion)}")
    print(f"La mediana de la población es: {mediana(lista_poblacion)}")
    print(f"La moda de la población es: {moda(lista_poblacion)}")


url = 'https://restcountries.com/v3.1/all'
lista_paises(url)
