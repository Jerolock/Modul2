def print_params(a=1, b='выхухоль', c=True):
    print(a, b, c)


print_params()
print_params(2, 'бибки', False)
print_params(b=25)
print_params(c=[2, 1, 3])


values_list = [2, True, 'турка']
values_dict = {'a': 3, 'b': 'паркет', 'c': False }
print_params(**values_dict)
print_params(*values_list)
values_list_2 = [2, 'валенок']
print_params(*values_list_2, 42)