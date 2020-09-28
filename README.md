# ünnepek
This is an homage to an application my couson created back in over twenty years ago that I fondly remember. It notified you of upcoming birthdays and [name days](https://en.wikipedia.org/wiki/Name_day#Hungary). As I journey on with improving my Python knowledge I decided to start experimenting with the concept.

# events.json
The content of the events has been moved to a file called `events.json`. The format for this file is:

```
{"09/27": "Sample event", "09/28": ["Another sample event", "Next event in the list"]}
```

Create a list within the file when multiple events are needed for the same day.

# Sample output

This is a sample output including the box:

```
┌──────────────────────────────┐
│ Mai ünnepek 09/27/2020       │
│                              │
│ András teszt névnap          │
│ Matthew teszt nap            │
└──────────────────────────────┘
```

# TODO
Ideally I want to have the box be generated dynamically when it comes to width. This will require the existing script to be altered. Also allowing the user to add events to the file via command line arguments will help improve user friendliness.

# Changelog
## [0.1] - 2020-09-27
### Added
- Box around the output text including the current date that events are occurring on

### Changed
- Removed the JSON string from the file itself and moved it to events.json 
