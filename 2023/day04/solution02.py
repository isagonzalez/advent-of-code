with open('input.txt', 'r') as file:
    lines = [line.strip("\n") for line in file.readlines()]

    scratchcards_won = {}
    for line in lines:
        card = int(line.split(":")[0].split("Card")[1])
        winning_nums = [n for n in line.split("|")[0].split(":")[1].split(" ") if n != ""]
        your_nums = [n for n in line.split("|")[1].split(" ") if n != ""]

        # adding the og card
        if card in scratchcards_won:
            scratchcards_won[card] += 1
        else:
            scratchcards_won[card] = 1

        count = 0
        for num in your_nums:
            if num in winning_nums: 
                count += 1

        # adding the new cards
        for i in range(count):
            copy_won = card + i + 1
            if copy_won in scratchcards_won:
                scratchcards_won[copy_won] += scratchcards_won[card]
            else:
                scratchcards_won[copy_won] = scratchcards_won[card]

    points = 0 
    for card in scratchcards_won.keys():
        if card > len(lines):
            continue
        points += scratchcards_won[card]
    print(points)