import xml.etree.ElementTree as ET
import json

def load_tier_locations():
    """Load tier locations from a JSON file."""
    try:
        with open('tier_locations.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Tier locations file not found. Please check the file path.")
        exit(1)
    except json.JSONDecodeError:
        print("Failed to parse tier locations file. Please check the file format.")
        exit(1)

def get_user_choice(num_choices):
    """Ask the user to choose a number and return it."""
    while True:
        try:
            choice = int(input("\n Choose a number from the list: ")) - 1
            if 0 <= choice < num_choices:
                return choice
            else:
                print("Invalid choice. Please choose a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def search_item(root, tier_locations):
    """Search for an item in the XML root and print its tier locations."""
    while True:
        search_term = input("\n Enter the item you're looking for (or 'q' to quit): ").lower()
        if search_term == 'q':
            break

        matches = []
        for type_tag in root.findall('type'):
            name = type_tag.get('name').lower()
            if search_term in name:
                matches.append(type_tag)

        if len(matches) == 0:
            print("No matches found.")
        elif len(matches) == 1:
            print_tier_locations(matches[0], tier_locations)
        else:
            print("\n Multiple matches found:")
            for i, match in enumerate(matches, start=1):
                print(f"{i}. {match.get('name')}")
            choice = get_user_choice(len(matches))
            print_tier_locations(matches[choice], tier_locations)

def print_tier_locations(type_tag, tier_locations):
    """Print the tier locations of the given item."""
    print(f"\n Locations for {type_tag.get('name')}:")

    for value in type_tag.findall('value'):
        tier = value.get('name')
        if tier in tier_locations:
            print(f"{tier}: {', '.join(tier_locations[tier])}")

if __name__ == "__main__":
    print("daz's 'deerloot' Version: 0.3.0")

    tier_locations = load_tier_locations()

    try:
        tree = ET.parse('types.xml')
        root = tree.getroot()
    except ET.ParseError:
        print("Failed to parse XML file. Please check the file format.")
        exit(1)
    except FileNotFoundError:
        print("XML file not found. Please check the file path.")
        exit(1)

    search_item(root, tier_locations)
