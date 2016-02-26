import wit
import json

access_token = 'LHCD4AQ4LF3REAOWFF2WDR2LFMXMZZXU'
END_FILE_NAME = "JSON_returns.json"
INPUT_FILE_NAME = "wit_queries.txt"

def write_data_to_file( data ):
	filename = END_FILE_NAME
	fo = open(filename, "w")
	fo.write( "[" + data + "]" )
	fo.close()

def get_inputs():
	queries = open(INPUT_FILE_NAME,'r')
	data = ""
	for query in queries.readlines():
	    #wit.text_query_async(query, 'ACCESS_TOKEN', append_data)
		response = wit.text_query( query, access_token )
		data += response + ','
	write_data_to_file(data)


wit.init()
get_inputs()

print("closing now...\n")
wit.close()
