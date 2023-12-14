with open('input.txt', 'r') as file:
    lines = file.readlines()
    
    possible_games = 0

    for line in lines:
        game_id = int(line.split(":")[0].split(" ")[1])
        rounds = line.split(": ")[1].split("; ")

        possible = True
        for round in rounds:
            draws = round.split(", ")

            for draw in draws:
                n = int(draw.split(" ")[0])
                colour = draw.split(" ")[1]

                if "red" in colour and n > 12:
                    possible = False
                    break

                if "green" in colour and n > 13:
                    possible = False
                    break

                if "blue" in colour and n > 14:
                    possible = False
                    break

            if possible == False:
                break

        if possible == True:
            possible_games += game_id

    print(possible_games)