# Here we make all of our little test
import string
"""list_a = ['book', 'boom', 'boon', 'boor', 'boos', 'boot', 'bops', 'bore', 'nothing', 'justatest']
def possible_matches(a):
    b = list(n for n in a)
    list_b = list(i for i in list_a if len(i) == len(a))
    list_c = list()
    for j in list_b:
        k = list(letter for letter in j)
        for l in range(len(k)):
            if b[l] == '_':
                k[l] = '_'
            if k == b:
              list_c.append(j)
    return list_c              
    

print(possible_matches('_oo_'))"""
a = string.ascii_lowercase 
liste = list(letters for letters in a) 