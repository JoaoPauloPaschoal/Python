import time

_imc = (0)
_altura = float(input('Qual sua altura em metros? (ex.: 1.70): '))
_peso = float(input('Qual seu peso? (Kg): '))
_imc = _peso / (_altura * _altura)
print('Calculando....')
time.sleep(0.5)
print('O seu IMC é: {:.2f}'.format(_imc))
time.sleep(0.5)
if _imc < 18.50:
    print('Abaixo do peso')
elif 18.50 <= _imc < 25 :
    print('Peso normal')
elif 25 <= _imc < 30:
    print('Acima do peso')
elif 30 <= _imc < 35:
    print('Obesidade I Grau')
elif 35 <= _imc < 40: 
    print('Obesidade II Grau')







    
