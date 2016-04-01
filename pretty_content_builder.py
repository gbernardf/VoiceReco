import json
import requests

server_address = "http://localhost:8080/SpideoCentral/contents/"
# server_address = "http://technicolor.dev.spideo.com/contents/"
recos = []


def print_contents(response):
    response_json = json.loads(response)
    if response_json.get("contents"):
        display_contents_titles(response_json)
    else:
        display_not_found()


def add_content_title(content_json):
    recos.append(content_json["title"])


def display_contents_titles(contents):
    for content in contents["contents"]:
        content_json = requests.get(server_address + content).json()
        add_content_title(content_json)
    print "Those might please you:"
    for content in recos:
        print "-\t" + content
    print ""


def display_not_found():
    print "Sorry your query produced no result."
