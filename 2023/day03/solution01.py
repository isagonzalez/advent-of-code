with open('input.txt', 'r') as file:
    lines = [line.strip() for line in file.readlines()]

    rows = len(lines)
    cols = len(lines[0])

    result = 0

    for i in range(rows):
        for j in range(cols):
            if lines[i][j].isalnum() == False and lines[i][j] != ".":
                # print("Found symbol:", lines[i][j], "at", i, ",", j)
                num = ""

                adjacent_nums = {} # {num: (start_index, end_index)}
                for dx in range(-1, 2): # -1, 0, 1
                    for dy in range(-1, 2): # -1, 0, 1
                        if dx == 0 and dy == 0:
                            continue

                        x = j + dx
                        y = i + dy

                        # print("\t x:", x, "y:", y)
                        if 0 <= x < cols and 0 <= y < rows:
                            char = lines[y][x]
                            # print("\t\tchar:", char)

                            left = x-1
                            right = x+1

                            num = char

                            # print("\t", adjacent_nums)
                            if char.isnumeric():
                                # find the total number
                                while 0 <= left and lines[y][left].isnumeric():
                                    num = lines[y][left] + num
                                    left -= 1

                                while right < cols and lines[y][right].isnumeric():
                                    num += lines[y][right]
                                    right += 1

                                if num not in adjacent_nums or (adjacent_nums[num][0] != left and adjacent_nums[num][1] != right):
                                    # print("\t", num)
                                    adjacent_nums[num] = (left, right)
                                    result += int(num)

    print(result)

