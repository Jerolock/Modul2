# -*- coding: utf-8 -*-

# блоки кода

i, k = 10, 29

if i < 0:
    print('Х меньше нуля')
    j = i ** 2 + k
else:
    print('Х больше нуля')
    j = i - k
print('Результат', j)

# ср. с С++

# if (x < 0) { printf('Меньше нуля\n'); z = x**2 + y; } else { printf('Больше нуля\n'); z = x - y; } printf(
# 'Получается\n', z)

# вложенные блоки кода

name = input('Enter your name >>>')
if name == 'Ola':
    opponent = 'Ola'
    print('Hi, Ola!')
else:
    if name == 'Sofi':
        opponent = 'Sofi'
        print('Hi, Sofi!')
    else:
        if name == 'Katy':
            opponent = 'Katy'
            print('Hi, Katy!')
        else:
            opponent = 'anonymous'
            print('Hi, anonymous!')

# оператор pass

if i < 0:
    if k > 0:
        j = -i + k
    else:
        j = -i - k
else:
    j = i + k

# соглашения о стиле кода
# PEP8 (Python Enhancement Proposal 8) - описан "правильный" стиль программирования в пайтон
# https://www.python.org/dev/peps/pep-0008/

# 4 пробела на каждый уровень отступа

if i < 0:
    if k > 0:
        pass
    else:
        print('направо!')
else:
    print('стой!')

# Максимальная длина строки

my_poem = ['Варкалось, хливкие шорьки пырялись по наве', 'И хрюкотали зелюки как мюмзики в мове',
           'О бойся Бармаглота, сын! Он так свирлеп и дик', 'А в глуше рымит исполин - Злопастный Брандашмыг!', ]

# пробелы в операторах

i = 2
k: int = i * i + 1
is_big = i >= 3000

i = my_poem[-1]
print(i)
my_list = [2, 3, 4, 5, 6, ]

# reformat кода

# noinspection PyRedeclaration
i, k = 3, 8
if k == 3:
    print(42)

if i < 0:
    if k > 0:
        print('налево!')
    else:
        print('направо!')
else:
    print(
        'стой!')

# названия переменных

count_of_my_pets = 34
if count_of_my_pets > 10:
    print('I need more space for my pets!')

my_favorite_pets_and_bird = ['cat', 'wolf', 'ostrich']
if 'lion' in my_favorite_pets_and_bird:
    print('Wow!')

MyFavoritePetsAndBirds = ['cat', 'wolf', 'ostrich']
# но такой стиль используется для названий классов


# рекомендации PEP8

# b (одиночная маленькая буква)
# B (одиночная заглавная буква)
# но лучше использовать только такие однобуквенные имена
#   i j k - для циклов
#   x y z - для координат

# никогда не используйте в названиях переменных одиночные l, I, O  !
la = 34
Is = 43
if la > Is:
    print()
Od = 9
if Od > 0:
    print()

# lowercase (слово в нижнем регистре)
# lower_case_with_underscores (слова из маленьких букв с подчеркиваниями)
# UPPERCASE (заглавные буквы)
# UPPERCASE_WITH_UNDERSCORES (слова из заглавных букв с подчеркиваниями)

# CapitalizedWords (слова с заглавными буквами, или CapWords, или CamelCase).
#   Замечание: когда вы используете аббревиатуры в таком стиле, пишите все буквы аббревиатуры заглавными —
#   HTTPServerError лучше, чем HttpServerError.

# mixedCase (отличается от CapitalizedWords тем, что первое слово начинается с маленькой буквы)
# Capitalized_Words_With_Underscores (слова с заглавными буквами и подчеркиваниями — уродливо!)


# автоматическое переименование в PyCharm и подсказки - вам не нужно набирать длинные названия переменных

ss = ['cat', 'wolf', 'ostrich']
if 'lion' in ss:
    print('Wow!')

# В каждой уважающей себя компании есть style guide (стайл-гайд) - руководство по стилю написания кода.
# Практически все они основываются на PEP8, с небольшими исключениями, принятыми в этой команде.
# Как пример стайл-гайда небольшой компании рекомендую почитать
# https://github.com/best-doctor/guides/blob/master/guides/python_styleguide.md
