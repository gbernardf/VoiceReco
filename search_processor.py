import search_in_central


def get_search_results(data):
    if data["outcomes"][0]["intent"] == "search_by_themes":
        return search_theme(data)
    elif data["outcomes"][0]["intent"] == "search_by_mood":
        return search_mood(data)
    elif data["outcomes"][0]["intent"] == "search_by_mood_and_theme":
        return search_theme_and_mood_id(data)


def search_theme(item):
    return search_in_central.do_get_request_for_themes(get_themes_ids_from_item(item))


def search_mood(item):
    return search_in_central.do_get_request_for_wishes(get_moods_ids_from_item(item))


def search_theme_and_mood_id(item):
    moods = get_moods_ids_from_item(item)
    themes = get_themes_ids_from_item(item)
    return search_in_central.do_get_request_for_wishes_and_themes(moods, themes)


def get_moods_ids_from_item(item):
    moods = []
    for mood in item["outcomes"][0]["entities"]["mood"]:
        if mood.get("id"):
            moods.append(mood["id"])
    return moods


def get_themes_ids_from_item(item):
    themes = []
    for theme in item["outcomes"][0]["entities"]["theme"]:
        if theme.get("id"):
            themes.append(theme["id"])
    return themes
