#importação das bibliotecas necessárias 
import os
import time
import psutil

# Definindo a quantidade de repetições e o tamanho do arquivo criado
QTD_REPETIÇÃO = 10000
TAMANHO_ARQUIVO = 10000

# Função para realizar a tarefa de benchmark
def benchmark():
    
    # Inicia a contagem do tempo
    inicio = time.time()
    
    # Laço de repetição da maniuplação de arquivos de acordo com a quantidade de repetições
    for i in range(QTD_REPETIÇÃO):
        
        # Cria o arquivo e escreve a palavra "Teste"
        with open("teste.txt", "w") as arquivo:
            arquivo.write("Teste")

        # Lê o arquivo
        with open("teste.txt", "r") as arquivo:
            reading = arquivo.read()

        # Remove o arquivo
        os.remove("teste.txt")

    # Calcula o tempo total
    tempo_total = time.time() - inicio
    
    # Puxa de psutil o percentual de memória e CPU
    Uso_CPU = psutil.cpu_percent()
    Uso_Memoria = psutil.virtual_memory()

    # Printa os valores e finaliza o código
    print(f"Tempo total: {tempo_total:.3f} segundos")
    print(f'Uso da CPU: {Uso_CPU}%')
    print(f'Uso da memória: {Uso_Memoria.percent}%\n')
    print("-----------------------------------------------------------------------------")

# Função principal
def main():
    
    # Prints para deixar a estética mais agradável ao usuário, em um design semelhante a uma "Nota Fiscal"
    print("-----------------------------------------------------------------------------\n")
    print("     Iniciando o teste de Benchmark de desempenho geral do sistema       ")
    print("    Nosso teste é voltado para eficiência da manipulação de arquivos       \n")
    print("Esta operação pode demorar alguns segundos, por favor aguarde...\n")
    print("-----------------------------------------------------------------------------\n")
    print("Para melhor execução do teste\n -Feche todos os aplicativos\n -Execute apenas o aplicativo do teste\n")
    print("-----------------------------------------------------------------------------\n")
    print('Teste de Arquivos\n')
    print("-----------------------------------------------------------------------------\n")
    
    # Chamada da Função Benchmark
    benchmark()
    
    # Input para pausar o resultado na tela, caso qualquer tecla seja tocada, o programa se encerra
    input("Pressione qualquer tecla para sair")

# If para garantir que a função main seja executada caso seja a função atual a ser executada
if __name__ == "__main__":
    main()