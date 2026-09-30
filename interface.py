import customtkinter as ctk
ctk.set_appearance_mode('light') #Aqui indicara qual será o tema da janela (optei pelo modo escuro)
#______________________________________________________________-
#Aqui começa a janela
janela = ctk.CTk()
janela.geometry('600x400')
janela.title('Academia SmartFit')
janela.iconbitmap('halter.ico')
janela.resizable(False,False)
#______________________________________________________________
#Aqui estará tudo o que está dentro da janela (texto, espaço cliente, butão)

titulo = ctk.CTkLabel(janela,
                      text = 'Academia Inteligente',
                      font = ('Times new roman', 40),
                      text_color = "#f7d30b"
                      )
subtitulo = ctk.CTkLabel(janela,
                         text = 'Seja bem-vindo à nossa academia',
                         font = ('Times new roman', 20),
                         text_color = "#0a0606"
                         )
titulo.pack(pady = 15) #não pode faltar pois é responsável pela funcionalidade do comando
subtitulo.pack()

login = ctk.CTkEntry(janela,
                     width = 200,
                     height = 15,
                     placeholder_text = 'Digite seu login: ',
                     border_color = '#000000',
                      )
senha = ctk.CTkEntry(janela,
                     width = 200,
                     height = 15,
                     placeholder_text = 'Digite a sua senha: ',
                     border_color = '#000000',
                     show = '*',
                     )
login.pack(pady=15)
senha.pack()

butao = ctk.CTkButton(janela,
                      text = 'Entrar',
                      font= ('Arial', 13, 'normal'),
                      width= 70,
                      height= 15,
                      )


butao.pack(pady = 15)



janela.mainloop()
