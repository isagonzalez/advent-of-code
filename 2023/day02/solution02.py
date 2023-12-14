from math import inf

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    power_sum = 0

    for line in lines:
        game_id = int(line.split(":")[0].split(" ")[1])
        rounds = line.split(": ")[1].split("; ")

        possible = True

        reds = blues = greens = 1
        for round in rounds:
            draws = round.split(", ")

            for draw in draws:
                n = int(draw.split(" ")[0])
                colour = draw.split(" ")[1]

                if "red" in colour:
                    reds = max(reds, n)

                if "green" in colour:
                    greens = max(greens, n)

                if "blue" in colour:
                    blues = max(blues, n)

        power_sum += (reds * greens * blues)

    print(power_sum)