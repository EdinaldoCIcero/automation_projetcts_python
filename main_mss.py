import mss
import cv2
import numpy as np
import customtkinter
from random import randint
#-----------------------------------------------



class AppScreenShot( customtkinter.CTk ):
    def __init__(self):
        super().__init__()
        self.geometry("200x150")

        self.button_print = customtkinter.CTkButton(self, text = "Shot" , command = self.screenShotFrame)
        self.button_print.pack(padx=20, pady=20)


    #-----------------------------------------------
    def button_callbck(self):
        print("button clicked")
        pass
        

    #-----------------------------------------------
    def screenShotFrame( self  ):
        rand_name_out = randint( 0 , 10000 )

        path_out_img = "imgs/prints_screen/"
        out_name_img = path_out_img + "shot_" + str( rand_name_out ) + ".png"

        #-------------------------------------------------
        with mss.mss() as sct:
            monitor_screen      = sct.monitors[1]
            print_screen_img    = sct.grab( monitor_screen  )

            screen_frame = np.array( print_screen_img )
            cv2.imwrite( out_name_img , screen_frame )

        print("Screenshot feita com sucesso e salva em " , out_name_img )
        
        pass
        

#-----------------------------------------------------
app = AppScreenShot()
app.mainloop()


