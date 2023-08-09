#!/usr/bin/env python3

import itertools

class Starmap:
    def __init__(self, starting_asteroid, *, teleport, short_flight=[]):
        self.starting_asteroid = starting_asteroid
        self.teleport = teleport
        self.short_flight = short_flight
        self.long_flight = outer_asteroids

outer_asteroids = ["Tundra", "Marshy", "Moo", "Water", "Superconductive", "Regolith"]
starmaps = [
    Starmap("Terra",             teleport="Radioactive Swamp"),
    Starmap("Oceania",           teleport="Glowood Wasteland"),
    Starmap("Squelchy",          teleport="Radioactive Forest"),
    Starmap("Rime",              teleport="Stinko Swamp"),
    Starmap("Verdante",          teleport="Radioactive Terra"),
    Starmap("Arboria",           teleport="Radioactive Terra"),
    Starmap("Volcanea",          teleport="Radioactive Swamp"),
    Starmap("The Badlands",      teleport="Radioactive Swamp"),
    Starmap("Aridio",            teleport="Radioactive Terrabog"),
    Starmap("Oasisse",           teleport="Radioactive Swamp"),
    Starmap("Terrania",          teleport="Oily Swamp",        short_flight=["Irradiated Forest"]),
    Starmap("Folia",             teleport="Rusty Oil",         short_flight=["Irradiated Swamp"]),
    Starmap("Quagmiris",         teleport="Rusty Oil",         short_flight=["Irradiated Marsh"]),
    Starmap("Metalic Swampy",    teleport="Frozen Forest",     short_flight=["The Desolands",  "Flipped",       "Radioactive Ocean"]),
    Starmap("The Desolands",     teleport="Radioactive Ocean", short_flight=["Metalic Swampy", "Frozen Forest", "Flipped"]),
    Starmap("Frozen Forest",     teleport="The Desolands",     short_flight=["Metalic Swampy", "Flipped",       "Radioactive Ocean"]),
    Starmap("Flipped",           teleport="The Desolands",     short_flight=["Metalic Swampy", "Frozen Forest", "Radioactive Ocean"]),
    Starmap("Radioactive Ocean", teleport="Flipped",           short_flight=["Metalic Swampy", "The Desolands", "Frozen Forest"]),
]


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
    "Metalic Swampy":       ["Magma", "Marsh", "Metallic", "Space", "Swampy"],
    "The Desolands":        ["Barren", "Jungle", "Oily", "Sandstone", "Space"],
    "Frozen Forest":        ["Jungle", "Forest", "Magma", "Rust", "Space"],
    "Flipped":              ["Magma", "Sandstone", "Space", "Tundra", "Wasteland"],
    "Radioactive Ocean":    ["Forest", "Magma", "Ocean", "Radioactive", "Space"],
    "Tundra":               ["Space", "Tundra"],
    "Marshy":               ["Jungle", "Magma", "Marsh", "Space"],
    "Moo":                  ["Moo", "Space"],
    "Water":                ["Aquatic", "Barren", "Space"],
    "Superconductive":      ["Magma", "Niobium", "Space"],
    "Regolith":             ["Barren", "Regolith", "Space"],
}

biome_resources = {
    "Aquatic": ["Graphite", "Igneous Rock", "Oxygen", "Carbon Dioxide", "Water"],
    "Barren": [
        "Aluminum Ore", "Dirt", "Oxygen", "Carbon Dioxide", "Obsidian", "Igneous Rock", "Iron", "Iron Ore", "Coal", "Granite",
        "Oxyfern", "Arbor Tree", "Mealwood", "Hexalent", "Mirth Leaf", "Pip",
    ],
    "Forest": [
        "Snow", "Ice", "Polluted Water", "Phosphorite", "Oxylite", "Aluminum Ore", "Water", "Carbon Dioxide", "Dirt", "Oxygen",
        "Igneous Rock", "Arbor Tree", "Mirth Leaf", "Oxyfern", "Mealwood", "Hexalent", "Shine Bug", "Pip",
    ],
    "Jungle": [
        "Algae", "Sand", "Iron Ore", "Hydrogen", "Bleach Stone", "Sandstone", "Coal", "Chlorine", "Phosphorite", "Igneous Rock",
        "Balm Lily", "Pincha Pepperplant", "Mirth Leaf", "Morb", "Drecko",
    ],
    "Magma": ["Igneous Rock", "Neutronium", "Obsidian", "Magma"],
    "Marsh": [
        "Water", "Igneous Rock", "Sand", "Sandstone", "Gold Amalgam", "Polluted Oxygen", "Algae", "Polluted Water", "Clay",
        "Carbon Dioxide", "Sedimentary Rock", "Slime", "Dusk Cap", "Thimble Reed", "Buddy Bud", "Puft", "Pacu",
    ],
    "Metalic": ["Aluminum Ore", "Oxylite", "Cobalt Ore", "Gold Amalgam", "Dirt", "Igneous Rock", "Coal"],
    "Moo": [
        "Carbon Dioxide", "Chlorine", "Bleach Stone", "Chlorine (Liquid)", "Granite", "Natural Gas", "Igneous Rock",
        "Gas Grass", "Gassy Moo",
    ],
    "Niobium": ["Obsidian", "Niobium"],
    "Ocean": [
        "Brine", "Brine Ice", "Granite", "Hydrogen", "Fossil", "Bleach Stone", "Salt Water", "Sand", "Sedimentary Rock", "Salt",
        "Carbon Dioxide", "Waterweed", "Pincha Pepperplant", "Pacu", "Pokeshell",
    ],
    "Oily": [
        "Curde Oil (Solid)", "Fossil", "Diamond", "Lead", "Iron Ore", "Crude Oil", "Granite", "Carbon Dioxide", "Igneous Rock",
        "Jumping Joya", "Sporchid", "Slickster",
    ],
    "Radioactive": [
        "Bleach Stone", "Rust", "Dirt", "Chlorine (Liquid)", "Snow", "Chlorine (Solid)", "Carbon Dioxide (Solid)", "Ice",
        "Carbon Dioxide", "Sulfur", "Wolframite", "Chlorine", "Uranium Ore", "Wheezewort", "Beeta Hive", "Shine Bug",
    ],
    "Regolith": ["Ice", "Oxygen", "Iron Ore", "Rust", "Crushed Ice", "Regolith", "Mafic Rock", "Wheezewort", "Shove Vole"],
    "Rust": [
        "Snow", "Iron Ore", "Sour Gas", "Salt Water", "Sulfur", "Brine Ice", "Ethanol", "Salt", "Chlorine", "Carbon Dioxide",
        "Bleach Stone", "Obsidian", "Mafic Rock", "Rust", "Nosh Sprout", "Dasha Saltvine", "Drecko", "Squeaky Puft",
    ],
    "Sandstone": [
        "Oxylite", "Snow", "Ice", "Phosphorite", "Fertilizer", "Dirt", "Algae", "Coal", "Sand", "Water", "Carbon Dioxide",
        "Oxygen", "Copper Ore", "Sandstone", "Bristle Blossom", "Bluff Briar", "Mealwood", "Buried Muckroot", "Shine Bug", "Hatch",
    ],
    "Space": ["Polluted Ice", "Ice", "Dirt", "Granite", "Regolith", "Mafic Rock", "Copper Ore", "Igneous Rock", "Shove Vole"],
    "Swampy": [
        "Phosphorite", "Fertilizer", "Sand", "Fossil", "Carbon Dioxide", "Oxylite", "Polluted Dirt", "Oxygen", "Water", "Dirt",
        "Mud", "Polluted Mud", "Polluted Water", "Sedimentary Rock", "Cobalt Ore", "Polluted Oxygen", "Mellow Mallow",
        "Bog Bucket", "Swamp Chard", "Pacu", "Plug Slug",
    ],
    "Tundra": [
        "Carbon Dioxide (Liquid)", "Wolframite", "Oxygen (Liquid)", "Carbon Dioxide (Solid)", "Salt Water", "Igneous Rock",
        "Rust", "Salt", "Sand", "Brine Ice", "Sandstone", "Carbon Dioxide", "Granite", "Oxygen", "Snow", "Polluted Ice", "Ice",
        "Sleet Wheat", "Wheezewort",
    ],
    "Wasteland": [
        "Sulfur", "Oxylite", "Sucrose", "Copper Ore", "Mafic Rock", "Oxygen", "Igneous Rock", "Sandstone", "Sand",
        "Bliss Burst", "Spindly Grubfruit Plant", "Sweetle",
    ],
}

all_biomes = set(biome_resources.keys())

def main():
    import argparse
    parser = argparse.ArgumentParser()
    args = parser.parse_args()

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

        missing_biomes = all_biomes - seen_biomes
        if missing_biomes:
            print("  Missing Biomes:")
            for biome in sorted(missing_biomes):
                print("  * {}".format(biome))

        print("")

if __name__ == "__main__":
    main()
