# daz's deerloot

## Version
0.2.0

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
