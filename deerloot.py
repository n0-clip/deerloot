# Import the required library
import xml.etree.ElementTree as ET

# Function to search for an item
def search_item():
    # Loop until the user decides to quit
    while True:
        # Ask the user for the item they're looking for
        search_term = input("\nEnter the item you're looking for (or 'q' to quit): ").lower()
        # If the user entered 'q', break the loop and end the program
        if search_term == 'q':
            break

        # Parse the XML file
        tree = ET.parse('types.xml')
        root = tree.getroot()

        # List to store matches
        matches = []
        # Loop through all 'type' tags in the XML
        for type_tag in root.findall('type'):
            # If the search term is found in the name attribute, add it to the matches list
            name = type_tag.get('name').lower()
            if search_term in name:
                matches.append(type_tag)

        # If no matches were found, print a message
        if len(matches) == 0:
            print("No matches found.")
        # If only one match was found, print its tier locations
        elif len(matches) == 1:
            print_tier_locations(matches[0])
        # If multiple matches were found, ask the user to choose one
        else:
            print("\nMultiple matches found:")
            for i, match in enumerate(matches, start=1):
                print(f"{i}. {match.get('name')}")
            choice = int(input("\nChoose a number from the list: ")) - 1
            print_tier_locations(matches[choice])

# Function to print the tier locations of a given item
def print_tier_locations(type_tag):
    # Dictionary mapping tiers to their locations
    tier_locations = {
        "Tier1": ["Crotch Island", "Barringer Island"],
        "Tier2": ["Start Island"],
        "Tier3": ["Main Island (South)"],
        "Tier4": ["Paris Island"],
        "Tier5": ["Swamp"],
        "Tier6": ["Main Island (North)"],
        "Tier7": ["Mt. Katahdin"],
        "Tier8": ["Main Island (East)"],
        "Tier9": ["Oilrigs"],
        "Tier10": ["Temple"],
        "Tier11": ["Powerplant"],
        "Tier12": ["Devils Eye"],
        "Tier13": ["Area 42"],
        "Tier14": ["Arctic"],
        "Tier15": ["Archipelago"],
        "Tier16": ["Barringer Crater"],
        "Tier17": ["Alcatraz"],
    }

    # Print the item name
    print(f"\nLocations for {type_tag.get('name')}:")

    # Loop through all 'value' tags of the item
    for value in type_tag.findall('value'):
        # If the value is a tier, print its locations
        tier = value.get('name')
        if tier in tier_locations:
            print(f"{tier}: {', '.join(tier_locations[tier])}")

# If the script is run directly (not imported), start the search
if __name__ == "__main__":
    print("daz's 'deerloot' Version: 0.2.0")
    search_item()
