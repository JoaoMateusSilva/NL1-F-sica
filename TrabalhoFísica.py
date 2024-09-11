import numpy as np

c = 3e8  
u0 = 4 * np.pi * 1e-7

def descricao():
    
    print("Autores:")
    print("Heron de Souza, João Mateus E. B. da Silva, Sergio de Siqueira Santos, Vinicius Trivellato Pereira")
    
    print()
    
    print("Sobre o programa:")
    print("Este programa realiza cálculos envolvendo ondas eletromagnéticas.")
    print("Ele permite calcular parâmetros como o campo elétrico (Em), campo magnético (Bm),")
    print("intensidade da onda (I), além de parâmetros como a frequência (f),")
    print("comprimento de onda (λ), número de onda (k), e frequência angular (ω).")
    
    print()
    
    print("Conceitos físicos envolvidos:")
    print("Ondas eletromagnéticas são perturbações que se propagam no espaço transportando energia.")
    print("Elas consistem em campos elétricos (Em) e magnéticos (Bm) oscilantes,")
    print("que são perpendiculares entre si e à direção de propagação da onda.")
    print("Essas ondas podem se propagar no vácuo, com a velocidade da luz (c ≈ 3.0 x 10^8 m/s),")
    print("e são descritas por grandezas como frequência (f), comprimento de onda (λ),")
    print("número de onda (k), e intensidade (I).")
    
    print()
    
    print("Equações utilizadas:")
    print("- Bm = Em / c")
    print("- I = Em² / (2 * u0 * c)")
    print("- f = c / λ")
    print("- k = 2π / λ")
    print("- ω = 2πf")
    
    print()
    
    print("Limitações:")
    print("- As equações assumem que a onda eletromagnética se propaga no vácuo.")
    print("- Não considera atenuações, reflexões ou interferências de materiais.")
    
    print()
    
    print("Observações:")
    print("As entradas do programa devem ser: 6.58e-3 ou 8.27e6, caso os números sejam em notações científicas.")

def calc_campos_eletromagneticos():
    print("Escolha a entrada:")
    print("1 - Em (Campo Elétrico)")
    print("2 - Bm (Campo Magnético)")
    print("3 - I (Intensidade da Onda)")

    tipo_entrada = input("Digite 1, 2 ou 3: ")

    if tipo_entrada == "1":
        Em = float(input("Digite o valor de Em (Campo Elétrico) em V/m: "))
        Bm = Em / c
        I = Em**2 / (2 * u0 * c)

        print(f"Campo Magnético (Bm): {Bm:.5e} T")
        print(f"Intensidade da Onda (I): {I:.5e} W/m²")

    elif tipo_entrada == "2":
        Bm = float(input("Digite o valor de Bm (Campo Magnético) em µT: ")) * 1e-6  
        Em = Bm * c  
        I = (Bm**2 * c) / (2 * u0)  

        print(f"Campo Elétrico (Em): {Em:.5e} V/m")
        print(f"Intensidade da Onda (I): {I:.5e} W/m²")


    elif tipo_entrada == "3":
        I = float(input("Digite o valor de I (Intensidade da Onda) em W/m²: "))
        Em = (2 * I * u0 * c)**0.5
        Bm = Em / c

        print(f"Campo Elétrico (Em): {Em:.5e} V/m")
        print(f"Campo Magnético (Bm): {Bm:.5e} T")

    else:
        print("Opção não existente.")

def calcular_parametros_onda():
    print("Escolha a entrada:")
    print("1 - Frequência (f)")
    print("2 - Comprimento de onda (λ)")
    print("3 - Número de onda (k)")
    print("4 - Frequência angular (ω)")

    tipo_entrada = input("Digite 1, 2, 3 ou 4: ")

    if tipo_entrada == "1":  
        f = float(input("Digite o valor da frequência (f) em Hz: "))
        λ = c / f
        k = 2 * np.pi / λ
        ω = 2 * np.pi * f

        print(f"Comprimento de onda (λ): {λ:.5e} m")
        print(f"Número de onda (k): {k:.5e} rad/m")
        print(f"Frequência angular (ω): {ω:.5e} rad/s")

    elif tipo_entrada == "2":
        λ = float(input("Digite o valor do comprimento de onda (λ) em metros: "))
        f = c / λ
        k = 2 * np.pi / λ
        ω = 2 * np.pi * f

        print(f"Frequência (f): {f:.5e} Hz")
        print(f"Número de onda (k): {k:.5e} rad/m")
        print(f"Frequência angular (ω): {ω:.5e} rad/s")
        
    elif tipo_entrada == "3":  
        k = float(input("Digite o valor do número de onda (k) em rad/m: "))
        λ = 2 * np.pi / k
        f = c / λ
        ω = 2 * np.pi * f

        print(f"Frequência (f): {f:.5e} Hz")
        print(f"Comprimento de onda (λ): {λ:.5e} m")
        print(f"Frequência angular (ω): {ω:.5e} rad/s")

    elif tipo_entrada == "4": 
        ω = float(input("Digite o valor da frequência angular (ω) em rad/s: "))
        f = ω / (2 * np.pi)
        λ = c / f
        k = 2 * np.pi / λ

        print(f"Frequência (f): {f:.5e} Hz")
        print(f"Comprimento de onda (λ): {λ:.5e} m")
        print(f"Número de onda (k): {k:.5e} rad/m")

    else:
        print("Opção não existente.")

def menu():
    descricao() 
    
    while True:
        print("\nSelecione uma das opções abaixo:")
        print("1 - Calcular campos eletromagnéticos (Em, Bm, I)")
        print("2 - Calcular parâmetros de onda (f, λ, k, ω)")
        print("3 - Sair")

        opcao = input("Digite o número da opção: ")

        if opcao == "1":
            calc_campos_eletromagneticos() 
        elif opcao == "2":
            calcular_parametros_onda()  
        elif opcao == "3":
            print("Saindo do programa...")
            break
        else:
            print("Opção não existente.")
menu()
    
