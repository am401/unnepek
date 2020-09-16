import datetime
import json
import sys


# Create events data 
event_data_string = '{"dates": [{"09/15": ["Test case", "Second event", "Something else", "Another thing"], "09/16": "Should not display"}]}'
event_json_object = json.loads(event_data_string)

# Grab today's date in MM/DD format to pull data for that specific date.
today = datetime.datetime.today()
today = today.strftime('%m/%d')

# Grab relevant list from JSON object dictionary
try:
    events = event_json_object['dates'][0][today]
except KeyError:
    print("No events were found for today.")
    sys.exit()

for event in events:
    print(event)
