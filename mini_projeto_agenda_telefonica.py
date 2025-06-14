alfabeto = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"

c1_nome = ""
c1_sobrenome = ""
c1_telefone = ""
c1_celular = ""
c1_email = ""
c1_dia_aniv = ""
c1_mes_aniv = ""
c1_ano_aniv = ""

c2_nome = ""
c2_sobrenome = ""
c2_telefone = ""
c2_celular = ""
c2_email = ""
c2_dia_aniv = ""
c2_mes_aniv = ""
c2_ano_aniv = ""

c3_nome = ""
c3_sobrenome = ""
c3_telefone = ""
c3_celular = ""
c3_email = ""
c3_dia_aniv = ""
c3_mes_aniv = ""
c3_ano_aniv = ""

c4_nome = ""
c4_sobrenome = ""
c4_telefone = ""
c4_celular = ""
c4_email = ""
c4_dia_aniv = ""
c4_mes_aniv = ""
c4_ano_aniv = ""

c5_nome = ""
c5_sobrenome = ""
c5_telefone = ""
c5_celular = ""
c5_email = ""
c5_dia_aniv = ""
c5_mes_aniv = ""
c5_ano_aniv = ""

menu = True
while menu:
    print("AGENDA TELEFÔNICA")
    print("1 - Inserir Contato")
    print("2 - Listar Contatos")
    print("3 - Imprimir Contato")
    print("4 - Atualizar Contato")
    print("5 - Remover Contato")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        if c1_nome == "":
            #NOME
            x_nome = True
            while x_nome:
                teste = True
                contador = 0

                print("Digite o nome do contato 1: ")
                c1_nome_teste = input()
                
                for letra in c1_nome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c1_nome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_nome = c1_nome_teste
                    x_nome = False

            #SOBRENOME
            x_sobrenome = True
            while x_sobrenome:
                teste = True
                contador = 0

                print("Digite o sobrenome do contato 1: ")
                c1_sobrenome_teste = input()
                
                for letra in c1_sobrenome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c1_sobrenome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_sobrenome = c1_sobrenome_teste
                    x_sobrenome = False           
            
            #TELEFONE
            x_telefone = True
            while x_telefone:
                teste = True
                contador = 0

                print("Digite o telefone do contato 1: ")
                c1_telefone_teste = input()
                
                for numero in c1_telefone_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_telefone = c1_telefone_teste
                    x_telefone = False 

            #CELULAR
            x_celular = True
            while x_celular:
                teste = True
                contador = 0

                print("Digite o celular do contato 1: ")
                c1_celular_teste = input()
                
                for numero in c1_celular_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c1_celular_teste == "" or contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_celular = c1_celular_teste
                    x_celular = False

            #EMAIL
            x_email = True
            while x_email:
                teste = True
                
                print("Digite o e-mail do contato 1: ")
                c1_email_teste = input()
                contador_a = 0
                contador_b = 0
                contador_c = 0
                tem_arroba = False
                tem_ponto_apos_arroba = False

                for caractere in c1_email_teste:
                    valido = False
                    if (caractere in alfabeto) or (caractere in numeros):
                        valido = True

                            
                    if not valido:
                        if caractere == "@":
                            contador_b += 1
                            tem_arroba = True
                        elif caractere == "." and tem_arroba:
                            tem_ponto_apos_arroba = True
                        else:
                            teste = False
                            break
                    if not tem_arroba and valido:
                        contador_a += 1

                if not (contador_a >= 1) and (contador_b == 1) and tem_ponto_apos_arroba and (c1_email_teste[-1] != ".") and (c1_email_teste[0] != "@") and (c1_email_teste[0] != "."):
                    teste = False
                if teste:
                    c1_email = c1_email_teste
                    x_email = False
                else:
                    print("O valor não atende a especificação do campo.")
           
            #MES DE ANIVERSARIO
            x_mes = True
            while x_mes:
                teste = True
                contador = 0

                print("Digite o mês de aniversario do contato 1: ")
                c1_mes_teste = input()
                
                for numero in c1_mes_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c1_mes_teste) < 1 or int(c1_mes_teste) > 12):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_mes_aniv = c1_mes_teste
                    x_mes = False

            #DIA DE ANIVERSARIO
            x_dia = True
            while x_dia:
                teste = True
                contador = 0

                print("Digite o dia de aniversario do contato 1: ")
                c1_dia_teste = input()
                
                for numero in c1_dia_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c1_dia_teste) < 1 or int(c1_dia_teste) > 31):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_dia_aniv = c1_dia_teste
                    x_dia = False

            #ANO DE ANIVERSARIO
            x_ano = True
            while x_ano:
                teste = True
                contador = 0

                print("Digite o ano de aniversario do contato 1: ")
                c1_ano_teste = input()
                
                for numero in c1_ano_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c1_ano_teste) < 1900 or int(c1_ano_teste) > 2025):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c1_ano_aniv = c1_ano_teste
                    x_ano = False
                    print("O contato", c1_nome, c1_sobrenome, "adicionado com sucesso")

        elif c2_nome == "":
            #NOME
            x_nome = True
            while x_nome:
                teste = True
                contador = 0

                print("Digite o nome do contato 2: ")
                c2_nome_teste = input()
                
                for letra in c2_nome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c2_nome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_nome = c2_nome_teste
                    x_nome = False

            #SOBRENOME
            x_sobrenome = True
            while x_sobrenome:
                teste = True
                contador = 0

                print("Digite o sobrenome do contato 2: ")
                c2_sobrenome_teste = input()
                
                for letra in c2_sobrenome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c2_sobrenome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_sobrenome = c2_sobrenome_teste
                    x_sobrenome = False           
            
            #TELEFONE
            x_telefone = True
            while x_telefone:
                teste = True
                contador = 0

                print("Digite o telefone do contato 2: ")
                c2_telefone_teste = input()
                
                for numero in c2_telefone_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_telefone = c2_telefone_teste
                    x_telefone = False 

            #CELULAR
            x_celular = True
            while x_celular:
                teste = True
                contador = 0

                print("Digite o celular do contato 2: ")
                c2_celular_teste = input()
                
                for numero in c2_celular_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c2_celular_teste == "" or contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_celular = c2_celular_teste
                    x_celular = False

            #EMAIL
            x_email = True
            while x_email:
                teste = True
                
                print("Digite o e-mail do contato 2: ")
                c2_email_teste = input()
                contador_a = 0
                contador_b = 0
                contador_c = 0
                tem_arroba = False
                tem_ponto_apos_arroba = False

                for caractere in c2_email_teste:
                    valido = False
                    if (caractere in alfabeto) or (caractere in numeros):
                        valido = True

                            
                    if not valido:
                        if caractere == "@":
                            contador_b += 1
                            tem_arroba = True
                        elif caractere == "." and tem_arroba:
                            tem_ponto_apos_arroba = True
                        else:
                            teste = False
                            break
                    if not tem_arroba and valido:
                        contador_a += 1

                if not (contador_a >= 2) and (contador_b == 2) and tem_ponto_apos_arroba and (c2_email_teste[-1] != ".") and (c2_email_teste[0] != "@") and (c2_email_teste[0] != "."):
                    teste = False
                if teste:
                    c2_email = c2_email_teste
                    x_email = False
                else:
                    print("O valor não atende a especificação do campo.")

            #MES DE ANIVERSARIO
            x_mes = True
            while x_mes:
                teste = True
                contador = 0

                print("Digite o mês de aniversario do contato 2: ")
                c2_mes_teste = input()
                
                for numero in c2_mes_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c2_mes_teste) < 1 or int(c2_mes_teste) > 12):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_mes_aniv = c2_mes_teste
                    x_mes = False

            #DIA DE ANIVERSARIO
            x_dia = True
            while x_dia:
                teste = True
                contador = 0

                print("Digite o dia de aniversario do contato 2: ")
                c2_dia_teste = input()
                
                for numero in c2_dia_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c2_dia_teste) < 1 or int(c2_dia_teste) > 31):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_dia_aniv = c2_dia_teste
                    x_dia = False

            #ANO DE ANIVERSARIO
            x_ano = True
            while x_ano:
                teste = True
                contador = 0

                print("Digite o ano de aniversario do contato 2: ")
                c2_ano_teste = input()
                
                for numero in c2_ano_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c2_ano_teste) < 1900 or int(c2_ano_teste) > 2025):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c2_ano_aniv = c2_ano_teste
                    x_ano = False
                    print("O contato", c2_nome, c2_sobrenome, "adicionado com sucesso")

        elif c3_nome == "":
            
            #NOME
            x_nome = True
            while x_nome:
                teste = True
                contador = 0

                print("Digite o nome do contato 3: ")
                c3_nome_teste = input()
                
                for letra in c3_nome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c3_nome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_nome = c3_nome_teste
                    x_nome = False

            #SOBRENOME
            x_sobrenome = True
            while x_sobrenome:
                teste = True
                contador = 0

                print("Digite o sobrenome do contato 3: ")
                c3_sobrenome_teste = input()
                
                for letra in c3_sobrenome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c3_sobrenome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_sobrenome = c3_sobrenome_teste
                    x_sobrenome = False           
            
            #TELEFONE
            x_telefone = True
            while x_telefone:
                teste = True
                contador = 0

                print("Digite o telefone do contato 3: ")
                c3_telefone_teste = input()
                
                for numero in c3_telefone_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_telefone = c3_telefone_teste
                    x_telefone = False 

            #CELULAR
            x_celular = True
            while x_celular:
                teste = True
                contador = 0

                print("Digite o celular do contato 3: ")
                c3_celular_teste = input()
                
                for numero in c3_celular_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c3_celular_teste == "" or contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_celular = c3_celular_teste
                    x_celular = False


            #EMAIL
            x_email = True
            while x_email:
                teste = True
                
                print("Digite o e-mail do contato 3: ")
                c3_email_teste = input()
                contador_a = 0
                contador_b = 0
                contador_c = 0
                tem_arroba = False
                tem_ponto_apos_arroba = False

                for caractere in c3_email_teste:
                    valido = False
                    if (caractere in alfabeto) or (caractere in numeros):
                        valido = True

                            
                    if not valido:
                        if caractere == "@":
                            contador_b += 1
                            tem_arroba = True
                        elif caractere == "." and tem_arroba:
                            tem_ponto_apos_arroba = True
                        else:
                            teste = False
                            break
                    if not tem_arroba and valido:
                        contador_a += 1

                if not (contador_a >= 2) and (contador_b == 2) and tem_ponto_apos_arroba and (c3_email_teste[-1] != ".") and (c3_email_teste[0] != "@") and (c3_email_teste[0] != "."):
                    teste = False
                if teste:
                    c3_email = c3_email_teste
                    x_email = False
                else:
                    print("O valor não atende a especificação do campo.")

            #MES DE ANIVERSARIO
            x_mes = True
            while x_mes:
                teste = True
                contador = 0

                print("Digite o mês de aniversario do contato 3: ")
                c3_mes_teste = input()
                
                for numero in c3_mes_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c3_mes_teste) < 1 or int(c3_mes_teste) > 12):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_mes_aniv = c3_mes_teste
                    x_mes = False

            #DIA DE ANIVERSARIO
            x_dia = True
            while x_dia:
                teste = True
                contador = 0

                print("Digite o dia de aniversario do contato 3: ")
                c3_dia_teste = input()
                
                for numero in c3_dia_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c3_dia_teste) < 1 or int(c3_dia_teste) > 31):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_dia_aniv = c3_dia_teste
                    x_dia = False

            #ANO DE ANIVERSARIO
            x_ano = True
            while x_ano:
                teste = True
                contador = 0

                print("Digite o ano de aniversario do contato 3: ")
                c3_ano_teste = input()
                
                for numero in c3_ano_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c3_ano_teste) < 1900 or int(c3_ano_teste) > 2025):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c3_ano_aniv = c3_ano_teste
                    x_ano = False
                    print("O contato", c3_nome, c3_sobrenome, "adicionado com sucesso")

        elif c4_nome == "":
            
            #NOME
            x_nome = True
            while x_nome:
                teste = True
                contador = 0

                print("Digite o nome do contato 4: ")
                c4_nome_teste = input()
                
                for letra in c4_nome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c4_nome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_nome = c4_nome_teste
                    x_nome = False

            #SOBRENOME
            x_sobrenome = True
            while x_sobrenome:
                teste = True
                contador = 0

                print("Digite o sobrenome do contato 4: ")
                c4_sobrenome_teste = input()
                
                for letra in c4_sobrenome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c4_sobrenome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_sobrenome = c4_sobrenome_teste
                    x_sobrenome = False           
            
            #TELEFONE
            x_telefone = True
            while x_telefone:
                teste = True
                contador = 0

                print("Digite o telefone do contato 4: ")
                c4_telefone_teste = input()
                
                for numero in c4_telefone_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_telefone = c4_telefone_teste
                    x_telefone = False 

            #CELULAR
            x_celular = True
            while x_celular:
                teste = True
                contador = 0

                print("Digite o celular do contato 4: ")
                c4_celular_teste = input()
                
                for numero in c4_celular_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c4_celular_teste == "" or contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_celular = c4_celular_teste
                    x_celular = False


            #EMAIL
            x_email = True
            while x_email:
                teste = True
                
                print("Digite o e-mail do contato 4: ")
                c4_email_teste = input()
                contador_a = 0
                contador_b = 0
                contador_c = 0
                tem_arroba = False
                tem_ponto_apos_arroba = False

                for caractere in c4_email_teste:
                    valido = False
                    if (caractere in alfabeto) or (caractere in numeros):
                        valido = True

                            
                    if not valido:
                        if caractere == "@":
                            contador_b += 1
                            tem_arroba = True
                        elif caractere == "." and tem_arroba:
                            tem_ponto_apos_arroba = True
                        else:
                            teste = False
                            break
                    if not tem_arroba and valido:
                        contador_a += 1

                if not (contador_a >= 2) and (contador_b == 2) and tem_ponto_apos_arroba and (c4_email_teste[-1] != ".") and (c4_email_teste[0] != "@") and (c4_email_teste[0] != "."):
                    teste = False
                if teste:
                    c4_email = c4_email_teste
                    x_email = False
                else:
                    print("O valor não atende a especificação do campo.")

            #MES DE ANIVERSARIO
            x_mes = True
            while x_mes:
                teste = True
                contador = 0

                print("Digite o mês de aniversario do contato 4: ")
                c4_mes_teste = input()
                
                for numero in c4_mes_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c4_mes_teste) < 1 or int(c4_mes_teste) > 12):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_mes_aniv = c4_mes_teste
                    x_mes = False

            #DIA DE ANIVERSARIO
            x_dia = True
            while x_dia:
                teste = True
                contador = 0

                print("Digite o dia de aniversario do contato 4: ")
                c4_dia_teste = input()
                
                for numero in c4_dia_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c4_dia_teste) < 1 or int(c4_dia_teste) > 31):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_dia_aniv = c4_dia_teste
                    x_dia = False

            #ANO DE ANIVERSARIO
            x_ano = True
            while x_ano:
                teste = True
                contador = 0

                print("Digite o ano de aniversario do contato 4: ")
                c4_ano_teste = input()
                
                for numero in c4_ano_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c4_ano_teste) < 1900 or int(c4_ano_teste) > 2025):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c4_ano_aniv = c4_ano_teste
                    x_ano = False
                    print("O contato", c4_nome, c4_sobrenome, "adicionado com sucesso")

        elif c5_nome == "":
            
            #NOME
            x_nome = True
            while x_nome:
                teste = True
                contador = 0

                print("Digite o nome do contato 5: ")
                c5_nome_teste = input()
                
                for letra in c5_nome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c5_nome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_nome = c5_nome_teste
                    x_nome = False

            #SOBRENOME
            x_sobrenome = True
            while x_sobrenome:
                teste = True
                contador = 0

                print("Digite o sobrenome do contato 5: ")
                c5_sobrenome_teste = input()
                
                for letra in c5_sobrenome_teste:
                    if letra not in alfabeto:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c5_sobrenome_teste == "" or contador > 20):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_sobrenome = c5_sobrenome_teste
                    x_sobrenome = False           
            
            #TELEFONE
            x_telefone = True
            while x_telefone:
                teste = True
                contador = 0

                print("Digite o telefone do contato 5: ")
                c5_telefone_teste = input()
                
                for numero in c5_telefone_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_telefone = c5_telefone_teste
                    x_telefone = False 

            #CELULAR
            x_celular = True
            while x_celular:
                teste = True
                contador = 0

                print("Digite o celular do contato 5: ")
                c5_celular_teste = input()
                
                for numero in c5_celular_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (c5_celular_teste == "" or contador > 15):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_celular = c5_celular_teste
                    x_celular = False


            #EMAIL
            x_email = True
            while x_email:
                teste = True
                
                print("Digite o e-mail do contato 5: ")
                c5_email_teste = input()
                contador_a = 0
                contador_b = 0
                contador_c = 0
                tem_arroba = False
                tem_ponto_apos_arroba = False

                for caractere in c5_email_teste:
                    valido = False
                    if (caractere in alfabeto) or (caractere in numeros):
                        valido = True

                            
                    if not valido:
                        if caractere == "@":
                            contador_b += 1
                            tem_arroba = True
                        elif caractere == "." and tem_arroba:
                            tem_ponto_apos_arroba = True
                        else:
                            teste = False
                            break
                    if not tem_arroba and valido:
                        contador_a += 1

                if not (contador_a >= 2) and (contador_b == 2) and tem_ponto_apos_arroba and (c5_email_teste[-1] != ".") and (c5_email_teste[0] != "@") and (c5_email_teste[0] != "."):
                    teste = False
                if teste:
                    c5_email = c5_email_teste
                    x_email = False
                else:
                    print("O valor não atende a especificação do campo.")

            #MES DE ANIVERSARIO
            x_mes = True
            while x_mes:
                teste = True
                contador = 0

                print("Digite o mês de aniversario do contato 5: ")
                c5_mes_teste = input()
                
                for numero in c5_mes_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c5_mes_teste) < 1 or int(c5_mes_teste) > 12):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_mes_aniv = c5_mes_teste
                    x_mes = False

            #DIA DE ANIVERSARIO
            x_dia = True
            while x_dia:
                teste = True
                contador = 0

                print("Digite o dia de aniversario do contato 5: ")
                c5_dia_teste = input()
                
                for numero in c5_dia_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c5_dia_teste) < 1 or int(c5_dia_teste) > 31):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_dia_aniv = c5_dia_teste
                    x_dia = False

            #ANO DE ANIVERSARIO
            x_ano = True
            while x_ano:
                teste = True
                contador = 0

                print("Digite o ano de aniversario do contato 5: ")
                c5_ano_teste = input()
                
                for numero in c5_ano_teste:
                    if numero not in numeros:
                        print("O valor não atende a especificação do campo.")
                        teste = False
                    contador +=1

                if (int(c5_ano_teste) < 1900 or int(c5_ano_teste) > 2025):
                    print("O valor não atende a especificação do campo.")
                    teste = False
        
                if teste:
                    c5_ano_aniv = c5_ano_teste
                    x_ano = False
                    print("O contato", c5_nome, c5_sobrenome, "adicionado com sucesso")

    elif opcao == "2":
        print("Contatos:")
        if c1_nome != "":
            print("1 - ", c1_nome, c1_sobrenome)
        if c2_nome != "":
            print("2 - ", c2_nome, c2_sobrenome)
        if c3_nome != "":
            print("3 - ", c3_nome, c3_sobrenome)
        if c4_nome != "":
            print("4 - ", c4_nome, c4_sobrenome)
        if c5_nome != "":
            print("5 - ", c5_nome, c5_sobrenome)
    

    elif opcao == "3":
        nome = input("Digite o nome do contato: ")
        sobrenome = input("Digite o sobrenome do contato: ")
        
        if nome == c1_nome and sobrenome == c1_sobrenome:
            print("Nome - ", c1_nome, c1_sobrenome)
            print("Telefone - ", c1_telefone)
            print("Celular - ", c1_celular)
            print("Email - ", c1_email)
            print("Dia de aniversário - ", c1_dia_aniv)
            print("Mês de aniversário - ", c1_mes_aniv)
            print("Ano de aniversário - ", c1_ano_aniv)
            
        elif nome == c2_nome and sobrenome == c2_sobrenome:
            print("Nome - ", c2_nome, c2_sobrenome)
            print("Telefone - ", c2_telefone)
            print("Celular - ", c2_celular)
            print("Email - ", c2_email)
            print("Dia de aniversário - ", c2_dia_aniv)
            print("Mês de aniversário - ", c2_mes_aniv)
            print("Ano de aniversário - ", c2_ano_aniv)
            
        elif nome == c3_nome and sobrenome == c3_sobrenome:
            print("Nome - ", c3_nome, c3_sobrenome)
            print("Telefone - ", c3_telefone)
            print("Celular - ", c3_celular)
            print("Email - ", c3_email)
            print("Dia de aniversário - ", c3_dia_aniv)
            print("Mês de aniversário - ", c3_mes_aniv)
            print("Ano de aniversário - ", c3_ano_aniv)

        elif nome == c4_nome and sobrenome == c4_sobrenome:
            print("Nome - ", c4_nome, c4_sobrenome)
            print("Telefone - ", c4_telefone)
            print("Celular - ", c4_celular)
            print("Email - ", c4_email)
            print("Dia de aniversário - ", c4_dia_aniv)
            print("Mês de aniversário - ", c4_mes_aniv)
            print("Ano de aniversário - ", c4_ano_aniv)

        elif nome == c5_nome and sobrenome == c5_sobrenome:
            print("Nome - ", c5_nome, c5_sobrenome)
            print("Telefone - ", c5_telefone)
            print("Celular - ", c5_celular)
            print("Email - ", c5_email)
            print("Dia de aniversário - ", c5_dia_aniv)
            print("Mês de aniversário - ", c5_mes_aniv)
            print("Ano de aniversário - ", c5_ano_aniv)
        
        else:
            print("Contato não encontrado")

    elif opcao == "4":
        nome = input("Digite o nome do contato: ")
        sobrenome = input("Digite o sobrenome do contato: ")
        
        if nome == c1_nome and sobrenome == c1_sobrenome:
            menu_atualizacao = True
            while menu_atualizacao:
                print("1 - Nome")
                print("2 - Sobrenome")
                print("3 - Telefone")
                print("4 - Celular")
                print("5 - Email")
                print("6 - Mês de Aniversário")
                print("7 - Dia de Aniversário")
                print("8 - Ano de Aniversário")
                print("9 - Voltar para o menu principal")
                opcao_atualizacao = input()
                if opcao_atualizacao == "1":
                    #NOME
                    x_nome = True
                    while x_nome:
                        teste = True
                        contador = 0

                        print("Digite o nome do contato 1: ")
                        c1_nome_teste = input()
                        
                        for letra in c1_nome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c1_nome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_nome = c1_nome_teste
                            x_nome = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "2":
                    #SOBRENOME
                    x_sobrenome = True
                    while x_sobrenome:
                        teste = True
                        contador = 0

                        print("Digite o sobrenome do contato 1: ")
                        c1_sobrenome_teste = input()
                        
                        for letra in c1_sobrenome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c1_sobrenome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_sobrenome = c1_sobrenome_teste
                            x_sobrenome = False  
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "3":
                    #TELEFONE
                    x_telefone = True
                    while x_telefone:
                        teste = True
                        contador = 0

                        print("Digite o telefone do contato 1: ")
                        c1_telefone_teste = input()
                        
                        for numero in c1_telefone_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_telefone = c1_telefone_teste
                            x_telefone = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "4":
                    #CELULAR
                    x_celular = True
                    while x_celular:
                        teste = True
                        contador = 0

                        print("Digite o celular do contato 1: ")
                        c1_celular_teste = input()
                        
                        for numero in c1_celular_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c1_celular_teste == "" or contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_celular = c1_celular_teste
                            x_celular = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "5":
                    #EMAIL
                    x_email = True
                    while x_email:
                        teste = True
                        
                        print("Digite o e-mail do contato 1: ")
                        c1_email_teste = input()
                        contador_a = 0
                        contador_b = 0
                        contador_c = 0
                        tem_arroba = False
                        tem_ponto_apos_arroba = False

                        for caractere in c1_email_teste:
                            valido = False
                            if (caractere in alfabeto) or (caractere in numeros):
                                valido = True

                                    
                            if not valido:
                                if caractere == "@":
                                    contador_b += 1
                                    tem_arroba = True
                                elif caractere == "." and tem_arroba:
                                    tem_ponto_apos_arroba = True
                                else:
                                    teste = False
                                    break
                            if not tem_arroba and valido:
                                contador_a += 1

                        if not (contador_a >= 1) and (contador_b == 1) and tem_ponto_apos_arroba and (c1_email_teste[-1] != ".") and (c1_email_teste[0] != "@") and (c1_email_teste[0] != "."):
                            teste = False
                        if teste:
                            c1_email = c1_email_teste
                            print("Campo atualizado com sucesso")
                            x_email = False
                        else:
                            print("O valor não atende a especificação do campo.")

                elif opcao_atualizacao == "6":
                    #MES DE ANIVERSARIO
                    x_mes = True
                    while x_mes:
                        teste = True
                        contador = 0

                        print("Digite o mês de aniversario do contato 1: ")
                        c1_mes_teste = input()
                        
                        for numero in c1_mes_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c1_mes_teste) < 1 or int(c1_mes_teste) > 12):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_mes_aniv = c1_mes_teste
                            x_mes = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "7":
                    #DIA DE ANIVERSARIO
                    x_dia = True
                    while x_dia:
                        teste = True
                        contador = 0

                        print("Digite o dia de aniversario do contato 1: ")
                        c1_dia_teste = input()
                        
                        for numero in c1_dia_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c1_dia_teste) < 1 or int(c1_dia_teste) > 31):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_dia_aniv = c1_dia_teste
                            x_dia = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "8":

                    #ANO DE ANIVERSARIO
                    x_ano = True
                    while x_ano:
                        teste = True
                        contador = 0

                        print("Digite o ano de aniversario do contato 1: ")
                        c1_ano_teste = input()
                        
                        for numero in c1_ano_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c1_ano_teste) < 1900 or int(c1_ano_teste) > 2025):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c1_ano_aniv = c1_ano_teste
                            x_ano = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "9":
                    menu_atualizacao = False

        elif nome == c2_nome and sobrenome == c2_sobrenome:

            menu_atualizacao = True
            while menu_atualizacao:
                print("1 - Nome")
                print("2 - Sobrenome")
                print("3 - Telefone")
                print("4 - Celular")
                print("5 - Email")
                print("6 - Mês de Aniversário")
                print("7 - Dia de Aniversário")
                print("8 - Ano de Aniversário")
                print("9 - Voltar para o menu principal")
                opcao_atualizacao = input()
                if opcao_atualizacao == "1":
                    #NOME
                    x_nome = True
                    while x_nome:
                        teste = True
                        contador = 0

                        print("Digite o nome do contato 2: ")
                        c2_nome_teste = input()
                        
                        for letra in c2_nome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c2_nome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_nome = c2_nome_teste
                            x_nome = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "2":
                    #SOBRENOME
                    x_sobrenome = True
                    while x_sobrenome:
                        teste = True
                        contador = 0

                        print("Digite o sobrenome do contato 2: ")
                        c2_sobrenome_teste = input()
                        
                        for letra in c2_sobrenome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c2_sobrenome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_sobrenome = c2_sobrenome_teste
                            x_sobrenome = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "3":
                    #TELEFONE
                    x_telefone = True
                    while x_telefone:
                        teste = True
                        contador = 0

                        print("Digite o telefone do contato 2: ")
                        c2_telefone_teste = input()
                        
                        for numero in c2_telefone_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_telefone = c2_telefone_teste
                            x_telefone = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "4":
                    #CELULAR
                    x_celular = True
                    while x_celular:
                        teste = True
                        contador = 0

                        print("Digite o celular do contato 2: ")
                        c2_celular_teste = input()
                        
                        for numero in c2_celular_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c2_celular_teste == "" or contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_celular = c2_celular_teste
                            x_celular = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "5":
                    #EMAIL
                    x_email = True
                    while x_email:
                        teste = True
                        
                        print("Digite o e-mail do contato 2: ")
                        c2_email_teste = input()
                        contador_a = 0
                        contador_b = 0
                        contador_c = 0
                        tem_arroba = False
                        tem_ponto_apos_arroba = False

                        for caractere in c2_email_teste:
                            valido = False
                            if (caractere in alfabeto) or (caractere in numeros):
                                valido = True

                                    
                            if not valido:
                                if caractere == "@":
                                    contador_b += 1
                                    tem_arroba = True
                                elif caractere == "." and tem_arroba:
                                    tem_ponto_apos_arroba = True
                                else:
                                    teste = False
                                    break
                            if not tem_arroba and valido:
                                contador_a += 1

                        if not (contador_a >= 1) and (contador_b == 1) and tem_ponto_apos_arroba and (c2_email_teste[-1] != ".") and (c2_email_teste[0] != "@") and (c2_email_teste[0] != "."):
                            teste = False
                        if teste:
                            c2_email = c2_email_teste
                            x_email = False
                            print("Campo atualizado com sucesso")

                        else:
                            print("O valor não atende a especificação do campo.")

                elif opcao_atualizacao == "6":
                    #MES DE ANIVERSARIO
                    x_mes = True
                    while x_mes:
                        teste = True
                        contador = 0

                        print("Digite o mês de aniversario do contato 2: ")
                        c2_mes_teste = input()
                        
                        for numero in c2_mes_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c2_mes_teste) < 1 or int(c2_mes_teste) > 12):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_mes_aniv = c2_mes_teste
                            x_mes = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "7":
                    #DIA DE ANIVERSARIO
                    x_dia = True
                    while x_dia:
                        teste = True
                        contador = 0

                        print("Digite o dia de aniversario do contato 2: ")
                        c2_dia_teste = input()
                        
                        for numero in c2_dia_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c2_dia_teste) < 1 or int(c2_dia_teste) > 31):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_dia_aniv = c2_dia_teste
                            x_dia = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "8":

                    #ANO DE ANIVERSARIO
                    x_ano = True
                    while x_ano:
                        teste = True
                        contador = 0

                        print("Digite o ano de aniversario do contato 2: ")
                        c2_ano_teste = input()
                        
                        for numero in c2_ano_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c2_ano_teste) < 1900 or int(c2_ano_teste) > 2025):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c2_ano_aniv = c2_ano_teste
                            x_ano = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "9":
                    menu_atualizacao = False
            
        elif nome == c3_nome and sobrenome == c3_sobrenome:

            menu_atualizacao = True
            while menu_atualizacao:
                print("1 - Nome")
                print("2 - Sobrenome")
                print("3 - Telefone")
                print("4 - Celular")
                print("5 - Email")
                print("6 - Mês de Aniversário")
                print("7 - Dia de Aniversário")
                print("8 - Ano de Aniversário")
                print("9 - Voltar para o menu principal")
                opcao_atualizacao = input()
                if opcao_atualizacao == "1":
                    #NOME
                    x_nome = True
                    while x_nome:
                        teste = True
                        contador = 0

                        print("Digite o nome do contato 3: ")
                        c3_nome_teste = input()
                        
                        for letra in c3_nome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c3_nome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_nome = c3_nome_teste
                            x_nome = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "2":
                    #SOBRENOME
                    x_sobrenome = True
                    while x_sobrenome:
                        teste = True
                        contador = 0

                        print("Digite o sobrenome do contato 3: ")
                        c3_sobrenome_teste = input()
                        
                        for letra in c3_sobrenome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c3_sobrenome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_sobrenome = c3_sobrenome_teste
                            x_sobrenome = False  
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "3":
                    #TELEFONE
                    x_telefone = True
                    while x_telefone:
                        teste = True
                        contador = 0

                        print("Digite o telefone do contato 3: ")
                        c3_telefone_teste = input()
                        
                        for numero in c3_telefone_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_telefone = c3_telefone_teste
                            x_telefone = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "4":
                    #CELULAR
                    x_celular = True
                    while x_celular:
                        teste = True
                        contador = 0

                        print("Digite o celular do contato 3: ")
                        c3_celular_teste = input()
                        
                        for numero in c3_celular_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c3_celular_teste == "" or contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_celular = c3_celular_teste
                            x_celular = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "5":
                    #EMAIL
                    x_email = True
                    while x_email:
                        teste = True
                        
                        print("Digite o e-mail do contato 3: ")
                        c3_email_teste = input()
                        contador_a = 0
                        contador_b = 0
                        contador_c = 0
                        tem_arroba = False
                        tem_ponto_apos_arroba = False

                        for caractere in c3_email_teste:
                            valido = False
                            if (caractere in alfabeto) or (caractere in numeros):
                                valido = True

                                    
                            if not valido:
                                if caractere == "@":
                                    contador_b += 1
                                    tem_arroba = True
                                elif caractere == "." and tem_arroba:
                                    tem_ponto_apos_arroba = True
                                else:
                                    teste = False
                                    break
                            if not tem_arroba and valido:
                                contador_a += 1

                        if not (contador_a >= 1) and (contador_b == 1) and tem_ponto_apos_arroba and (c3_email_teste[-1] != ".") and (c3_email_teste[0] != "@") and (c3_email_teste[0] != "."):
                            teste = False
                        if teste:
                            c3_email = c3_email_teste
                            x_email = False
                            print("Campo atualizado com sucesso")

                        else:
                            print("O valor não atende a especificação do campo.")

                elif opcao_atualizacao == "6":
                    #MES DE ANIVERSARIO
                    x_mes = True
                    while x_mes:
                        teste = True
                        contador = 0

                        print("Digite o mês de aniversario do contato 3: ")
                        c3_mes_teste = input()
                        
                        for numero in c3_mes_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c3_mes_teste) < 1 or int(c3_mes_teste) > 12):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_mes_aniv = c3_mes_teste
                            x_mes = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "7":
                    #DIA DE ANIVERSARIO
                    x_dia = True
                    while x_dia:
                        teste = True
                        contador = 0

                        print("Digite o dia de aniversario do contato 3: ")
                        c3_dia_teste = input()
                        
                        for numero in c3_dia_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c3_dia_teste) < 1 or int(c3_dia_teste) > 31):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_dia_aniv = c3_dia_teste
                            x_dia = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "8":

                    #ANO DE ANIVERSARIO
                    x_ano = True
                    while x_ano:
                        teste = True
                        contador = 0

                        print("Digite o ano de aniversario do contato 3: ")
                        c3_ano_teste = input()
                        
                        for numero in c3_ano_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c3_ano_teste) < 1900 or int(c3_ano_teste) > 2025):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c3_ano_aniv = c3_ano_teste
                            x_ano = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "9":
                    menu_atualizacao = False
            

        elif nome == c4_nome and sobrenome == c4_sobrenome:

            menu_atualizacao = True
            while menu_atualizacao:
                print("1 - Nome")
                print("2 - Sobrenome")
                print("3 - Telefone")
                print("4 - Celular")
                print("5 - Email")
                print("6 - Mês de Aniversário")
                print("7 - Dia de Aniversário")
                print("8 - Ano de Aniversário")
                print("9 - Voltar para o menu principal")
                opcao_atualizacao = input()
                if opcao_atualizacao == "1":
                    #NOME
                    x_nome = True
                    while x_nome:
                        teste = True
                        contador = 0

                        print("Digite o nome do contato 4: ")
                        c4_nome_teste = input()
                        
                        for letra in c4_nome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c4_nome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_nome = c4_nome_teste
                            x_nome = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "2":
                    #SOBRENOME
                    x_sobrenome = True
                    while x_sobrenome:
                        teste = True
                        contador = 0

                        print("Digite o sobrenome do contato 4: ")
                        c4_sobrenome_teste = input()
                        
                        for letra in c4_sobrenome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c4_sobrenome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_sobrenome = c4_sobrenome_teste
                            x_sobrenome = False  
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "3":
                    #TELEFONE
                    x_telefone = True
                    while x_telefone:
                        teste = True
                        contador = 0

                        print("Digite o telefone do contato 4: ")
                        c4_telefone_teste = input()
                        
                        for numero in c4_telefone_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_telefone = c4_telefone_teste
                            x_telefone = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "4":
                    #CELULAR
                    x_celular = True
                    while x_celular:
                        teste = True
                        contador = 0

                        print("Digite o celular do contato 4: ")
                        c4_celular_teste = input()
                        
                        for numero in c4_celular_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c4_celular_teste == "" or contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_celular = c4_celular_teste
                            x_celular = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "5":
                    #EMAIL
                    x_email = True
                    while x_email:
                        teste = True
                        
                        print("Digite o e-mail do contato 4: ")
                        c4_email_teste = input()
                        contador_a = 0
                        contador_b = 0
                        contador_c = 0
                        tem_arroba = False
                        tem_ponto_apos_arroba = False

                        for caractere in c4_email_teste:
                            valido = False
                            if (caractere in alfabeto) or (caractere in numeros):
                                valido = True

                                    
                            if not valido:
                                if caractere == "@":
                                    contador_b += 1
                                    tem_arroba = True
                                elif caractere == "." and tem_arroba:
                                    tem_ponto_apos_arroba = True
                                else:
                                    teste = False
                                    break
                            if not tem_arroba and valido:
                                contador_a += 1

                        if not (contador_a >= 1) and (contador_b == 1) and tem_ponto_apos_arroba and (c4_email_teste[-1] != ".") and (c4_email_teste[0] != "@") and (c4_email_teste[0] != "."):
                            teste = False
                        if teste:
                            c4_email = c4_email_teste
                            x_email = False
                            print("Campo atualizado com sucesso")

                        else:
                            print("O valor não atende a especificação do campo.")

                elif opcao_atualizacao == "6":
                    #MES DE ANIVERSARIO
                    x_mes = True
                    while x_mes:
                        teste = True
                        contador = 0

                        print("Digite o mês de aniversario do contato 4: ")
                        c4_mes_teste = input()
                        
                        for numero in c4_mes_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c4_mes_teste) < 1 or int(c4_mes_teste) > 12):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_mes_aniv = c4_mes_teste
                            x_mes = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "7":
                    #DIA DE ANIVERSARIO
                    x_dia = True
                    while x_dia:
                        teste = True
                        contador = 0

                        print("Digite o dia de aniversario do contato 4: ")
                        c4_dia_teste = input()
                        
                        for numero in c4_dia_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c4_dia_teste) < 1 or int(c4_dia_teste) > 31):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_dia_aniv = c4_dia_teste
                            x_dia = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "8":

                    #ANO DE ANIVERSARIO
                    x_ano = True
                    while x_ano:
                        teste = True
                        contador = 0

                        print("Digite o ano de aniversario do contato 4: ")
                        c4_ano_teste = input()
                        
                        for numero in c4_ano_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c4_ano_teste) < 1900 or int(c4_ano_teste) > 2025):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c4_ano_aniv = c4_ano_teste
                            x_ano = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "9":
                    menu_atualizacao = False

        elif nome == c5_nome and sobrenome == c5_sobrenome:
            
            menu_atualizacao = True
            while menu_atualizacao:
                print("1 - Nome")
                print("2 - Sobrenome")
                print("3 - Telefone")
                print("4 - Celular")
                print("5 - Email")
                print("6 - Mês de Aniversário")
                print("7 - Dia de Aniversário")
                print("8 - Ano de Aniversário")
                print("9 - Voltar para o menu principal")
                opcao_atualizacao = input()
                if opcao_atualizacao == "1":
                    #NOME
                    x_nome = True
                    while x_nome:
                        teste = True
                        contador = 0

                        print("Digite o nome do contato 5: ")
                        c5_nome_teste = input()
                        
                        for letra in c5_nome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c5_nome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_nome = c5_nome_teste
                            x_nome = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "2":
                    #SOBRENOME
                    x_sobrenome = True
                    while x_sobrenome:
                        teste = True
                        contador = 0

                        print("Digite o sobrenome do contato 5: ")
                        c5_sobrenome_teste = input()
                        
                        for letra in c5_sobrenome_teste:
                            if letra not in alfabeto:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c5_sobrenome_teste == "" or contador > 20):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_sobrenome = c5_sobrenome_teste
                            x_sobrenome = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "3":
                    #TELEFONE
                    x_telefone = True
                    while x_telefone:
                        teste = True
                        contador = 0

                        print("Digite o telefone do contato 5: ")
                        c5_telefone_teste = input()
                        
                        for numero in c5_telefone_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_telefone = c5_telefone_teste
                            x_telefone = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "4":
                    #CELULAR
                    x_celular = True
                    while x_celular:
                        teste = True
                        contador = 0

                        print("Digite o celular do contato 5: ")
                        c5_celular_teste = input()
                        
                        for numero in c5_celular_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (c5_celular_teste == "" or contador > 15):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_celular = c5_celular_teste
                            x_celular = False
                            print("Campo atualizado com sucesso")


                elif opcao_atualizacao == "5":
                    #EMAIL
                    x_email = True
                    while x_email:
                        teste = True
                        
                        print("Digite o e-mail do contato 5: ")
                        c5_email_teste = input()
                        contador_a = 0
                        contador_b = 0
                        contador_c = 0
                        tem_arroba = False
                        tem_ponto_apos_arroba = False

                        for caractere in c5_email_teste:
                            valido = False
                            if (caractere in alfabeto) or (caractere in numeros):
                                valido = True

                                    
                            if not valido:
                                if caractere == "@":
                                    contador_b += 1
                                    tem_arroba = True
                                elif caractere == "." and tem_arroba:
                                    tem_ponto_apos_arroba = True
                                else:
                                    teste = False
                                    break
                            if not tem_arroba and valido:
                                contador_a += 1

                        if not (contador_a >= 1) and (contador_b == 1) and tem_ponto_apos_arroba and (c5_email_teste[-1] != ".") and (c5_email_teste[0] != "@") and (c5_email_teste[0] != "."):
                            teste = False
                        if teste:
                            c5_email = c5_email_teste
                            x_email = False
                            print("Campo atualizado com sucesso")

                        else:
                            print("O valor não atende a especificação do campo.")

                elif opcao_atualizacao == "6":
                    #MES DE ANIVERSARIO
                    x_mes = True
                    while x_mes:
                        teste = True
                        contador = 0

                        print("Digite o mês de aniversario do contato 5: ")
                        c5_mes_teste = input()
                        
                        for numero in c5_mes_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c5_mes_teste) < 1 or int(c5_mes_teste) > 12):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_mes_aniv = c5_mes_teste
                            x_mes = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "7":
                    #DIA DE ANIVERSARIO
                    x_dia = True
                    while x_dia:
                        teste = True
                        contador = 0

                        print("Digite o dia de aniversario do contato 5: ")
                        c5_dia_teste = input()
                        
                        for numero in c5_dia_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c5_dia_teste) < 1 or int(c5_dia_teste) > 31):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_dia_aniv = c5_dia_teste
                            x_dia = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "8":

                    #ANO DE ANIVERSARIO
                    x_ano = True
                    while x_ano:
                        teste = True
                        contador = 0

                        print("Digite o ano de aniversario do contato 5: ")
                        c5_ano_teste = input()
                        
                        for numero in c5_ano_teste:
                            if numero not in numeros:
                                print("O valor não atende a especificação do campo.")
                                teste = False
                            contador +=1

                        if (int(c5_ano_teste) < 1900 or int(c5_ano_teste) > 2025):
                            print("O valor não atende a especificação do campo.")
                            teste = False
                
                        if teste:
                            c5_ano_aniv = c5_ano_teste
                            x_ano = False
                            print("Campo atualizado com sucesso")

                elif opcao_atualizacao == "9":
                    menu_atualizacao = False

        else:
            print("Contato não encontrado")
            
    elif opcao == "5":
        nome = input("Digite o nome do contato: ")
        sobrenome = input("Digite o sobrenome do contato: ")

        if nome == c1_nome and sobrenome == c1_sobrenome:
            c1_nome = ""
            c1_sobrenome = ""
            c1_telefone = ""
            c1_celular = ""
            c1_email = ""
            c1_dia_aniv = ""
            c1_mes_aniv = ""
            c1_ano_aniv = ""
            print("Contato",nome, sobrenome, "foi excluído com sucesso")
            
        elif nome == c2_nome and sobrenome == c2_sobrenome:
            c2_nome = ""
            c2_sobrenome = ""
            c2_telefone = ""
            c2_celular = ""
            c2_email = ""
            c2_dia_aniv = ""
            c2_mes_aniv = ""
            c2_ano_aniv = ""
            print("Contato",nome, sobrenome, "foi excluído com sucesso")

        elif nome == c3_nome and sobrenome == c3_sobrenome:
            c3_nome = ""
            c3_sobrenome = ""
            c3_telefone = ""
            c3_celular = ""
            c3_email = ""
            c3_dia_aniv = ""
            c3_mes_aniv = ""
            c3_ano_aniv = ""
            print("Contato",nome, sobrenome, "foi excluído com sucesso")

        elif nome == c4_nome and sobrenome == c4_sobrenome:
            c4_nome = ""
            c4_sobrenome = ""
            c4_telefone = ""
            c4_celular = ""
            c4_email = ""
            c4_dia_aniv = ""
            c4_mes_aniv = ""
            c4_ano_aniv = ""
            print("Contato",nome, sobrenome, "foi excluído com sucesso")

        elif nome == c5_nome and sobrenome == c5_sobrenome:
            c5_nome = ""
            c5_sobrenome = ""
            c5_telefone = ""
            c5_celular = ""
            c5_email = ""
            c5_dia_aniv = ""
            c5_mes_aniv = ""
            c5_ano_aniv = ""
            print("Contato",nome, sobrenome, "foi excluído com sucesso")
        else:
            print("Contato não encontrado")

    elif opcao == "6":
        print("Saindo da agenda...")
        menu = False

    else:
        print("Opção inválida. Tente novamente.")