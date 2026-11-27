from time import sleep
print('-' * 20)
print('ANÁLISE DE TEXTOS')
print('-' * 20)
frase = str(input('Digite a frase/palavra a ser analizada: ')).lower().strip()
print('ANALIZANDO...')
sleep(3)
div = frase.count(' ') + 1
a = frase.count('a')
e = frase.count('e')
i = frase.count('i')
o = frase.count('o')
u = frase.count('u')
vog = a + e + i + o + u
if len(frase.replace(' ', '')) >= 2:
    print('Sua frase tem {} caracteres'.format(len(frase.replace(' ', ''))))
else:
    print('Sua frase tem {} caractér'.format(len(frase.replace(' ', ''))))
if div >= 2:
    print('Sua frase tem {} palavras'.format(div))
else:
    print('Sua frase tem {} palavra'.format(div))
if vog >= 2:
    print('Sua frase tem {} vogais'.format(vog))
else:
    print('Sua frase tem {} vogal'.format(vog))
print(' ')
print('Obrigado pela preferência em nossos serviços')
