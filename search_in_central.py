import requests

server_address = "http://localhost:8080/SpideoCentral"
#server_address = "http://technicolor.dev.spideo.com"
search_url = server_address + "/search/vod?"


def do_get_request_for_wishes_and_themes(moods, themes):
    query = "wishes="
    query = add_elements(query, moods)
    query += "&themes="
    query = add_elements(query, themes)
    response = requests.get(search_url + query)
    return response.text


def do_get_request_for_wishes(moods):
    query = "wishes="
    query = add_elements(query, moods)
    response = requests.get(search_url + query)
    return response.text


def do_get_request_for_themes(themes):
    query = "themes="
    query = add_elements(query, themes)
    print search_url + query
    response = requests.get(search_url + query)
    return response.text


def add_elements(query, elements):
    for element in elements:
        query += element + ','
    query = query[:-1]
    return query
