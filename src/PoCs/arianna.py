#Primo esercizio - Stampare a console la frase 'Hello World!'
print('Hello World!')
print('%')
print('13')

#Secondo esercizio - Concatenazione di stringhe
pippo : str = "Hello World 2!"
print(pippo)
pippo += " Ciao Mondo!"
print(pippo)

#Terzo esercizio - Tipi di variabili
num_int: int = -13
num_int_pos: int = 7

risultato = num_int + num_int_pos
print(risultato)

#Variabile FLOAT
risultato_2 = num_int_pos / num_int
print(risultato_2)

#Variabile bool solo due valori: True(1), False(0)
var_bool: bool = num_int_pos == 7
print(var_bool)
var_bool: bool = num_int_pos != 7
print(var_bool)
