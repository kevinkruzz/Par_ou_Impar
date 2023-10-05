from tkinter import *
from constantes import *
from calculo_par_impar import *
import random
import tkinter.messagebox as mbox
'''
import win32gui, win32con

try:
    ocultar_janela = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(ocultar_janela, win32con.SW_HIDE)

except:
    pass
'''
raiz = Tk()

class Janela():
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, bg=cinza1)
        self.fr1.pack()

        self.fr2 = Frame(raiz, bg=cinza1)
        self.fr2.pack()

        self.fr3 = Frame(raiz, bg=cinza1)
        self.fr3.pack()

        self.fr4 = Frame(raiz, bg= cinza1)
        self.fr4.pack()

        self.fr5 = Frame(raiz, bg= cinza1)
        self.fr5.pack()

        self.fr6 = Frame(raiz, bg= cinza1)
        self.fr6.pack()


        self.img_player = PhotoImage(file='imagens/ninja.png')
        self.img0 = PhotoImage(file='imagens/numero_0.png')
        self.img1 = PhotoImage(file='imagens/numero_1.png')
        self.img2 = PhotoImage(file='imagens/numero_2.png')
        self.img3 = PhotoImage(file='imagens/numero_3.png')
        self.img4 = PhotoImage(file='imagens/numero_4.png')
        self.img5 = PhotoImage(file='imagens/numero_5.png')
        self.img6 = PhotoImage(file='imagens/numero_6.png')
        self.img7 = PhotoImage(file='imagens/numero_7.png')
        self.img8 = PhotoImage(file='imagens/numero_8.png')
        self.img9 = PhotoImage(file='imagens/numero_9.png')
        self.img10 = PhotoImage(file='imagens/numero_10.png')
        self.img_pc = PhotoImage(file='imagens/robo.png')

        self.botao_restart = Button(self.fr1, text='Restart', pady= 3, bg= azul_claro, font= fonte5, relief= RAISED, border=8, command= self.resetar)
        self.botao_restart.bind('<Return>',self.resetar2)
        self.botao_restart.pack()

        #Texto inicial 
        self.lb1 = Label(self.fr1, text='BATALHA DO KAKASHI', pady= 10, font= fonte1, bg= cinza1, fg= azul2)
        self.lb1.pack()

        #Resultado
        self.lb_result = Label(self.fr1, text='', font=fonte1, bg= cinza1, fg='green')
        self.lb_result.pack()

        # Placar
        self.placar1 = 0
        self.placar2 = 0
    
        self.lb2 = Label(self.fr1, text= 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR",
                         bg= cinza1, font = fonte3, fg= azul2, pady= 10)
        self.lb2.pack()

        #imagem do jogador
        self.lbimg1 = Label(self.fr3, image= self.img_player,bg= cinza1)
        self.lbimg1.pack(side= LEFT)

        #espaço entre as imagens
        self.lb_separador = Label(self.fr3, text='      ',bg= cinza1)
        self.lb_separador.pack(side= LEFT)

        #imagem do computador
        self.lbimg2 = Label(self.fr3, image= self.img_pc, bg= cinza1)
        self.lbimg2.pack(side= LEFT)


        self.escolha = StringVar()

        #escolha par     
        self.rb_par = Radiobutton(self.fr4, text='Par', value= 'par', variable= self.escolha, bg= cinza1,
                                   fg= azul2, font= fonte2, pady= 20)
        self.rb_par.pack(side= LEFT)

        #escolha impar
        self.rb_impar = Radiobutton(self.fr4, text='Impar', value='impar', variable= self.escolha, bg= cinza1,
                                    fg= azul2, font= fonte2, pady= 20)
        self.rb_impar.pack(side= LEFT)

        #texto information
        self.lb3 = Label(self.fr5, text='Numero de 0 a 10: ',bg= cinza1, fg= azul2, font= fonte3, width= 15, pady= 20)
        self.lb3.pack(side= LEFT)

        #caixa escolha
        self.num = Entry(self.fr5, width= 2, font= fonte3)
        self.num.pack(side= LEFT)

        self.bt_jogar = Button(self.fr6, text="JOGAR", font=fonte1, bg=cinza2, relief= RAISED, border=8, command=self.jogar)
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack()

        self.lb_error = Label(self.fr6, text= '', font= fonte4, bg= cinza1, fg= 'red',pady= 20)
        self.lb_error.pack()
    
    def jogar(self):
        try:

            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0,11)

            if escolha == 'par' or escolha == 'impar':
                if num >= 0 and num <=10:
                    if num == 0:
                        self.lbimg1['image'] = self.img0
                        self.lb_error['text'] = ''
                    elif num == 1:
                        self.lbimg1['image'] = self.img1
                        self.lb_error['text'] = ''
                    elif num == 2:
                        self.lbimg1['image'] = self.img2
                        self.lb_error['text'] = ''
                    elif num == 3:
                        self.lbimg1['image'] = self.img3
                        self.lb_error['text'] = ''
                    elif num == 4:
                        self.lbimg1['image'] = self.img4
                        self.lb_error['text'] = ''
                    elif num == 5:
                        self.lbimg1['image'] = self.img5
                        self.lb_error['text'] = ''
                    elif num == 6:
                        self.lbimg1['image'] = self.img6
                        self.lb_error['text'] = ''
                    elif num == 7:
                        self.lbimg1['image'] = self.img7
                        self.lb_error['text'] = ''
                    elif num == 8:
                        self.lbimg1['image'] = self.img8
                        self.lb_error['text'] = ''
                    elif num == 9:
                        self.lbimg1['image'] = self.img9
                        self.lb_error['text'] = ''
                    elif num == 10:
                        self.lbimg1['image'] = self.img10
                        self.lb_error['text'] = ''
            

                    if num_robo == 0:
                        self.lbimg2['image'] = self.img0
                    elif num_robo == 1:
                        self.lbimg2['image'] = self.img1
                    elif num_robo == 2:
                        self.lbimg2['image'] = self.img2
                    elif num_robo == 3:
                        self.lbimg2['image'] = self.img3
                    elif num_robo == 4:
                        self.lbimg2['image'] = self.img4
                    elif num_robo == 5:
                        self.lbimg2['image'] = self.img5
                    elif num_robo == 6:
                        self.lbimg2['image'] = self.img6
                    elif num_robo == 7:
                        self.lbimg2['image'] = self.img7
                    elif num_robo == 8:
                        self.lbimg2['image'] = self.img8
                    elif num_robo == 9:
                        self.lbimg2['image'] = self.img9
                    elif num_robo == 10:
                        self.lbimg2['image'] = self.img10

                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == 'par':
                        self.lb_result['text'] = 'DEU PAR'
                    elif par_impar == 'impar':
                        self.lb_result['text'] = 'DEU IMPAR'

                    if par_impar == 'par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"

                    elif par_impar == 'par' and escolha == 'impar':
                        self.placar2 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"
                    
                    elif par_impar == 'impar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"

                    elif par_impar == 'impar' and escolha == 'par':
                        self.placar2 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"



                else:
                        self.lb_error['text'] = 'ERROR!! DIGITE APENAS NUMEROS DE 0 A 10'
            else:
                        self.lb_error['text'] =  'ERROR!!!...ESCOLHA IMPAR OU PAR'
                    
        except:
            self.lb_error['text'] = 'ERROR!! ESCOLHA SOMENTE NUMEROS DE 0 A 10'
    
    def jogar2(self, event):
        try:

            num = int(self.num.get())
            escolha = self.escolha.get()
            num_robo = random.randrange(0,11)

            if escolha == 'par' or escolha == 'impar':
                if num >= 0 and num <=10:
                    if num == 0:
                        self.lbimg1['image'] = self.img0
                        self.lb_error['text'] = ''
                    elif num == 1:
                        self.lbimg1['image'] = self.img1
                        self.lb_error['text'] = ''
                    elif num == 2:
                        self.lbimg1['image'] = self.img2
                        self.lb_error['text'] = ''
                    elif num == 3:
                        self.lbimg1['image'] = self.img3
                        self.lb_error['text'] = ''
                    elif num == 4:
                        self.lbimg1['image'] = self.img4
                        self.lb_error['text'] = ''
                    elif num == 5:
                        self.lbimg1['image'] = self.img5
                        self.lb_error['text'] = ''
                    elif num == 6:
                        self.lbimg1['image'] = self.img6
                        self.lb_error['text'] = ''
                    elif num == 7:
                        self.lbimg1['image'] = self.img7
                        self.lb_error['text'] = ''
                    elif num == 8:
                        self.lbimg1['image'] = self.img8
                        self.lb_error['text'] = ''
                    elif num == 9:
                        self.lbimg1['image'] = self.img9
                        self.lb_error['text'] = ''
                    elif num == 10:
                        self.lbimg1['image'] = self.img10
                        self.lb_error['text'] = ''
            

                    if num_robo == 0:
                        self.lbimg2['image'] = self.img0
                    elif num_robo == 1:
                        self.lbimg2['image'] = self.img1
                    elif num_robo == 2:
                        self.lbimg2['image'] = self.img2
                    elif num_robo == 3:
                        self.lbimg2['image'] = self.img3
                    elif num_robo == 4:
                        self.lbimg2['image'] = self.img4
                    elif num_robo == 5:
                        self.lbimg2['image'] = self.img5
                    elif num_robo == 6:
                        self.lbimg2['image'] = self.img6
                    elif num_robo == 7:
                        self.lbimg2['image'] = self.img7
                    elif num_robo == 8:
                        self.lbimg2['image'] = self.img8
                    elif num_robo == 9:
                        self.lbimg2['image'] = self.img9
                    elif num_robo == 10:
                        self.lbimg2['image'] = self.img10

                    par_impar = calcular_par_impar(num, num_robo)
                    if par_impar == 'par':
                        self.lb_result['text'] = 'DEU PAR'
                    elif par_impar == 'impar':
                        self.lb_result['text'] = 'DEU IMPAR'

                    if par_impar == 'par' and escolha == 'par':
                        self.placar1 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"

                    elif par_impar == 'par' and escolha == 'impar':
                        self.placar2 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"
                    
                    elif par_impar == 'impar' and escolha == 'impar':
                        self.placar1 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"

                    elif par_impar == 'impar' and escolha == 'par':
                        self.placar2 += 1
                        self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"



                else:
                        self.lb_error['text'] = 'ERROR!! DIGITE APENAS NUMEROS DE 0 A 10'
            else:
                        self.lb_error['text'] =  'ERROR!!!...ESCOLHA IMPAR OU PAR'
                    
        except:
            self.lb_error['text'] = 'ERROR!! ESCOLHA SOMENTE NUMEROS DE 0 A 10'

    def resetar(self):
        resp = mbox.askquestion('Restart', 'Deseja Reiniciar?')
        if resp == 'yes':
            self.lb_result['text'] = ''
            self.lbimg1['image'] = self.img_player
            self.lbimg2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"
            self.lb_error['text'] = ''
    
    def resetar2(self, event):
        resp = mbox.askquestion('Restart', 'Deseja Resetar?')
        if resp == 'yes':
            self.lb_result['text'] = ''
            self.lbimg1['image'] = self.img_player
            self.lbimg2['image'] = self.img_pc
            self.placar1 = 0
            self.placar2 = 0
            self.lb2['text'] = 'JOGADOR          '+str(self.placar1)+ "  x  " + str(self.placar2) + "   COMPUTADOR"
            self.lb_error['text'] = ''

# tamanho da janela
raiz.geometry('840x650+300+30')
 #icone da janela
raiz.iconbitmap('imagens/ninjaa.ico')
#titulo da barra do programa
raiz.title('Par ou Impar by KevinCruz')
# cor da fundo do prograa
raiz['bg'] = cinza1


janela = Janela(raiz)
raiz.mainloop()