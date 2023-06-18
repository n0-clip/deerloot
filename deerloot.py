import xml.etree.ElementTree as ET

# Map of tiers to locations
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

# Parse the XML file
tree = ET.parse('types.xml')
root = tree.getroot()

# Get user input
user_input = input("Enter the exact loot name: ")

# Find the type entry that matches the user's input
for type_entry in root.findall('type'):
    if type_entry.get('name') == user_input:
        # Find the tiers within this type entry
        for value in type_entry.findall('value'):
            tier = value.get('name')
            # Print the locations for this tier
            print(f"{tier}: {', '.join(tier_locations[tier])}")
        break
