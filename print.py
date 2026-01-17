import tkinter as tk
from PIL import ImageGrab
from random import randint
import mss
import cv2
import numpy as np
import customtkinter
import os


#----------------------------------------------------



#----------------------------------------------------
class ScreenSelector:
    def __init__(self , path_out_img ):
        self.root = tk.Tk()

        self.path_out_img = path_out_img

        # tela inteira configuração de tela do app
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg="blue")
        self.root.overrideredirect(True)

        #--------- usando o Cavnas para criar a area preta responsavel por sonseguir desenhar o retangulo 
        self.canvas = tk.Canvas( self.root, cursor = "cross" , bg="black" )
        self.canvas.pack(fill=tk.BOTH, expand=True)
        #-----------------------------------------------------------------------------------------------

        #--- Positions
        self.start_x    = None
        self.start_y    = None
        self.rect       = None

        # carregando as funç~eos de Draw do retangulo
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)

        #------------------------
        self.root.mainloop()

    #-----------------------------------

    def on_mouse_down(self, event):
        self.start_x , self.start_y = event.x , event.y

        self.rect = self.canvas.create_rectangle(   self.start_x, self.start_y,
                                                    self.start_x, self.start_y,
                                                    outline = "red",
                                                    width   = 2
                                                )

    #-----------------------------------
    def on_mouse_drag(self, event):
        self.canvas.coords( self.rect, self.start_x, self.start_y, event.x, event.y )
        

    #----- função responsavel por fazer o prin e salvar 
    def on_mouse_up( self , event  ):
        #rand_name_out = randint( 0 , 10000 )

        #path_out_img = "imgs/prints_screen/"
        #out_name_img = path_out_img + "area_shot_" + str( rand_name_out ) + ".png"
    
        end_x = event.x
        end_y = event.y

        #----------------------------------------------------------------------

        x1 = min( self.start_x , end_x )
        y1 = min( self.start_y , end_y )
        x2 = max( self.start_x , end_x )
        y2 = max( self.start_y , end_y )

        self.root.destroy() # fechar o TK

        # usando o pillow para criar a imagem do screenshot, sómente em windows
        screenshot = ImageGrab.grab( bbox = ( x1, y1, x2, y2 ) )
        screenshot.save( self.path_out_img )

        print("Área salva com sucesso!")


#-----------------------------------------------
class AppScreenShot( customtkinter.CTk ):
    def __init__(self):
        super().__init__()
        self.geometry("200x150")


        self.button_print = customtkinter.CTkButton(self, text = "Shot" , command =  self.button_callbck )
        self.button_print.pack(padx=20, pady=20)
        
        self.new_user_folder  = "open_any_desk_3/"
        self.path_out_img     = "database/prints_screen/" + self.new_user_folder 
        self.count_print_numb = 0
        
    #-----------------------------------------------
    def setImgName( self , rand_name_out , name_img = "screen_shot_" , extetion_type = ".png"  ):

        out_img_rand_name_end = self.path_out_img + name_img + str( rand_name_out ) + extetion_type

        return out_img_rand_name_end
    

    #-----------------------------------------------
    def button_callbck(self):
        rand_name_out = randint( 0 , 10000 )
        
        self.count_print_numb += 1
        #-------------------------------------------------------------------------------------------

        # Verifica se a pasta já existe para não gerar erro
        if not os.path.exists( self.path_out_img ):
            #os.mkdir( self.new_user_folder )
        
            # Cria a pasta e todas as pastas pais que não existem
            os.makedirs(self.path_out_img, exist_ok = True)
            print(f"Caminho '{self.path_out_img}' criado com sucesso (ou já existia).")
        
        

        self.screenShotComplete( path_out_img = self.setImgName( rand_name_out  = str( self.count_print_numb ) ,  
                                                                 name_img       = "screen_shot_" 
                                                                 ) )
        
        
        ScreenSelector( path_out_img = self.setImgName( rand_name_out = str( self.count_print_numb ) , 
                                                         name_img = "print_area_shot_" ) )
        
        
        print(f"Pasta '{ self.new_user_folder }' criada com sucesso!")
        

        pass
    


     #-----------------------------------------------
    def screenShotComplete( self  , path_out_img ):
        
        #-------------------------------------------------
        with mss.mss() as sct:
            monitor_screen      = sct.monitors[1]
            print_screen_img    = sct.grab( monitor_screen  )

            screen_frame = np.array( print_screen_img )
            cv2.imwrite( path_out_img , screen_frame )

        print("Screenshot feita com sucesso e salva em " , path_out_img )
        
        pass


#-----------------------------------------------------
app = AppScreenShot()
app.mainloop()