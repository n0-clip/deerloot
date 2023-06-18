import xml.etree.ElementTree as ET

def search_item():
    while True:
        search_term = input("\nEnter the item you're looking for (or 'q' to quit): ").lower()
        if search_term == 'q':
            break

        tree = ET.parse('types.xml')
        root = tree.getroot()

        matches = []
        for type_tag in root.findall('type'):
            name = type_tag.get('name').lower()
            if search_term in name:
                matches.append(type_tag)

        if len(matches) == 0:
            print("No matches found.")
        elif len(matches) == 1:
            print_tier_locations(matches[0])
        else:
            print("\nMultiple matches found:")
            for i, match in enumerate(matches, start=1):
                print(f"{i}. {match.get('name')}")
            choice = int(input("\nChoose a number from the list: ")) - 1
            print_tier_locations(matches[choice])

def print_tier_locations(type_tag):
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

    print(f"\nLocations for {type_tag.get('name')}:")
    for value in type_tag.findall('value'):
        tier = value.get('name')
        if tier in tier_locations:
            print(f"{tier}: {', '.join(tier_locations[tier])}")

if __name__ == "__main__":
    print("daz's 'deerloot' Version: 0.2.0")
    search_item()