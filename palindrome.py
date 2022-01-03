
"""A = [1, 2, '3', True]
A*2;
print(A)"""
#palindrome
"""number=int(input("Enter any number :"))
i=0
for i in range(len(number)):
    if number[i]!=number[-1-i]:
        print('It is not a palindrome')
        break
    else:
        print('It is a palindrome')
        break"""
"""my_dict = {'name': 'Vineel', 'age': 19, 'magic_power': False}
my_dict['name']
len(my_dict)
list(my_dict.keys())
list(my_dict.values())
list(my_dict.items())
my_dict['favourite_snack'] = 'Grapes'
my_dict.get('age')
my_dict.get('ages', 0 )

#Remove key
del my_dict['name']
my_dict.pop('name', None)"""
# Palindrome check
word = '9686'
p = bool(word.find(word[::-1]) + 1)
print(p) # True

