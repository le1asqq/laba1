#Целые четные числа. Максимальное число выводить прописью.
import re

digit_words = {
    0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре',
    5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
}

def num2words(num):
    if num == 0:
        return 'ноль'
    result = ''
    while num > 0:
        digit = num % 10
        result = digit_words[digit] + ' ' + result
        num = num // 10
    return result.strip()

max_num = 0

with open('input.txt', 'r') as f:
    data = f.read()
    nums = re.findall(r'-?\d*[02468](?!\d)', data)
    for num_str in nums:
        num = int(num_str)
        if num > max_num:
            max_num = num

if max_num != 0:
    print('Максимальное число:', num2words(max_num))
