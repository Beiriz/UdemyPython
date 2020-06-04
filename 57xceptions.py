#!/usr/bin/env python
# coding=utf-8

#-------------- Problema1

try:
    for i in ['a','b','c']:
        print(i**2)
except:
    print("Ocorreu um erro!")

#-------------- Problema2

x = 5
y = 0
try:
    z = x/y
except:
    print("Não pode divisão por zero!")
finally:
    print("FIM!")

#-------------- Problema3

def ask():
    while True:
        try:
            n = int(input("Informe um inteiro:"))
            print("Obrigado! O quadrado do número é:", n**2)
        except:
            print("Ocorreu um erro! Tente novamente...")
            continue
ask()