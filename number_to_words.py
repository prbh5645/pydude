while "true":
    number = input("Enter a 4 digit number: ")
    num = list(number)
    num_len = len(num)
    num_word = ""

    numbers_list = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    two_digit_numbers = ["eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens_multiple = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety" ]
    three_digit_numbers = ["", "ten", "hundred", "thousand"]

    pos = 0
    for i in num:
        if i != '0':
            if num_len == 1:
                num_word = num_word + numbers_list[int(i)]
            elif (num_len - pos) == 2 and i == "1":
                num_word = num_word + two_digit_numbers[int(num[pos+1])-1]
                break
            elif (num_len - pos) == 2:
                num_word = num_word + tens_multiple[int(i)-1] + " "
            else:
                num_word = num_word + numbers_list[int(i)] + " " + three_digit_numbers[num_len-pos-1] + " "
        pos = pos+1
    print("{0}: {1}".format(number, num_word))
done