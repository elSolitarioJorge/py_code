def str_reverse(s):
    return s[ : :-1]

if __name__ == '__main__':
    print(str_reverse('hello'))

def substr(s, x, y):
    return s[x:y]

if __name__ == '__main__':
    print(substr('hello world', 0, 5))