import requests

server_address = "http://localhost:8080/SpideoCentral"
search_url = server_address + "/search/vod?"

def do_get_request_for_wishes_and_themes(moods, themes):
	query = query + "wishes="
	query = add_elements(query, moods)
	query = query + "&themes="
	query = add_elements(query, themes)
	response = requests.get(query)
	return response

def do_get_request_for_wishes(moods):
	query = query + "wishes="
	query = add_elements(query, moods)
	response = requests.get(query)
	return response

def do_get_request_for_themes(moods, themes):
	query = query + "themes="
	query = add_elements(query, themes)
	response = requests.get(query)
	return response

def add_elements(query, elements):
	for element in elements:
		query += element + ','
	query = query[:-1]
	return query
