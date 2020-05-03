'''Write a program which accepts a sequence of comma-separated numbers from console and
generate a list.'''

#solution 1
def generate_list(user_input):
    converted_list = user_input.split(',')
    return list(converted_list)

print(generate_list('1,2,3'))

#solution 2
def generate_list2(user_input):
    my_list = []
    for i in user_input:
        if i != ',':
            my_list.append(i)
    return my_list
            
print(generate_list2('1,2,3'))        

############ output ########
''' sdev@satyam MINGW64 ~/Desktop/Ineuron pythoon/1st assignment (master)
$ python generate\ _list.py
['1', '2', '3'] '''