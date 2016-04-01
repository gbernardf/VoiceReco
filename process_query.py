import json
import wit

import search_prepare
import search_processor
import pretty_content_builder

access_token = 'LHCD4AQ4LF3REAOWFF2WDR2LFMXMZZXU'


def process(query):
    wit_response = wit.text_query(query, access_token)
    data = json.loads(wit_response)
    if is_good_candidate(data):
        search_prepare.prepare_json_for_search(data)
        search_result = search_processor.get_search_results(data)
        pretty_content_builder.print_contents(search_result)


def is_good_candidate(item):
    return item["outcomes"][0]["confidence"] >= 0.7
