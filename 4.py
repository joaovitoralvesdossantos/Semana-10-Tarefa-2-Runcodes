# exibe na tela uma frase com numero de 99 a 250 aumentando de 7 em 7.
def cancao():
    for i in range(99, 0, -11):
        print(f'{i} bugs no software, pegue onze deles e conserte...\nTecle "Ctrl+F5"')
        
# função principal:        
def main():

    # processamento e saída de dados:
        cancao()
    #Termina a canção com “Vamos fazer mais um café!”.
        print(f"Sem erros no software! Está estabilizado!")

# chama a função principa:
if __name__ == '__main__':
    main()