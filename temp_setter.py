def process( wit_outcome ):
	analyse_set_temp( wit_outcome )

def analyse_set_temp( outcome ):
	print ("Received: \"" + outcome["_text"] + "\"")
	print ("Analysing...")
	print ("I've been told to change the temperature by:")
	parse_entities(outcome["entities"])
	print("\n")


def parse_entities(entities):
	action = entities["action"][0]["value"]	
	
	if( action == "put" or action == "set" ):
		values = entities["value"][0]
		if action == "put":
			print("Putting"),
		else:
			print("Setting"),
		print ("the thermostat to "),
		print ( str(values["value"]) ),
		if( "unit" in entities["value"][0]):
			print( values["unit"] )	
		else:
			print("")

	elif( action == "raise"):		
		if( "value" in entities ):
			values = entities["value"][0]
			print ("Raising up the thermostat by"),
			print ( str(values["value"]) + " " + values["unit"] ) 
		else:
			print("Raising the thermostat a bit.")

	elif( action == "lower"):		
		if( "value" in entities ):
			values = entities["value"][0]
			print ("Lowering down the thermostat by"),
			print ( str(values["value"]) + " " + values["unit"] ) 
		else:
			print("Lowering the thermostat a bit.")


	elif( action == "make"):
		temp_notch = entities["temperature_notch"][0]
		print ("Making the room "),
		print ( str(temp_notch["value"])) 
		if( temp_notch["value"] == "warmer"):
			print( "So I'll raise the temperature a bit.")
		elif( temp_notch["value"] == "colder" or temp_notch["value"] == "cooler"):
			print( "So I'll lower the temperature a bit.")

	if( "datetime" in entities ):
		print("I've been ask to do it at a special time but I'm too dumb to get that for now. :/")
