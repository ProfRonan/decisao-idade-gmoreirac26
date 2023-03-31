print ('digite um numero')
idade = int(input('> '))

impossível = False
menor = False
maior = False
velho = False
print(idade)
if idade < 0:
    print('impossível')
    impossível = True
if idade < 18 :
    print ('não precisa se alistar.')
    menor= True
if 18 < idade < 65 : # 18 < idade and idade < 65
    print('não esqueça de votar na próxima eleição.')
    maior = True
if idade > 65 :
    print ('pode descansar')
    velho = True
if not (impossível or menor or maior or velho) :
    print('eita!')