spam = ['apples', True, 'tofu', 42]

def func(par):
    spam_str = ''
    for i in range(len(par)):
        if i == len(par)-1:
            spam_str += 'and ' + str(par[i])
        else:
            spam_str += str(par[i]) + ', '
    return spam_str


func(spam)
