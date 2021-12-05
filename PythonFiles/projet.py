import json
import re

from ourFunction import add_elem_to_dict
from ourFunction import filter_on_dict
from ourFunction import gather_information

decode = False

try:
    with open('../News_Category_Dataset_v2.json') as f:
        data = json.load(f)
    decode = True
except ValueError:
    print("Decoding initial JSON file has failed")

if not decode:
    try:
        print("Trying to decode JSON file")
        file = open("../News_Category_Dataset_v2.json", "r")
        lines = file.readlines()
        new_data = {}
        [(add_elem_to_dict(new_data, idx, json.loads(elem))) for idx, elem in enumerate(lines)]
        with open('data.json', 'w') as outfile:
            json.dump(new_data, outfile)
        print("New json file generated ! ")
        with open('data.json') as f:
            data = json.load(f)
    except:
        print("Decoding JSON has failed. Please correct your dataset")

# We filter our data in order to get a specific small sample
filtered_dict = filter_on_dict(data, "category", "WORLD NEWS")

# We decide to keep only value in 'headline' and 'short_description'
keeped_information = ["headline", "short_description"]
# All the data is stock in a list : gathered_data
gathered_data = gather_information(filtered_dict, keeped_information)

# Split each sentence in list of word without punctuations and text as lower()
corpus = ([re.sub(r'[^\w\s]', '', gathered_data[x].lower()).split() for x in range(len(gathered_data))])
print(corpus[0:2])
