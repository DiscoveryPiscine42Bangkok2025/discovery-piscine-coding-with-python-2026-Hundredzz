#!/usr/bin/env python3
def find_the_redheads(dictio:dict):
    return list(filter(lambda name: dictio[name] == 'red', dictio.keys()))

dupont_family = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(dupont_family))