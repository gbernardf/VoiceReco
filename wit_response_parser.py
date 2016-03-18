import json

themes_path = "TechnicolorThemes.json"
moods_path = "TechnicolorMoods.json"
wit_responses_path = "wit_responses.json"

with open(wit_responses_path) as data_file:  
	data = json.load(data_file)
with open(themes_path) as themes_data_file: 
	themes = json.load(themes_data_file)
with open(moods_path) as moods_data_file: 
	moods = json.load(moods_data_file)

def prepare_json_for_search():
	for item in data:
		if item["outcomes"][0]["entities"]["intent"] == "search_by_themes":
			add_theme_id(item)
		elif item["outcomes"][0]["entities"]["intent"] == "search_by_mood":
			add_mood_id(item)
		elif item["outcomes"][0]["entities"]["intent"] == "search_by_mood_and_theme":
			add_theme_and_mood_id(item)

	with open('wit_responses_UPDATED.json', 'w') as outfile:
		json.dump(data, outfile)

def add_theme_id(item):
	for textTheme in item["outcomes"][0]["entities"]["theme"]:
			textTheme['id'] = [theme["_id"] for theme in themes
            if theme["nom"].lower() == textTheme["value"]]

def add_mood_id(item):
		for textMood in item["outcomes"][0]["entities"]["mood"]:
			textMood['id'] = [mood["_id"] for mood in moods
            if mood["nom"].lower() == textMood["value"]]

def add_theme_and_mood_id(item):
	add_theme_id(item)
	add_mood_id(item)

