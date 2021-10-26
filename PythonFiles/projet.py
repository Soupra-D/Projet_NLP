import json
import re

def add_elem_to_dict(dictionary, key, value):
    dictionary[key] = value

def filter_on_dict(entry_dic, entry_key, entry_value, useless_key=None):
    new_dico = {}
    for key, dico in entry_dic.items() :
        for key2, value in dico.items() :
            if(key2==str(entry_key) and value==str(entry_value)):
                new_dico[key] = dico
    return new_dico

def gather_information(entry_dict, list_of_key):
    list_of_sentence = []
    for key, dico in entry_dict.items() :
        for key in list_of_key:
            list_of_sentence.append(dico[key])
    return list_of_sentence

#Not operationnal for the moment
"""def remove_useless_key(entry_dic, list_of_keys):
    edit_dict = entry_dic
    for key in list_of_keys:
        edit_dict.pop(key)
    return edit_dict"""



decode = False

try :
    with open('News_Category_Dataset_v2.json') as f:
        data = json.load(f)
    decode=True
except ValueError:
    print("Decoding initial JSON file has failed")

try :
    if(decode==False):
        print("Trying to decode JSON file")
        file = open("News_Category_Dataset_v2.json", "r")
        lines = file.readlines()
        new_data = {}
        [(add_elem_to_dict(new_data, idx, json.loads(elem))) for idx, elem in enumerate(lines)]
        with open('data.json', 'w') as outfile:
            json.dump(new_data, outfile)
        print("New json file generated ! ")
except :
    print("Decoding JSON has failed. Please correct your dataset")

with open('data.json') as f:
    data = json.load(f)

useless_keys = ['link']
test = filter_on_dict(data, "category", "WORLD NEWS", useless_keys)
"""print(type(test))
print(test.keys())"""
print(test["11"])

keeped_information = ["headline", "short_description"]
gathered_data = gather_information(test, keeped_information)

corpus = ([re.sub(r'[^\w\s]', '',  gathered_data[x].lower()).split() for x in range(len(gathered_data))])
print(corpus[0:2])
