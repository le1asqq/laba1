digit_words = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять', 6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
def num2words(num):
    if num == 0:
        return 'ноль'
    result = ''
    while num > 0:
        digit = num % 10
        result = digit_words[digit] + ' ' + result
        num = num // 10
    result = result.strip()
    return result

max_num = 0


with open('input.txt', 'r') as f:
    while True:
        block = f.read(1024)
        if not block:
            break
        words = block.split()
        for word in words:
            if word.isdigit():
                num = int(word)
                if num % 2 == 0:
                    lexeme = num2words(num)
                    if num > max_num:
                        max_num = num

if max_num > 0:
    print('Максимальное число: ' + num2words(max_num))
