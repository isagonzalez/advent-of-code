with open('input.txt', 'r') as file:
    lines = [line.strip("\n") for line in file.readlines()]

    points = 0

    for line in lines:
        winning_nums = [n for n in line.split("|")[0].split(":")[1].split(" ") if n != ""]

        your_nums = [n for n in line.split("|")[1].split(" ") if n != ""]

        card_points = 0
        for num in your_nums:
            if num in winning_nums:
                card_points = card_points + 1 if card_points == 0 else card_points*2

        points += card_points

    print(points)