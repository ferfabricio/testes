#!/usr/bin/python

import random

class PortaDosDesesperados:
    portas = []
    carro = 0
    escolhida = 0

    def __init__(self):
        self.portas = range(1,4)
        self.carro = random.choice(self.portas)

    def escolhaPorta(self, porta):
        self.escolhida = porta

    def isPortaValida(self, porta):
        if porta in self.portas:
            return True
        else:
            return False

    def portaGanhou(self):
        return self.escolhida == self.carro

    def abrirPorta(self):
        if self.escolhida != self.carro:
            portas = self.portas[:]
            portas.remove(self.carro)
            portas.remove(self.escolhida)
            self.portas.remove(portas[0])
            return portas[0]




a = PortaDosDesesperados()

print "Portas disponiveis"
print a.portas

escolha = int(raw_input("Escolha uma porta\n").splitlines()[0])

while not a.isPortaValida(escolha):
    print "Porta invalida"
    escolha = int(raw_input("Escolha uma porta\n").splitlines()[0])

a.escolhaPorta(escolha)
if a.portaGanhou():
    print "Ganhou"
else:
    print "Abrimos a porta %s" % a.abrirPorta()

    print "Portas disponiveis"
    print a.portas

    escolha = int(raw_input("Escolha uma porta\n").splitlines()[0])
    
    while not a.isPortaValida(escolha):
        print "Porta invalida"
        escolha = int(raw_input("Escolha uma porta\n").splitlines()[0])

    a.escolhaPorta(escolha)

    if a.portaGanhou():
        print "Ganhou"
    else:
        print "Perdeu, Si fu fu !!!"
print 10 * ' - '


acertos = 0

for i in range(100000):
    a = PortaDosDesesperados()
    portas = range(1,4)
    escolha = random.choice(portas)
    a.escolhaPorta(escolha)
    a.abrirPorta()

    a.escolhaPorta(escolha)
    if a.portaGanhou():
        acertos += 1

x = (100 * acertos) / 100000

print "Porcentagem nao mudando de porta: %s" % x


acertos = 0

for i in range(100000):
    a = PortaDosDesesperados()
    portas = range(1,4)
    escolha = random.choice(portas)
    a.escolhaPorta(escolha)
    a.abrirPorta()
    portas = a.portas[:]
    portas.remove(escolha)

    a.escolhaPorta(portas[0])
    if a.portaGanhou():
        acertos += 1

x = (100 * acertos) / 100000

print "Porcentagem mudando de porta: %s" % x
