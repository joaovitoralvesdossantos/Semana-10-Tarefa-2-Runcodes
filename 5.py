# Calcula o valor do juros de 1 até 24 do valor.
def parcela(valor_compra):
    for numero_parcela in range(1, 25):
       valor_prestacao = valor_compra / numero_parcela
       print (f"{numero_parcela}x de R$ {valor_prestacao:.2f}")

#função principal
def main():
    #entrada de dados:
    valor = float(input("Digite o valor da compra: "))

    #processamento e saída de dados:
    parcela(valor)

# chama a função principal
if __name__ == '__main__':
    main()