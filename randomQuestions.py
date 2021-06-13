def randomQuestion(tz_1, tz_2, tz_3, tz_4):
    sum_of_digit = 0
    for digit in tz_1 + tz_2 + tz_3 + tz_4:
        sum_of_digit += int(digit)
    q_1 = sum_of_digit % 9 + 1
    q_2 = sum_of_digit % 8 + 10
    q_3 = sum_of_digit ** 2 % 8 + 10
    q_4 = sum_of_digit % 11 + 19
    q_5 = sum_of_digit ** 2 % 11 + 19
    q_6 = sum_of_digit % 7 + 31
    print('Question 1: {0}\nQuestion 2: {1}\nQuestion 3: {2}\nQuestion 4: {3}\nQuestion 5: {4}\nQuestion 6: {5}'.format(
        q_1, q_2, q_3, q_4, q_5, q_6))


randomQuestion('345112148', '336068895', '315721969', '204795900')