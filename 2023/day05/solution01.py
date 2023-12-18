def find_destination(source, mappings):
    for mapping in mappings:
        dest_start = int(mapping[0])
        source_start = int(mapping[1])
        range_length = int(mapping[2])

        if source_start <= source < source_start+range_length:
                diff = source - source_start
                return dest_start + diff
        
    return source


with open('input.txt', 'r') as file:
    lines = [line.strip("\n") for line in file.readlines()]

    seeds = [line for line in lines[0].split(":")[1].split(" ") if line != ""]

    counter = 0
    counter_to_map = {
        1: "seed_to_soil",
        2: "soil_to_fertiliser",
        3: "fertiliser_to_water",
        4: "water_to_light",
        5: "light_to_temp",
        6: "temp_to_humidity",
        7: "humidity_to_location"
    }

    maps = {
        "seed_to_soil": [],
        "soil_to_fertiliser": [],
        "fertiliser_to_water": [],
        "water_to_light": [],
        "light_to_temp": [],
        "temp_to_humidity": [],
        "humidity_to_location": []
    }

    for line in lines[1:]:
        if line.find(":") == -1:
            if line == "":
                continue

            map_nums = line.split(" ")
            maps[counter_to_map[counter]].append(map_nums)
        else:
            counter += 1

    locations = []
    for seed in seeds:
        # convert to soil
        soil = find_destination(int(seed), maps["seed_to_soil"])
        fertiliser = find_destination(soil, maps["soil_to_fertiliser"])
        water = find_destination(fertiliser, maps["fertiliser_to_water"])
        light = find_destination(water, maps["water_to_light"])
        temp = find_destination(light, maps["light_to_temp"])
        humidity = find_destination(temp, maps["temp_to_humidity"])
        location = find_destination(humidity, maps["humidity_to_location"])
        locations.append(location)

    print(min(locations))

