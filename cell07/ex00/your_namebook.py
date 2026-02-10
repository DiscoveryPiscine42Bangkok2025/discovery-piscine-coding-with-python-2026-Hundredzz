#!/usr/bin/env python3
def array_of_names(dictio:dict):
    arr = []
    for i,v in dictio.items():
        arr.append(i.capitalize() + " " +v.capitalize())
    return arr

persons = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_of_names(persons))