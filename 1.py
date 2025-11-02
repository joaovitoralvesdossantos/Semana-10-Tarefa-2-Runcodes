# exibe na tela uma frase com numero de 99 a 250.
def conta():
    for i in range(99, 251):
        print (f"{i} bugs no software, pegue um deles e conserte...")

# Função principal
def main():
    
    #processamento e saida de dados:
    conta()

# chama a função principal:
if __name__ == '__main__':
    main()