texto1 = "Ola, "
texto2 = "tudo bem?"
texto_concatenado = texto1 + texto2 # O + soma as strings.
print(texto_concatenado)

print(f"-----------------------")

resposta = "sim "
multiplica = resposta * 5 # O * repete a string.
print(multiplica)

print(f"-----------------------")

nome = "Nycolas"
frase = "O aluno %s está aprendendo composição de strings." % nome # %s é uma composição de strings.
print(frase)

print(f"-----------------------")

nome2 = "Nykinhas"
idade = 31
filhos = 0
frase2 = "O aluno %s tem %d anos de idade e tem %d filhos." % (nome2, idade, filhos) # %d é uma composição de inteiros.
print(frase2)

print(f"-----------------------")

aula = 9
print(f"Esta é a aula de número %03d" % aula)
print(f"Esta é a aula de número %3d" % aula)
print(f"Esta é a aula de número [%3d]" % aula)
print(f"Esta é a aula de número [%03d]" % aula)
print(f"Esta é a aula de número [%-3d]" % aula)

print(f"-----------------------")

valor_un = 165.78
quantidade = 5 
valor_total = valor_un * quantidade
frase = "O produto custa R$ %f. Eu comprei %d. Paguei ao todo %f" % (valor_un, quantidade, valor_total) # %f é uma composição de floats.
print(frase)

print(f"-----------------------")

valor_unitario = 165.75
print("%f" % valor_unitario) #Imprime o valor com 6 casas decimais.
print("%.f" % valor_unitario) #Imprime o valor sem casas decimais.
print("%.1f" % valor_unitario) #Imprime o valor com 1 casa decimal.
print("%.2f" % valor_unitario) #Imprime o valor com 2 casas decima
print("%.3f" % valor_unitario) #Imprime o valor com 3 casas decimais.

print(f"-----------------------")

percent = 17.5
frase1 = "A taxa de juros é de %.2f%%" % percent # %% imprime o sinal de porcentagem.
print(frase1)

print(f"-----------------------")

nome = "Nycolas"
idade = 31
filhos = 0
frase3 = "{} tem {} anos de idade e tem {} filhos.".format(nome, idade, filhos) #" % pode ser substituido por .format.
print(frase3)

print(f"-----------------------")

frase4 = "Ola, eu vou viajar de {3}".format('bicicleta.', 'moto.', 'carro.', 'trem.')
print(frase4)

print(f"-----------------------")

nome = "Nycolas"
f"O nome dele é {nome}."
valor = 12.57
f"O valor é {valor}"

print(f"-----------------------")
