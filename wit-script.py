import wit
import time
import datetime

access_token = 'CX6U6BQL7Y7GA7LXVG2CD6ONKY53TQJL'
END_FILE_NAME = "_witResponses.json"

def write_data_to_file( data ):
	currentTime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H:%M:%S') #2012-12-15 01:21:05
	filename = currentTime + END_FILE_NAME
	fo = open(filename, "w")
	fo.write( "[" + data + "]" )	
	fo.close()

def get_user_inputs():
	
	data = ""

	while(True):
		userInput = str(raw_input("Enter query: "))
		if( userInput == "stop"):
			break
		if(data != ""):
			data += ","
		data += wit.text_query( userInput, access_token )

	write_data_to_file( data )



wit.init()



get_user_inputs()

print("closing now...\n")


#wit.voice_query_auto_async(access_token, process_response)


wit.close()