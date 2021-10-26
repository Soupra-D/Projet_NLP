def add_elem_to_dict(dictionary, key, value):
    dictionary[key] = value

def filter_on_dict(entry_dic, entry_key, entry_value):
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