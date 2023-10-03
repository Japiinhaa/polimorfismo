from classes import *

veiculo = Veiculo()
carro = Carro()
moto = Moto()

for x in (veiculo, carro, moto):
    x.mover()