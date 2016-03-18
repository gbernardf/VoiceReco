import json

def parse_outcome( outcome ):
	if( outcome["intent"] == "Set_temperature"):
		temp_setter.process(outcome)
	elif(outcome["intent"] == "Get_temperature"):
		temp_getter.process(outcome)
	else:
		print("Could not guess Intent :/ ")


data_file = open("last_witResponses.json","r")

data = json.loads(data_file.read())

for d in data:
	parse_outcome(d["outcomes"][0])

