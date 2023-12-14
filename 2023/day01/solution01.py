with open('input.txt', 'r') as file:
    lines = file.readlines()

    nums = []

    for line in lines:
        length = len(line)

        first_num = ""
        last_num = "" 

        for i in range(length):
            if first_num == "" and line[i].isdigit():
                first_num = line[i]

            if last_num == "" and line[length-i-1].isdigit():
                last_num = line[length - i - 1]

            if first_num != "" and last_num != "":
                break

        nums.append(first_num + last_num)

    sum_nums = 0

    for n in nums:
        sum_nums += int(n)

    print(sum_nums)