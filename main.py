name = 'Anna'
age = 28
is_human = False

text3 = 'Hello {} your age {} is human {}'.format(name, age, is_human)
text4 = f'Hello {name} your age {age * 2} is human {is_human}'

text4 = '{}{}{}!'.format(name, age, is_human)

# print(f'{name:*<10}')
# print(f'{2 * 2=  }')
# print(f'{name!r}')
# print(f'{"привет"!a}')
# print(f'{32345678.14159:,.2f}')


text = 'hello world python world'
# print(text.replace(' ', '', 1))
# print(text.find('world'))
# print(text.rfind('world'))
# print(text.index('world'))
# print(text.rindex('world'))
# print(text.count('hello', 0, 25))
# print(text.partition('world'))
# print(text.rpartition('world'))
print('fo'.isidentifier())
print('hello world'.casefold())
print('D'.lower())
print('t'.upper())
print('f'.title())
print('ldflflfl'.capitalize())
print('FFaaFFaa'.swapcase())
print('ß'.casefold())
