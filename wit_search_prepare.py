import json
from pymongo import MongoClient

wit_responses_path = "json/wit_responses.json"
client = MongoClient()

def prepare_json_for_search(filepath):
    with open(wit_responses_path) as data_file:
    	data = json.load(data_file)
    	for item in data:
    		if item["outcomes"][0]["intent"] == "search_by_themes":
    			add_theme_id(item)
    		elif item["outcomes"][0]["intent"] == "search_by_mood":
    			add_mood_id(item)
    		elif item["outcomes"][0]["intent"] == "search_by_mood_and_theme":
    			add_theme_and_mood_id(item)

    	with open(filepath, 'w') as outfile:
    		json.dump(data, outfile)

def add_theme_id(item):
    db = client.ExportLea
    for textTheme in item["outcomes"][0]["entities"]["theme"]:
        themeName = make_firsts_letters_upper(textTheme["value"])
        cursor = db.Theme.find({"nom":themeName, "langueCode":"en"})
        for document in cursor:
            print("Document Id: " + document["_id"])
            textTheme['id'] = document["_id"]

def add_mood_id(item):
    db = client.ExportLea
    for textMood in item["outcomes"][0]["entities"]["mood"]:
        moodName =  make_firsts_letters_upper(textMood["value"])
        cursor = db.Envie.find({"mapLangueCode.en":textMood["value"]})
        for document in cursor:
            print("Document Id: " + document["_id"])
            textMood['id'] = document["_id"]


def add_theme_and_mood_id(item):
    add_theme_id(item)
    add_mood_id(item)

def make_firsts_letters_upper(string):
    charList = [0]
    for i,char in enumerate(string):
        if (i != 0) and (string[i-1] == ' '):
            charList.append(i)
    chars = list(string)
    for i in charList:
        chars[i] = chars[i].upper()
    returnString = ''.join(chars)
    print(returnString)
    return returnString
