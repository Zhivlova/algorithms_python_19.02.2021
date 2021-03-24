"""
1. Определить количество различных подстрок с использованием хеш-функции.
"""
import hashlib

string = input('Вводите маленькие латинские буквы: ')
arrey = set()

for i in range(len(string)):
    for j in range(len(string), i, -1):
        hash_str = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
        arrey.add(hash_str)

print(f'{len(arrey) - 1} различных подстрок в строке {string}')
print('*' * 50)


def combination(string):
    length = len(string)
    return [string[i:j + 1] for i in range(length) for j in range(i, length)]
print(combination(input('Вводите маленькие латинские буквы: ')))
print('*' * 50)

def subs(string, ret=['']):
    if len(string) == 0:
        return ret
    head, tail = string[0], string[1:]
    ret = ret + list(map(lambda x: x+head, ret))
    return subs(tail, ret)
print(subs(input('Вводите маленькие латинские буквы: ')))






















































def rabin_karp(s, t):
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            return i

    return -1







import pprint

def make_trie(iterable):
    root = {}
    for s in iterable:
        node = root
        for c in s:
            node = node.setdefault(c, {})
        node[''] = None
    return root

pprint.pprint(make_trie(('then', 'than', 'thing', 'those')))