#Целые четные числа. Максимальное число выводить прописью.
import re

digit_words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}

def num2words(num):
    if num == 0:
        return 'ноль'
    result = ''
    while num != 0:
        digit = abs(num % 10)
        result = digit_words[digit] + ' ' + result
        num //= 10
    result = result.strip()
    return result

max_num = None

with open('input.txt', 'r') as f:
    data = f.read()
    nums = re.findall(r'-?\b\d+\b', data)
    for num in nums:
        num = int(num)
        if num % 2 == 0:
            lexeme = num2words(num)
            if max_num is None or num > max_num:
                max_num = num

if max_num is not None:
    print('Максимальное число: ' + num2words(max_num))
