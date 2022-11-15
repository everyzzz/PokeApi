import requests
import numpy as np
import urllib.request
import cv2
class Poke_Api:
    def __init__(self,name:str)->dict:
        url_pokeapi= (f'https://pokeapi.co/api/v2/pokemon/{name}/')
        #Verificación de url "200" si está bien
        print(requests.get(url_pokeapi))
         
        #Obtener datos de json
        self.response = requests.get(url_pokeapi)
        self.data= self.response.json()
        
    def obtener_nombre_peso(self):
        return f"\nPokemon: {self.data['name'].capitalize()}\n \nPeso:  {self.data['weight']} lb\n"

    def obtener_tipo(self):
        type_poke= [types['type']['name']for types in self.data['types']]
        return("Tipo: "+"-".join(type_poke))        

    def obtener_habilidades(self):
        #Lista de habilidades
        hab=[nombre_hab['ability']['name']for nombre_hab in self.data['abilities']]
        return "Habilidades:  "+ ", ".join(hab)
    
    def obtener_imagen(self):
        #Listar url de imagen
        lista_foto=[j for j in self.data['sprites']['other']['official-artwork']['front_default']]
        foto = "".join(lista_foto)

        resp = urllib.request.urlopen(foto)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        cv2.imshow("Image", image)
        cv2.waitKey(0)
        return "Terminó el proceso"
    
    def obtener_stats(self):
        stats=[k['base_stat'] for k in self.data['stats']]
        return f"\nSalud:  {stats[0]} \n\nAtaque:  {stats[1]} \n\nDefensa:  {stats[2]} \n\nAtaque Especial:  {stats[3]} \n\nDefensa Especial:  {stats[4]} \n\nVelocidad:  {stats[5]}\n"
            
        
nombre_pokemon=input("Ingrese nombre de pokemón>> ")    
pokeAPI= Poke_Api(nombre_pokemon)
print(pokeAPI.obtener_nombre_peso())
print(pokeAPI.obtener_habilidades())
print(pokeAPI.obtener_stats())
print(pokeAPI.obtener_tipo())
print(pokeAPI.obtener_imagen())

