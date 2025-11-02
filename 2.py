# exibe na tela uma frase com numero de 99 a 250.
def cancao():
    for i in range(99, 251):
        print(f'{i} bugs no software, pegue um deles e conserte...\nTecle "Ctrl+F5"')
        
# função principal:        
def main():

    # processamento e saída de dados:
        cancao()
    #Termina a canção com “Vamos fazer mais um café!”.
        print(f"Vamos fazer mais um café!")

# chama a função principa:
if __name__ == '__main__':
    main()