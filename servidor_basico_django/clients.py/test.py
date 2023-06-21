import requests 

endpoint_p = 'http://127.0.0.1:8000/pokemon/1'
endpoint_a = 'http://127.0.0.1:8000/ability/1'

endpoint_add_pokemon = 'http://127.0.0.1:8000/pokemon/create'
endpoint_add_ability = 'http://127.0.0.1:8000/ability/create'

endpoint_del_pokemon = 'http://127.0.0.1:8000/pokemon/5/delete'
endpoint_up_pokemon = 'http://127.0.0.1:8000/pokemon/6/update'

endpoint_api_view = 'http://127.0.0.1:8000/ability'

# PARA COMPROBAR LOS POKEMON Y HABILIDADES AÑADIDOS
# response = requests.get(endpoint_p)
# response = requests.get(endpoint_a)

# PARA VER EL LISTADO DE POKEMON Y HABILIDADES
# response = requests.get(endpoint_add_pokemon)
# response = requests.get(endpoint_add_ability)

# AÑADIENDO POKEMON
# response = requests.post(endpoint_add_pokemon, json={'name': 'Pikachu', 'dexNumber': 25, 'ability': 'Electricidad Estática'})
# response = requests.post(endpoint_add_pokemon, json={'name': 'Raichu', 'dexNumber': 26, 'ability': 'Electricidad Estática'})
# response = requests.post(endpoint_add_pokemon, json={'name': 'Bulbasaur', 'dexNumber': 1, 'ability': 'Espesura'})
# response = requests.post(endpoint_add_pokemon, json={'name': 'Ivysaur', 'dexNumber': 2, 'ability': 'Espesura'})
# response = requests.post(endpoint_add_pokemon, json={'name': 'Venusaur', 'dexNumber': 3, 'ability': 'Espesura'})

# AÑADIENDO HABILIDADES
# response = requests.post(endpoint_add_ability, json={'aName': 'Electricidad Estática', 'description': 'Paraliza al contacto'})
# response = requests.post(endpoint_add_ability, json={'aName': 'Espesura', 'description': 'Potencia movimientos tipo Planta en apuros'})

# PROBANDO LOS DELETE Y PUT
# response = requests.delete(endpoint_del_pokemon) 'AQUI BORRE A VENUSAUR, que equivale al pokemon 5'
# response = requests.put(endpoint_up_pokemon, json={'name': 'Mew', 'dexNumber': 151, 'ability': 'Levitación'})

# INSERCIONES DE COMPROBACIÓN
# response = requests.post(endpoint_add_pokemon, json={'name': 'Mewtwo', 'dexNumber': 150, 'ability': 'Presión'})
# response = requests.post(endpoint_add_ability, json={'aName': 'Levitación', 'description': 'Evita movimientos de Tierra'})
# response = requests.post(endpoint_add_ability, json={'aName': 'Presión', 'description': 'Ejerce Presión'})

# PROBANDO EL API_VIEW
response = requests.get(endpoint_api_view)

print(response.json())