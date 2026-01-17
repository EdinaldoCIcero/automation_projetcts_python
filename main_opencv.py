import cv2
import numpy as np
import pyautogui

# carregar imagens
imagem      = cv2.imread("imgs\img_base.png")
template    = cv2.imread("imgs\img_template.png")

# converter para escala de cinza (mais estável)
imagem_gray     = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
template_gray   = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

# pegar tamanho do template
h, w = template_gray.shape

# template matching
resultado = cv2.matchTemplate( imagem_gray , template_gray , cv2.TM_CCOEFF_NORMED )


# encontrar melhor correspondência
min_val, max_val, min_loc, max_loc = cv2.minMaxLoc( resultado )




# desenhar retângulo onde encontrou
top_left = max_loc
bottom_right = (top_left[0] + w, top_left[1] + h)

#cv2.rectangle( imagem , top_left , bottom_right, (0, 255, 0), 2)

# mostrar resultado
#cv2.imshow("Resultado", imagem)
#cv2.waitKey(0)
#cv2.destroyAllWindows()

center_x = top_left[0] + w // 2
center_y = top_left[1] + h // 2

print("Centro:", center_x, center_y)

#----------------------------------------------
print("Localizações:", max_val , max_loc )

print("Confiança:", max_val)
print("Posição:", max_loc)


#------ pyautogui processe simples



screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.



pyautogui.moveTo( center_x , center_y ) # Move the mouse to XY coordinates.
pyautogui.click( center_x , center_y )
pyautogui.press('enter') 

#pyautogui.click()          # Click the mouse.
#pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
#pyautogui.click('button.png') # Find where button.png appears on the screen and click it.

#pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
#pyautogui.doubleClick()     # Double click the mouse.
#pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

#pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key