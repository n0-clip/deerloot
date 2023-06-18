# deerloot

## Version
0.4.0

## Description
This is a Python-based tool for use with the DayZ map "Deer Isle" for searching items in an XML file and displaying their associated locations based on tier values. The tool supports case-insensitive and partial term searching. When multiple matches are found, the tool provides a numbered list for users to select the item they are interested in.

## Usage
1. Ensure you have Python installed on your system.
2. Download or clone this repository to your local machine.
3. Navigate to the directory containing the script via the command line.
4. Run the script using the command `python deerloot.py`.
5. When prompted, enter the name of the item you're looking for. The search is case-insensitive and accepts partial terms.
6. If multiple matches are found, you will be presented with a numbered list. Enter the number of the item you're interested in.
7. The tool will display the locations associated with the chosen item based on tier values.
8. To quit the program, enter 'q' at the search prompt.

## To-Do
- Implement colour-coded output based on original map tier list.
- Add support for more maps.
- Perhaps an option to go into more detail about the item and where it's found.
- Fix entries with no loot location info from showing as a search result.
- Error handling, input validation, xml parsing efficiency, modularity

# Changelog
Version 0.4.0 - June 2023
## New Features:
The print_tier_locations function now also prints the usage information of each item.
## Improvements:
Updated the print_tier_locations function to extract and print the 'usage' tags of each item from the XML file.
This update enhances the functionality of the print_tier_locations function by adding the ability to display the usage information for each item in addition to its tier locations. This makes the output of the script more informative for the user.

Version 0.3.0 - June 2023
## New Features:
Added a new function load_tier_locations to load tier locations from a JSON file.
Added a new function get_user_choice to ask the user to choose a number within a given range and validate the input.
## Improvements:
Modified the search_item function to use the get_user_choice function for user input and to accept the XML root as a parameter.
Modified the print_tier_locations function to accept a dictionary of tier locations as a parameter.
## Bug Fixes:
Fixed a bug where the print_tier_locations function was called with one argument instead of two.
## Other Changes:
The tier locations are now stored in a separate JSON file for easier updates and better separation of data and code.
Added error handling for file reading and parsing operations.