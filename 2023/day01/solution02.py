digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

with open('input.txt', 'r') as file:
    lines = file.readlines()

    nums = []

    for line in lines:
        print(line.strip("\n"))
        spelled_nums_min = {line.find(digit): digit for digit in digits if line.find(digit) != -1}
        spelled_nums_max = {line.rfind(digit): digit for digit in digits if line.find(digit) != -1}
        spelled_nums = {**spelled_nums_min, **spelled_nums_max}
        min_index = min(spelled_nums.keys()) if spelled_nums else -1
        max_index = max(spelled_nums.keys()) if spelled_nums else -1

        print(spelled_nums)
        print("min:", min_index, "max:", max_index)

        length = len(line)

        first_index = -1
        last_num = -1
        first_num = ""
        last_num = "" 

        for i in range(length):
            if first_num == "" and line[i].isdigit():
                first_num = line[i]
                first_index = i

            if last_num == "" and line[length-i-1].isdigit():
                last_num = line[length - i - 1]
                last_index = length - i - 1

            if first_num != "" and last_num != "":
                break
                
        num1 = digits[spelled_nums[min_index]] if first_index > min_index and min_index != -1 or first_index == -1 else first_num
        num2 = digits[spelled_nums[max_index]] if last_index < max_index and max_index != -1 or last_index == -1 else last_num

        print("final:", num1, num2)
        nums.append(num1 + num2)
        print()

    sum_nums = 0

    for n in nums:
        sum_nums += int(n)

    print(sum_nums)