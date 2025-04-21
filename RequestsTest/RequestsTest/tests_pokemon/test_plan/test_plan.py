import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'user_token'
HEADERS = {'Content-Type' : 'application/json','trainer_token' : TOKEN}
TRAINER_ID = '28718'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID} )
    assert response.status_code == 200

def test_part_code():
    respons_get = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID} )
    assert respons_get.json()['data'][0]['trainer_name'] == 'Саймоша'