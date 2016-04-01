import wit
import json
import wit_search_prepare
import search_in_central


access_token = 'LHCD4AQ4LF3REAOWFF2WDR2LFMXMZZXU'
QUERIES_FILE = "queries/wit_queries.txt"
WIT_RESPONSE = "json/wit_responses.json"
END_FILE_NAME = "json/wit_responses.json"
UPDATED_FILE_NAME = 'json/wit_responses_UPDATED.json'

def write_data_to_file( data ):
	filename = WIT_RESPONSE
	fo = open(filename, "w")
	fo.write( "[" + data + "]" )
	fo.close()

def get_inputs():
	queries = open(QUERIES_FILE,'r')
	data = ""
	for query in queries.readlines():
	    #wit.text_query_async(query, 'ACCESS_TOKEN', append_data)
		response = wit.text_query( query, access_token )
		data += response + ','
	data = data[:-1]
	write_data_to_file(data)
	wit_search_prepare.prepare_json_for_search(UPDATED_FILE_NAME)

def get_search_results():
	with open(UPDATED_FILE_NAME) as data_file:
		data = json.load(data_file)
		for item in data:
			if item["outcomes"][0]["intent"] == "search_by_themes":
				search_theme(item)
			elif item["outcomes"][0]["intent"] == "search_by_mood":
				search_mood(item)
			elif item["outcomes"][0]["intent"] == "search_by_mood_and_theme":
				search_theme_and_mood_id(item)

def search_theme(item):
	if(is_good_candidate(item)):
		print search_in_central.do_get_request_for_themes(get_themes_ids_from_item(item))

def search_mood(item):
	if(is_good_candidate(item)):
		print search_in_central.do_get_request_for_wishes(get_moods_ids_from_item(item))

def search_theme_and_mood_id(item):
	if(is_good_candidate(item)):
		moods = get_moods_ids_from_item(item)
		themes = get_themes_ids_from_item(item)
		print(search_in_central.do_get_request_for_wishes_and_themes(moods, themes))

def get_moods_ids_from_item(item):
	moods = []
	for mood in item["outcomes"][0]["entities"]["mood"]:
		moods.append(mood["id"])
	return moods

def get_themes_ids_from_item(item):
	themes = []
	for theme in item["outcomes"][0]["entities"]["theme"]:
		themes.append(theme["id"])
	return themes

def is_good_candidate(item):
	return item["outcomes"][0]["confidence"] >= 0.7

wit.init()
get_inputs()
get_search_results()

print("closing now...\n")
wit.close()
