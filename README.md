# Deerloot

Deerloot is a Python-based tool for looking up loot tables in the DayZ "Deer Isle" map. It allows for searching items in an XML file and displaying their associated locations and usages.

## How to Use Deerloot

1. Ensure Python is installed on your system.
2. Download or clone this repository to your machine.
3. Via the command line, navigate to the directory with the script.
4. Run the script with `python deerloot.py`.
5. Follow the on-screen prompts to search for items.
6. If multiple matches are found, choose from the provided list.
7. Locations and usages for the chosen item will be displayed.
8. Enter 'q' at the search prompt to quit.

## Upcoming Features

- Color-coded output based on map tier list.
- Support for additional maps.
- Detailed information about items and their locations.
- Improved handling for entries without location information.
- Enhanced error handling and code modularity.

## Changelog

**Version 0.4.0 - June 18 2023**
- New Feature: Usage information of each item is now displayed.
- Improvement: Enhanced XML parsing to include item usage.

**Version 0.3.0 - June 18 2023**
- New Features: Added functions for loading tier locations from JSON and for user input validation.
- Improvement: Refactored main functions for improved modularity and error handling.
- Bug Fix: Resolved argument mismatch in function call.
- Other: Tier locations are now stored separately for easier updates.

**Version 0.2.0 - June 18 2023**
- New Feature: Partial term search enabled for more flexible item lookup.
- Improvement: Enhanced search_item function for improved usability.
- Bug Fix: Resolved an issue where items without location information were showing as results.

**Version 0.1.0 - June 18 2023**
- Initial release: Basic item search and location display functionality implemented.
