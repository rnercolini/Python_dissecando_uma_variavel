n = input('Digite algo: ')
cor = {'magenta' : '\033[35m',
       'vermelho' : '\033[31m',
       'limpa' : '\033[m'}
print('{0}{2}{1} é alfanumérico?{3}'.format(cor['magenta'], cor['limpa'],n, cor['vermelho']), (n.isalnum()))
print('{0}{2}{1} é letra?{3}'.format(cor['magenta'], cor['limpa'], n, cor['vermelho']), (n.isalpha()))
print('{0}{2}{1} está em forma maiúscula?{3}'.format(cor['magenta'], cor['limpa'], n, cor['vermelho']), (n.isupper()))
print('{0}{2}{1} é um número?{3}'.format(cor['magenta'], cor['limpa'], n, cor['vermelho']), (n.isnumeric()))
print('{0}{2}{1} é um número decimal?{3}'.format(cor['magenta'], cor['limpa'], n, cor['vermelho']), (n.isdecimal()))


