
import requests

def get_all_pokemon_names():
    all_pokemon_names = []
    next_url = "https://pokeapi.co/api/v2/pokemon"
    
    while next_url:
        response = requests.get(next_url)
        if response.status_code == 200:
            data = response.json()
            results = data.get("results", [])
            all_pokemon_names.extend([entry["name"] for entry in results])
            next_url = data.get("next")
        else:
            next_url = None

    return all_pokemon_names

def get_pokemon():
    url = "https://pokeapi.co/api/v2/pokemon?limit=10"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return [entry["name"] for entry in data["results"]]
    else:
        return []

def get_pokemon_details(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        image = data["sprites"]["front_shiny"]
        types = [type_data["type"]["name"] for type_data in data["types"]]
        return (name, ', '.join(types),image)
    else:
        return None
    
def fetchdetails():
    #pokemon_names =  get_all_pokemon_names()
    pokemon_names =  get_pokemon()
    pokemon_details = []
    for pokemon_id in pokemon_names:
        details = get_pokemon_details(pokemon_id)
        if details:
            pokemon_details.append(details)
    return pokemon_details
            
        