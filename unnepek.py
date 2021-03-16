import datetime
import json
import sys


# Create events data 
with open('events.json') as json_file:
    event_json_object = json.load(json_file)

# Grab today's date in MM/DD format to pull data for that specific date.
today = datetime.datetime.today()
today_formatted = today.strftime('%m/%d')
today_date = today.strftime("%m/%d/%Y")

# Grab relevant list from JSON object dictionary
def get_event(event_date):
    try:
        events = event_json_object[event_date]
        for event in events:
            if event:
                print(event)
    except KeyError:
        print("No events were found for today.")
        sys.exit()

#longest_string = max(events, key=len)
#width = 29 - len(longest_string)

# print("┌" + "─" * 30 + "┐")
# print("│ " + "Mai ünnepek " + today_date + " " * 7 + "│") 
# print("│" + " " * 30 + "│")
print("Today's events:")
# for event in events:
    # width = 29 - len(event)
    # print("│ " + event + " " * width + "│")
    # if event == today_formatted:
    #    print(event)
print(get_event(today_formatted))
tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
tomorrow_formatted = tomorrow.strftime('%m/%d')
print("Tomorrow's events:")
print(get_event(tomorrow_formatted))
#print("└" + "─" * 30 + "┘")
