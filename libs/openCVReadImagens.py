import cv2
import numpy as np


#----------------------------------------------------

#-----------------------------------------------
class OpenCVRead():
    def __init__(self , path_img_fullscreen , path_area_img_element_reference ):
        super().__init__()


        # carregar imagens
        self.imagem             = cv2.imread( path_img_fullscreen )
        self.template           = cv2.imread(  path_area_img_element_reference )
        # converter para escala de cinza (mais estável)
        self.imagem_gray        = cv2.cvtColor( self.imagem, cv2.COLOR_BGR2GRAY)
        self.template_gray      = cv2.cvtColor( self.template, cv2.COLOR_BGR2GRAY)
        # pegar tamanho do template
        self.h, self.w          = self.template_gray.shape
        # template matching
        self.result_end         = cv2.matchTemplate( self.imagem_gray , self.template_gray , cv2.TM_CCOEFF_NORMED )


        # encontrar melhor correspondência
        self.min_val, self.max_val, self.min_loc, self.max_loc = cv2.minMaxLoc( self.result_end )

        # desenhar retângulo onde encontrou
        self.top_left       = self.max_loc
        self.bottom_right   = ( self.top_left[0] + self.w, self.top_left[1] + self.h )

        
        #cv2.rectangle( imagem , top_left , bottom_right, (0, 255, 0), 2)

        # mostrar resultado
        #cv2.imshow("Resultado", imagem)
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()

        self.center_x = self.top_left[0] + self.w // 2
        self.center_y = self.top_left[1] + self.h // 2


      

    def positionsValuesElement( self ):

        #print("Centro:", self.center_x, self.center_y)
        #print("Localizações:", self.max_val , self.max_loc )
        centers     = [ self.center_x, self.center_y ]
        max_values  = [ self.max_val , self.max_loc ] 
        
        return centers , max_values
     
