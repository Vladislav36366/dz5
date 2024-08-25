immutable_var = (1, 2, 'a', 'b')
print(immutable_var)
#immutable_var[0] = 3 изменить значение нельзя, это неизменяемый обект, чтобы можно было изменить он должен быть такой формы:
immutable_var=([1, 2], 'a', 'b')
immutable_var[0][0] = 3
print(immutable_var)
mutable_list = ([1, 2, 'a', 'b', 'Modified'])
print(mutable_list)
mutable_list[0] = 5
mutable_list[1] = 8
mutable_list[2] = 'd'
mutable_list[3] = 'c'
mutable_list[4] = 'improved'
print(mutable_list)

