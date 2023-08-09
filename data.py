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

all_biomes = set(itertools.chain(*asteroid_biomes.values()))

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