def find_source(destination, mappings):
    for mapping in mappings:
        dest_start = int(mapping[0])
        source_start = int(mapping[1])
        range_length = int(mapping[2])

        if dest_start <= destination < dest_start+range_length:
                diff = destination - dest_start
                return source_start + diff

    return destination


with open('input.txt', 'r') as file:
    lines = [line.strip("\n") for line in file.readlines()]

    seeds = [line for line in lines[0].split(":")[1].split(" ") if line != ""]
    seed_ranges = []
    
    i = 0
    while i < len(seeds):
        seed_ranges.append([int(seeds[i]), int(seeds[i+1])])
        i += 2

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

    maps["humidity_to_location"] = sorted(maps["humidity_to_location"], key=lambda x: int(x[0]))

    found_seed = False
    offset = 0
    range_offset = 0
    while found_seed == False:
        min_humidity = int(maps["humidity_to_location"][range_offset][1]) + offset
        print("testing: " + str(min_humidity) + "...")
        offset += 1

        if offset > int(maps["humidity_to_location"][range_offset][2]):
            print("testing new range:", int(maps["humidity_to_location"][range_offset]))
            offset = 0
            range_offset += 1

        # find each source corresponding to the minimum location
        temp = find_source(min_humidity, maps["temp_to_humidity"])
        light = find_source(temp, maps["light_to_temp"])
        water = find_source(light, maps["water_to_light"])
        fertiliser = find_source(water, maps["fertiliser_to_water"])
        soil = find_source(fertiliser, maps["soil_to_fertiliser"])
        seed = find_source(soil, maps["seed_to_soil"])
        
        print("\tseed:", seed)
        for range in seed_ranges:
            if range[0] <= seed < range[0]+range[1]:
                found_seed = True
                break

    print(seed)







# BRUTE FORCE : TAKES FOREVER
# def find_destination(source, mappings):
#     for mapping in mappings:
#         dest_start = int(mapping[0])
#         source_start = int(mapping[1])
#         range_length = int(mapping[2])

#         if source_start <= source < source_start+range_length:
#                 diff = source - source_start
#                 return dest_start + diff
        
#     return source


# with open('input.txt', 'r') as file:
#     lines = [line.strip("\n") for line in file.readlines()]

#     seeds = [line for line in lines[0].split(":")[1].split(" ") if line != ""]
#     seed_ranges = []
    
#     i = 0
#     while i < len(seeds):
#         seed_ranges.append([int(seeds[i]), int(seeds[i+1])])
#         i += 2

#     counter = 0
#     counter_to_map = {
#         1: "seed_to_soil",
#         2: "soil_to_fertiliser",
#         3: "fertiliser_to_water",
#         4: "water_to_light",
#         5: "light_to_temp",
#         6: "temp_to_humidity",
#         7: "humidity_to_location"
#     }

#     maps = {
#         "seed_to_soil": [],
#         "soil_to_fertiliser": [],
#         "fertiliser_to_water": [],
#         "water_to_light": [],
#         "light_to_temp": [],
#         "temp_to_humidity": [],
#         "humidity_to_location": []
#     }

#     for line in lines[1:]:
#         if line.find(":") == -1:
#             if line == "":
#                 continue

#             map_nums = line.split(" ")
#             maps[counter_to_map[counter]].append(map_nums)
#         else:
#             counter += 1

#     locations = []
#     for seed_range in seed_ranges:
#         start_seed = seed_range[0]
#         end_seed = start_seed + seed_range[1]

#         print("new seed range!")

#         for seed in range(start_seed, end_seed):
#             # convert to soil
#             soil = find_destination(int(seed), maps["seed_to_soil"])
#             fertiliser = find_destination(soil, maps["soil_to_fertiliser"])
#             water = find_destination(fertiliser, maps["fertiliser_to_water"])
#             light = find_destination(water, maps["water_to_light"])
#             temp = find_destination(light, maps["light_to_temp"])
#             humidity = find_destination(temp, maps["temp_to_humidity"])
#             location = find_destination(humidity, maps["humidity_to_location"])
#             locations.append(location)

#     print(min(locations))

