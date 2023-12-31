#!/usr/bin/env python3

import itertools, collections

class Starmap:
    def __init__(self, category, starting_asteroid, *, teleport, short_flight=[]):
        self.category = category
        self.starting_asteroid = starting_asteroid
        self.teleport = teleport
        self.short_flight = short_flight
        self.long_flight = outer_asteroids

outer_asteroids = ["Tundra", "Marshy", "Moo", "Water", "Superconductive", "Regolith"]
starmaps = [
    Starmap("Classic",     "Terra",             teleport="Radioactive Swamp"),
    Starmap("Classic",     "Oceania",           teleport="Glowood Wasteland"),
    Starmap("Classic",     "Squelchy",          teleport="Radioactive Forest"),
    Starmap("Classic",     "Rime",              teleport="Stinko Swamp"),
    Starmap("Classic",     "Verdante",          teleport="Radioactive Terra"),
    Starmap("Classic",     "Arboria",           teleport="Radioactive Terra"),
    Starmap("Classic",     "Volcanea",          teleport="Radioactive Swamp"),
    Starmap("Classic",     "The Badlands",      teleport="Radioactive Swamp"),
    Starmap("Classic",     "Aridio",            teleport="Radioactive Terrabog"),
    Starmap("Classic",     "Oasisse",           teleport="Radioactive Swamp"),
    Starmap("Spaced Out!", "Terrania",          teleport="Oily Swamp",        short_flight=["Irradiated Forest"]),
    Starmap("Spaced Out!", "Folia",             teleport="Rusty Oil",         short_flight=["Irradiated Swamp"]),
    Starmap("Spaced Out!", "Quagmiris",         teleport="Rusty Oil",         short_flight=["Irradiated Marsh"]),
    Starmap("Spaced Out!", "Metallic Swampy",   teleport="Frozen Forest",     short_flight=["The Desolands",   "Flipped",       "Radioactive Ocean"]),
    Starmap("Spaced Out!", "The Desolands",     teleport="Radioactive Ocean", short_flight=["Metallic Swampy", "Frozen Forest", "Flipped"]),
    Starmap("Spaced Out!", "Frozen Forest",     teleport="The Desolands",     short_flight=["Metallic Swampy", "Flipped",       "Radioactive Ocean"]),
    Starmap("Spaced Out!", "Flipped",           teleport="The Desolands",     short_flight=["Metallic Swampy", "Frozen Forest", "Radioactive Ocean"]),
    Starmap("Spaced Out!", "Radioactive Ocean", teleport="Flipped",           short_flight=["Metallic Swampy", "The Desolands", "Frozen Forest"]),
    Starmap("The Lab",     "Skewed",            teleport="Radioactive Swamp"),
]

starting_asteroid_images = {
    "Terra": "[[File:Terra Asteroid.png|center|40x40px|link=Terra]]",
    "Oceania": "[[File:Oceania Asteroid (Spaced Out).png|center|42x42px|link=Oceania]]",
    "Squelchy": "[[File:Squelchy Asteroid.png|center|48x48px|link=Squelchy Asteroid]]",
    "Rime": "[[File:Rime Asteroid (Spaced Out).png|center|40x40px|link=Rime]]",
    "Verdante": "[[File:Verdante Asteroid (Spaced Out).png|center|43x43px|link=Verdante]]",
    "Arboria": "[[File:Arboria Asteroid (Spaced Out).png|center|48x48px|link=Arboria]]",
    "Volcanea": "[[File:Volcanea Asteroid (Spaced Out).png|center|40x40px|link=Volcanea]]",
    "The Badlands": "[[File:The Badlands Asteroid (Spaced Out).png|center|40x40px|link=The Badlands]]",
    "Aridio": "[[File:Aridio Asteroid (Spaced Out).png|center|40x40px|link=Aridio]]",
    "Oasisse": "[[File:Oassise Asteroid (Spaced Out).png|center|47x47px|link=Oasisse]]",
    "Terrania": "[[File:Sandstone Asteroid.png|link=Terrania Asteroid|center|41x41px]]",
    "Folia": "[[File:Forest Moonlet.png|link=Folia Asteroid|center|40x40px]]",
    "Quagmiris": "[[File:Swampy Asteroid.png|link=Quagmiris Asteroid|center|41x41px]]",
    "Metallic Swampy": "[[File:metallic_swampy_asteroid.png|link=Metallic Swampy Asteroid|center|40x40px]]",
    "The Desolands": "[[File:the_desolands_asteroid.png|link=The Desolands Asteroid|center|48x48px]]",
    "Frozen Forest": "[[file:frozen_forest_asteroid.png|link=Frozen Forest Asteroid|center|43x43px]]",
    "Flipped": "[[file:flipped_asteroid.png|link=Flipped Asteroid|center|40x40px]]",
    "Radioactive Ocean": "[[file:radioactive_ocean_asteroid.png|link=Radioactive Ocean Asteroid|center|42x42px]]",
    "Skewed": "[[File:Skewed Asteroid.png|center|47x47px|link=Skewed Asteroid]]",
}


asteroid_biomes = {
    "Terra":                ["Jungle", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Sandstone", "Space", "Tundra", "Wasteland"],
    "Radioactive Swamp":    ["Forest", "Marsh", "Radioactive", "Rust", "Space", "Swampy", "Tundra"],
    "Oceania":              ["Jungle", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Sandstone", "Space", "Swampy", "Tundra"],
    "Glowood Wasteland":    ["Forest", "Radioactive", "Rust", "Space", "Tundra", "Wasteland"],
    "Squelchy":             ["Jungle", "Magma", "Marsh", "Oily", "Radioactive", "Sandstone", "Space", "Swampy", "Tundra", "Wasteland"],
    "Radioactive Forest":   ["Forest", "Ocean", "Radioactive", "Rust", "Space", "Tundra"],
    "Rime":                 ["Jungle", "Forest", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Rust", "Sandstone", "Space", "Tundra"],
    "Stinko Swamp":         ["Barren", "Jungle", "Magma", "Marsh", "Space", "Swampy", "Tundra", "Wasteland"],
    "Verdante":             ["Jungle", "Forest", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Rust", "Space", "Swampy"],
    "Radioactive Terra":    ["Jungle", "Radioactive", "Sandstone", "Space", "Tundra", "Wasteland"],
    "Arboria":              ["Jungle", "Forest", "Magma", "Ocean", "Oily", "Radioactive", "Rust", "Space", "Swampy", "Tundra"],
    "Volcanea":             ["Jungle", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Sandstone", "Space", "Tundra", "Wasteland"],
    "The Badlands":         ["Barren", "Jungle", "Magma", "Oily", "Radioactive", "Rust", "Sandstone", "Space", "Tundra", "Wasteland"],
    "Aridio":               ["Jungle", "Forest", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Rust", "Space", "Wasteland"],
    "Radioactive Terrabog": ["Barren", "Radioactive", "Sandstone", "Space", "Swampy", "Tundra"],
    "Oasisse":              ["Jungle", "Forest", "Magma", "Marsh", "Ocean", "Oily", "Radioactive", "Sandstone", "Space", "Wasteland"],
    "Terrania":             ["Barren", "Jungle", "Magma", "Marsh", "Sandstone", "Space", "Tundra", "Wasteland"],
    "Irradiated Forest":    ["Barren", "Forest", "Metallic", "Ocean", "Radioactive", "Space", "Tundra"],
    "Oily Swamp":           ["Barren", "Oily", "Rust", "Space", "Swampy", "Tundra"],
    "Folia":                ["Barren", "Jungle", "Forest", "Magma", "Rust", "Space", "Tundra", "Wasteland"],
    "Irradiated Swamp":     ["Marsh", "Metallic", "Radioactive", "Space", "Swampy", "Tundra"],
    "Rusty Oil":            ["Magma", "Ocean", "Oily", "Rust", "Sandstone", "Space"],
    "Quagmiris":            ["Barren", "Jungle", "Magma", "Space", "Swampy", "Tundra", "Wasteland"],
    "Irradiated Marsh":     ["Barren", "Forest", "Marsh", "Metallic", "Radioactive", "Space", "Tundra"],
    "Metallic Swampy":      ["Magma", "Marsh", "Metallic", "Space", "Swampy"],
    "The Desolands":        ["Barren", "Jungle", "Oily", "Sandstone", "Space"],
    "Frozen Forest":        ["Jungle", "Forest", "Magma", "Rust", "Space"],
    "Flipped":              ["Magma", "Sandstone", "Space", "Tundra", "Wasteland"],
    "Radioactive Ocean":    ["Forest", "Magma", "Ocean", "Radioactive", "Space"],
    "Skewed":               ["Sandstone", "Jungle", "Marsh", "Jungle", "Tundra", "Ocean", "Magma", "Oily", "Space"],
    "Tundra":               ["Space", "Tundra"],
    "Marshy":               ["Jungle", "Magma", "Marsh", "Space"],
    "Moo":                  ["Moo", "Space"],
    "Water":                ["Aquatic", "Barren", "Space"],
    "Superconductive":      ["Magma", "Niobium", "Space"],
    "Regolith":             ["Barren", "Regolith", "Space"],
}

biome_resources = {
    "Aquatic": [
        # As of version 568201, the in-game wiki gives this pathetic list of resources:
        #  "Graphite", "Igneous Rock", "Oxygen", "Carbon Dioxide", "Water",
        # But really we get way more than that:
        "Carbon Dioxide", "Coal", "Dirt", "Fossil", "Granite", "Graphite", "Igneous Rock", "Lime", "Mafic Rock", "Oxygen",
        "Oxylite", "Phosphorite", "Sand", "Sandstone", "Sedimentary Rock", "Water",
    ],
    "Barren": [
        "Aluminum Ore", "Dirt", "Oxygen", "Carbon Dioxide", "Obsidian", "Igneous Rock", "Iron", "Iron Ore", "Coal", "Granite",
        # As of version 568201, the in-game wiki gives these additional items, but this is surely a bug:
        #  "Oxyfern", "Arbor Tree", "Mealwood", "Hexalent", "Mirth Leaf", "Pip",
    ],
    "Forest": [
        "Phosphorite", "Oxylite", "Aluminum Ore", "Water", "Carbon Dioxide", "Dirt", "Oxygen", "Igneous Rock",
        "Arbor Tree", "Mirth Leaf", "Oxyfern", "Mealwood", "Hexalent", "Shine Bug", "Pip",
        # As of version 568201, the in-game wiki gives these additional items, but it seems like a bug:
        #  "Snow", "Ice", "Polluted Water",
    ],
    "Jungle": [
        "Algae", "Sand", "Iron Ore", "Hydrogen", "Bleach Stone", "Sandstone", "Coal", "Chlorine", "Phosphorite", "Igneous Rock",
        "Balm Lily", "Pincha Pepperplant", "Mirth Leaf", "Morb", "Drecko",
    ],
    "Magma": [
        "Neutronium", "Obsidian", "Magma",
        # As of version 568201, the in-game wiki gives this additional item, but it's redundant with Magma:
        #  "Igneous Rock",
    ],
    "Marsh": [
        "Igneous Rock", "Sand", "Sandstone", "Gold Amalgam", "Polluted Oxygen", "Algae", "Polluted Water", "Clay",
        "Carbon Dioxide", "Sedimentary Rock", "Slime", "Dusk Cap", "Thimble Reed", "Buddy Bud", "Puft", "Pacu",
        # As of version 568201, the in-game wiki gives this additional item, but it appears to be a bug:
        #  "Water",
    ],
    "Metallic": [
        # As of version 568201, the in-game wiki gives this completely wrong list of resources:
        #  "Aluminum Ore", "Oxylite", "Cobalt Ore", "Gold Amalgam", "Dirt", "Igneous Rock", "Coal",
        # Experimentation with a Quagmiris start and exploring the Irradiated Marsh Astroid shows it's more like this:
        "Aluminum Ore", "Carbon Dioxide", "Coal", "Dirt", "Gold Amalgam", "Igneous Rock", "Oxygen", "Oxylite", "Water",
        "Arbor Tree", "Hexalent", "Mealwood", "Oxyfern", "Pip", "Shine Bug",
    ],
    "Moo": [
        "Carbon Dioxide", "Chlorine", "Bleach Stone", "Liquid Chlorine", "Granite", "Natural Gas", "Igneous Rock",
        "Gas Grass", "Gassy Moo",
    ],
    "Niobium": ["Obsidian", "Niobium"],
    "Ocean": [
        "Granite", "Hydrogen", "Fossil", "Bleach Stone", "Salt Water", "Sand", "Sedimentary Rock", "Salt", "Carbon Dioxide",
        "Waterweed", "Pincha Pepperplant", "Pacu", "Pokeshell",
        # As of version 568201, the in-game wiki gives these additional items, but it appears to be a bug:
        #  "Brine", "Brine Ice",
    ],
    "Oily": [
        "Fossil", "Diamond", "Lead", "Iron Ore", "Crude Oil", "Granite", "Carbon Dioxide", "Igneous Rock",
        "Jumping Joya", "Sporechid", "Slickster",
        # As of version 568201, the in-game wiki gives this additional item, but it's not clear why.
        # Perhaps placing high-mass solid crude oil is how over-pressurized oil pockets are implemented?
        #  "Solid Crude Oil",
    ],
    "Radioactive": [
        "Bleach Stone", "Rust", "Dirt", "Liquid Chlorine", "Snow", "Solid Chlorine", "Solid Carbon Dioxide", "Ice",
        "Carbon Dioxide", "Sulfur", "Wolframite", "Chlorine", "Uranium Ore", "Wheezewort", "Beeta", "Shine Bug",
        # As of version 568201, the in-game wiki is missing these additional items:
        "Liquid Carbon Dioxide",
        # Note the in-game wiki lists Beeta Hive, but here we use Beeta because it looks nicer.
    ],
    "Regolith": ["Ice", "Oxygen", "Iron Ore", "Rust", "Crushed Ice", "Regolith", "Mafic Rock", "Wheezewort", "Shove Vole"],
    "Rust": [
        "Iron Ore", "Ethanol", "Salt", "Chlorine", "Carbon Dioxide", "Bleach Stone", "Obsidian", "Mafic Rock", "Rust",
        "Nosh Sprout", "Dasha Saltvine", "Drecko", "Squeaky Puft",
        # As of version 568201, the in-game wiki gives these additional items, but it appears to be a bug:
        #  "Snow", "Brine Ice", "Salt Water", "Sour Gas", "Sulfur",
    ],
    "Sandstone": [
        "Oxylite", "Phosphorite", "Fertilizer", "Dirt", "Algae", "Coal", "Sand", "Water", "Carbon Dioxide", "Oxygen",
        "Copper Ore", "Sandstone", "Bristle Blossom", "Bluff Briar", "Mealwood", "Buried Muckroot", "Shine Bug", "Hatch",
        # As of version 568201, the in-game wiki gives these additional items, but it appears to be a bug:
        #  "Snow", "Ice",
    ],
    "Space": ["Polluted Ice", "Ice", "Dirt", "Granite", "Regolith", "Mafic Rock", "Copper Ore", "Igneous Rock", "Shove Vole"],
    "Swampy": [
        "Phosphorite", "Fertilizer", "Sand", "Fossil", "Carbon Dioxide", "Oxylite", "Polluted Dirt", "Oxygen", "Water", "Dirt",
        "Mud", "Polluted Mud", "Polluted Water", "Sedimentary Rock", "Cobalt Ore", "Polluted Oxygen", "Mellow Mallow",
        "Bog Bucket", "Swamp Chard", "Pacu", "Plug Slug",
    ],
    "Tundra": [
        "Liquid Carbon Dioxide", "Wolframite", "Liquid Oxygen", "Solid Carbon Dioxide", "Salt Water", "Igneous Rock",
        "Rust", "Salt", "Sand", "Brine Ice", "Sandstone", "Carbon Dioxide", "Granite", "Oxygen", "Snow", "Polluted Ice", "Ice",
        "Sleet Wheat", "Wheezewort",
    ],
    "Wasteland": [
        "Sulfur", "Oxylite", "Sucrose", "Copper Ore", "Mafic Rock", "Oxygen", "Igneous Rock", "Sandstone", "Sand",
        "Bliss Burst", "Spindly Grubfruit Plant", "Sweetle",
    ],
}

category_names = ["Metal", "Rock", "Other Solids", "Liquid", "Gases", "Plants and Critters"]
resource_categories = {
    "Algae": "Other Solids",
    "Aluminum Ore": "Metal",
    "Arbor Tree": "Plants and Critters",
    "Balm Lily": "Plants and Critters",
    "Beeta": "Plants and Critters",
    "Bleach Stone": "Other Solids",
    "Bliss Burst": "Plants and Critters",
    "Bluff Briar": "Plants and Critters",
    "Bog Bucket": "Plants and Critters",
    "Brine Ice": "Other Solids",
    #"Brine": "Liquid",
    "Bristle Blossom": "Plants and Critters",
    "Buddy Bud": "Plants and Critters",
    "Buried Muckroot": "Plants and Critters",
    "Carbon Dioxide": "Gases",
    "Chlorine": "Gases",
    "Clay": "Other Solids",
    "Coal": "Other Solids",
    "Cobalt Ore": "Metal",
    "Copper Ore": "Metal",
    "Crude Oil": "Liquid",
    "Crushed Ice": "Other Solids",
    "Dasha Saltvine": "Plants and Critters",
    "Diamond": "Other Solids",
    "Dirt": "Other Solids",
    "Drecko": "Plants and Critters",
    "Dusk Cap": "Plants and Critters",
    "Ethanol": "Liquid",
    "Fertilizer": "Other Solids",
    "Fossil": "Other Solids",
    "Gas Grass": "Plants and Critters",
    "Gassy Moo": "Plants and Critters",
    "Gold Amalgam": "Metal",
    "Granite": "Rock",
    "Graphite": "Other Solids",
    "Hatch": "Plants and Critters",
    "Hexalent": "Plants and Critters",
    "Hydrogen": "Gases",
    "Ice": "Other Solids",
    "Igneous Rock": "Rock",
    "Iron": "Metal",
    "Iron Ore": "Metal",
    "Jumping Joya": "Plants and Critters",
    "Lead": "Metal",
    "Lime": "Other Solids",
    "Liquid Carbon Dioxide": "Liquid",
    "Liquid Chlorine": "Liquid",
    "Liquid Oxygen": "Liquid",
    "Mafic Rock": "Rock",
    "Magma": "Liquid",
    "Mealwood": "Plants and Critters",
    "Mellow Mallow": "Plants and Critters",
    "Mirth Leaf": "Plants and Critters",
    "Morb": "Plants and Critters",
    "Mud": "Other Solids",
    "Natural Gas": "Gases",
    "Neutronium": "Other Solids",
    "Niobium": "Metal",
    "Nosh Sprout": "Plants and Critters",
    "Obsidian": "Rock",
    "Oxyfern": "Plants and Critters",
    "Oxygen": "Gases",
    "Oxylite": "Other Solids",
    "Pacu": "Plants and Critters",
    "Phosphorite": "Other Solids",
    "Pincha Pepperplant": "Plants and Critters",
    "Pip": "Plants and Critters",
    "Plug Slug": "Plants and Critters",
    "Pokeshell": "Plants and Critters",
    "Polluted Dirt": "Other Solids",
    "Polluted Ice": "Other Solids",
    "Polluted Mud": "Other Solids",
    "Polluted Oxygen": "Gases",
    "Polluted Water": "Liquid",
    "Puft": "Plants and Critters",
    "Regolith": "Other Solids",
    "Rust": "Other Solids",
    "Salt": "Other Solids",
    "Salt Water": "Liquid",
    "Sand": "Other Solids",
    "Sandstone": "Rock",
    "Sedimentary Rock": "Rock",
    "Shine Bug": "Plants and Critters",
    "Shove Vole": "Plants and Critters",
    "Sleet Wheat": "Plants and Critters",
    "Slickster": "Plants and Critters",
    "Slime": "Other Solids",
    "Snow": "Other Solids",
    "Solid Carbon Dioxide": "Other Solids",
    "Solid Chlorine": "Other Solids",
    #"Solid Crude Oil": "Other Solids",
    #"Sour Gas": "Gases",
    "Spindly Grubfruit Plant": "Plants and Critters",
    "Sporechid": "Plants and Critters",
    "Squeaky Puft": "Plants and Critters",
    "Sucrose": "Other Solids",
    "Sulfur": "Other Solids",
    "Swamp Chard": "Plants and Critters",
    "Sweetle": "Plants and Critters",
    "Thimble Reed": "Plants and Critters",
    "Uranium Ore": "Metal",
    "Water": "Liquid",
    "Waterweed": "Plants and Critters",
    "Wheezewort": "Plants and Critters",
    "Wolframite": "Metal",
}

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("command", choices=[
        "biome-reachability",
        "biome-resources",
        "resource-reachability",
        "interesting-things",
    ])
    parser.add_argument("--all", action="store_true")
    args = parser.parse_args()

    if args.command == "biome-reachability":
        do_biome_reachability()
    elif args.command == "biome-resources":
        do_biome_resources()
    elif args.command == "resource-reachability":
        do_resource_reachability(not args.all)
    elif args.command == "interesting-things":
        do_interesting_things()
    else: assert False

def do_biome_reachability():
    for starmap in starmaps:
        print("{}:".format(starmap.starting_asteroid))
        seen_biomes = set()
        def is_new(biome):
            if biome in seen_biomes: return False
            seen_biomes.add(biome)
            return True

        print("  Starting Biomes:")
        for biome in asteroid_biomes[starmap.starting_asteroid]:
            if is_new(biome):
                print("  * {}".format(biome))

        print("  Teleport Biomes:")
        for biome in asteroid_biomes[starmap.teleport]:
            if is_new(biome):
                print("  * {}".format(biome))

        short_flight_biomes = set(itertools.chain(*(asteroid_biomes[asteroid] for asteroid in starmap.short_flight)))
        if short_flight_biomes - seen_biomes:
            print("  Short Flight Biomes:")
            for biome in sorted(short_flight_biomes):
                if is_new(biome):
                    print("  * {}".format(biome))

        print("  Long Flight Biomes:")
        for biome in sorted(set(itertools.chain(*(asteroid_biomes[asteroid] for asteroid in starmap.long_flight)))):
            if is_new(biome):
                print("  * {}".format(biome))

        missing_biomes = set(biome_resources.keys()) - seen_biomes
        if missing_biomes:
            print("  Missing Biomes:")
            for biome in sorted(missing_biomes):
                print("  * {}".format(biome))

        print("")

def do_resource_reachability(just_interesting):
    rows = []
    for starmap, tiers in compute_rsource_reachability():
        row = [
            "!%(image)s [[%(name)s Asteroid|%(name)s]]<br>''(%(category)s)''" % {
                "image": starting_asteroid_images[starmap.starting_asteroid],
                "name": starmap.starting_asteroid,
                "category": starmap.category,
            },
        ]
        for tier_name, resources in tiers:
            if just_interesting:
                resources = [resource for resource in resources if resource in interesting_resources]
            resources.sort(key=lambda resource: (category_names.index(resource_categories[resource]), resource))
            if not resources:
                row.append("|None")
            else:
                row.append("|" + "".join(
                    "{{Pic|%(format)s|%(name)s}}" % {
                        "name": resource,
                        "format": "x48" if resource_categories[resource] == "Plants and Critters" else "48",
                    }
                    for resource in resources
                ))
        rows.append(row)

    vertically_join_cells(rows)

    print("""\
=== Resource Reachability ===
{| class="wikitable" style="text-align: center;"
!Scenario
!Starting Asteroid
!Reachable via Teleporter
!Reachable via Short Rocket Trip
!Reachable via Long Rocket Trip
!Unreachable
|-
""" + "".join("\n".join(row) + "\n|-\n" for row in rows) + """|}
''This table was generated from [https://github.com/thejoshwolfe/oni-data this script].''
""", end="")

def compute_rsource_reachability():
    results = []
    for starmap in starmaps:
        tiers = []
        seen_resources = set()
        for tier_name, tier_asteroids in get_reachability_tiers(starmap):
            resources = []
            for asteroid in tier_asteroids:
                for biome in asteroid_biomes[asteroid]:
                    for resource in biome_resources[biome]:
                        if resource in seen_resources: continue
                        seen_resources.add(resource)
                        resources.append(resource)
            tiers.append((tier_name, resources))

        missing_resources = list(sorted(set(resource_categories.keys()) - seen_resources))
        tiers.append(("Missing", missing_resources))

        results.append((starmap, tiers))
    return results

def get_reachability_tiers(starmap):
    return [
        ("Starting", [starmap.starting_asteroid]),
        ("Teleport", [starmap.teleport]),
        ("Short Flight", starmap.short_flight),
        ("Long Flight", starmap.long_flight),
    ]

def do_interesting_things():
    resource_to_tier_to_starmap_names = collections.defaultdict(lambda: ([], [], [], [], []))
    for starmap, tiers in compute_rsource_reachability():
        for tier_i, (tier_name, resources) in enumerate(tiers):
            for resource in resources:
                resource_to_tier_to_starmap_names[resource][tier_i].append(starmap.starting_asteroid)
    variability_to_resource = collections.defaultdict(list)
    for resource, tier_to_starmap_names in resource_to_tier_to_starmap_names.items():
        variability_to_resource[sum(int(bool(starmap_names)) for starmap_names in tier_to_starmap_names)].append(resource)
    # Then explore the data i guess.
    import pdb; pdb.set_trace()
    print(resource_to_tier_to_starmap_names["Sandstone"])

interesting_resources = {
    "Gold", "Gold Amalgam", # For Oxylite, Super Coolant, pumping hot oil, etc.
    "Fossil", "Lime", "Iron Ore", "Rust", # For Steel
    "Graphite", "Niobium", "Gas Grass", "Gassy Moo", # Space resources
    "Crude Oil", # For Plastic
    "Drecko", # For Plastic and Reed Fiber
    "Thimble Reed", # For Reed Fiber
    "Diamond", # For Drill Cone, Monument
    "Arbor Tree", "Ethanol", # For power
    "Clay", # For Ceramic
    "Coal", # For power, Steel, Ceramic, etc.
    "Wheezewort", "Uranium Ore", # For Applied Sciences Research
    "Algae", "Oxyfern", "Polluted Dirt", "Polluted Mud", # For Oxygen
    # Food crops:
    "Bog Bucket", "Bristle Blossom", "Dusk Cap", "Mealwood", "Nosh Sprout",
    "Sleet Wheat", "Spindly Grubfruit Plant", "Waterweed",
    # Food critters:
    "Hatch", "Pip", "Pokeshell", "Pacu", "Slickster", "Shove Vole",
    "Plug Slug", "Sweetle",
}

def do_biome_resources():
    rows = []
    for biome, resources in biome_resources.items():
        row = [
            "!{{Pic|96|%(name)s Biome}}<br>[[%(name)s Biome|%(name)s]]" % {"name": biome},
        ]
        categorized = partition(resources, resource_categories.__getitem__)
        for category in category_names:
            try:
                items = categorized[category]
            except KeyError:
                row.append("|None")
            else:
                row.append("|" + "".join(
                    "{{Pic|%(format)s|%(name)s}}" % {
                        "name": item,
                        "format": "x48" if category == "Plants and Critters" else "48",
                    }
                    for item in sorted(items)
                ))
                del categorized[category] # for assertion
        assert len(categorized) == 0, "Unrecognized category: " + next(iter(categorized.keys()))
        row.append("|-")
        rows.append("\n".join(row))

    print("""\
== Biomes Contents ==
{| class="wikitable"
|-
! Biome !! Metal !! Rock !! Other Solids !! Liquid !! Gases !! Plants and Critters
|-
""" + "\n".join(rows) + """
|}
''This table was generated from [https://github.com/thejoshwolfe/oni-data this script].''
""", end="")

def vertically_join_cells(rows):
    for column_i in reversed(range(1, len(rows[0]))):
        run_start = 0
        def flush_run(row_i):
            run_length = row_i - run_start
            if run_length > 1:
                rows[run_start][column_i] = "| rowspan=\"{}\" ".format(run_length) + rows[run_start][column_i]
        for row_i, row in list(enumerate(rows))[1:]:
            if row[column_i] == rows[run_start][column_i]:
                # The run continues
                del row[column_i]
            else:
                # The run is done.
                flush_run(row_i)
                run_start = row_i
        flush_run(row_i + 1)

def partition(items, categorize_fn):
    result = collections.defaultdict(list)
    for item in items:
        result[categorize_fn(item)].append(item)
    return dict(result)

if __name__ == "__main__":
    main()
