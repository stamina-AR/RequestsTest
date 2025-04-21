import requests 
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'users_token'
HEADERS = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
BODY_CREATE = {
    "name": "Liza",
    "photo_id": 15}
response = requests.post(url= f'{URL}/pokemons', headers = HEADERS, json = BODY_CREATE)
print(response.status_code)
print(response.text)
POKEMON_ID = response.json()['id']
BODY_NAME = {
    "pokemon_id": "285920",
    "name": "Подмена",
    "photo_id": 15
}
response_name = requests.put(url= f'{URL}/pokemons', headers = HEADERS, json = BODY_NAME)
print(response_name.status_code)
print(response_name.text)
BODY_POKEBOLL = {
    "pokemon_id": "285916"
}
response_pokeboll = requests.post(url= f'{URL}/trainers/add_pokeball', headers = HEADERS, json = BODY_POKEBOLL)
print(response_pokeboll.status_code)
print(response_pokeboll.text)

