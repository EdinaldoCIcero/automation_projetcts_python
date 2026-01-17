import tkinter as tk
import threading
import customtkinter
from PIL import ImageGrab
from random import randint
import mss
import cv2
import numpy as np
import os
import time


#------------------------------------------------------
from libs.openCVReadImagens import OpenCVRead



#----------------------------------------------------
class ScreenSelector:
    def __init__(self, parent, path_out_img, on_finish ):
        self.on_finish      = on_finish
        self.path_out_img   = path_out_img

        self.root = tk.Toplevel(parent)
        self.root.attributes("-fullscreen", True)
        self.root.attributes("-alpha", 0.3)
        self.root.configure(bg="blue")
        self.root.overrideredirect(True)

        self.canvas = tk.Canvas(self.root, cursor="cross", bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.start_x = None
        self.start_y = None
        self.rect    = None

        # aplicando as funçãos draws e drags
        self.canvas.bind("<ButtonPress-1>", self.on_mouse_down)
        self.canvas.bind("<B1-Motion>", self.on_mouse_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_mouse_up)



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

        self.on_finish()



#-----------------------------------------------
class AppScreenShot( customtkinter.CTk ):
    def __init__(self):
        super().__init__()
        self.geometry("200x150")


        self.button_print = customtkinter.CTkButton(self, text = "Shot" , command =  self.buttonPrint )
        self.button_print.pack(padx=20, pady=20)
        
        self.path_database    = "database/"
        self.new_user_folder  = "open_any_desk_1"
        self.path_out_img     = "database/prints_screen/" + self.new_user_folder + "/"
        self.count_print_numb = 0
        
        self.read           = False
        self.new_img_shot   = ""
        self.new_img_print  = "" 

        #-------------------------------
        # IDEIA DE BANCO DE DADOS PARA PYAUTOGUI....
        self.data_save_process_locs_values = {
            "NAME_PROCESS"   : self.new_user_folder,
            "STEPS_VALUES"   : [
                                [ "CENTER_INT_POS_X" , "CENTER_INT_POS_Y" , "STR( TYPE_ACTION = (CLICK , KEY , WRITE_TEXT ) )" ],
                                [ "CENTER_INT_POS_X" , "CENTER_INT_POS_Y" , "STR( TYPE_ACTION = (CLICK , KEY , WRITE_TEXT ) )" ],

                                ]
        }


    #-----------------------------------------------
    def setImgName( self , rand_name_out , name_img = "screen_shot_" , extetion_type = ".png"  ):
        out_img_rand_name_end = self.path_out_img + name_img + str( rand_name_out ) + extetion_type
        return out_img_rand_name_end
    

    #-----------------------------------------------
    def buttonPrint(self):
        rand_name_out = randint( 0 , 10000 )
        self.count_print_numb += 1
        #-------------------------------------------------------------------------------------------

        # Verifica se a pasta já existe para não gerar erro
        if not os.path.exists( self.path_out_img ):
            #os.mkdir( self.new_user_folder )
        
            # Cria a pasta e todas as pastas pais que não existem
            os.makedirs(self.path_out_img, exist_ok = True)
            print(f"Caminho '{self.path_out_img}' criado com sucesso (ou já existia).")
        
        
        self.new_img_shot  = self.setImgName( rand_name_out  = str( self.count_print_numb ) ,  name_img       = self.new_user_folder + "_shot_" )
        self.new_img_print = self.setImgName( rand_name_out = str( self.count_print_numb ) , name_img = self.new_user_folder + "_print_" )
        
        self.screenShotComplete( path_out_img = self.new_img_shot )
        
        
        ScreenSelector( parent       = self , 
                        path_out_img = self.new_img_print, 
                        on_finish    = self.readOpen 
                       )
        


    #-----------------------------------------------
    def screenShotComplete( self  , path_out_img ):
        
        #-------------------------------------------------
        with mss.mss() as sct:
            monitor_screen      = sct.monitors[1]
            print_screen_img    = sct.grab( monitor_screen  )
            screen_frame        = np.array( print_screen_img )
            cv2.imwrite( path_out_img , screen_frame )

        print("Screenshot feita com sucesso e salva em " , path_out_img )
        
        pass

    

    #-----------------------------------------------
    def readOpen(self):
        new_read_img = OpenCVRead( path_img_fullscreen              = self.new_img_shot  , 
                                   path_area_img_element_reference  = self.new_img_print 
                                   )
        
        centers , max_values = new_read_img.positionsValuesElement( )

        print( "--> Center : " , centers , "---> Location : ", max_values )
        
        
        pass
        


#-----------------------------------------------------
app = AppScreenShot()
app.mainloop()
