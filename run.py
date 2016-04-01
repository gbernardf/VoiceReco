import wit

import process_query

wit.init()
print "Enter a sentence query or hit Ctrl + C to close the program..."
while True:
    query = raw_input("I'm listening.\n")
    process_query.process(query)
