from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
#-------------------------------------------------------------------


class SelenChromeWeb:
    def __init__( self , set_url , set_timind_drive = 15 ):

        self.set_timind_drive = set_timind_drive

        self.driver     = webdriver.Chrome()
        self.wait       = WebDriverWait( self.driver , self.set_timind_drive ) 
        self.actions    = ActionChains(self.driver)

        self.driver.get( set_url)



        self.modls_by = {
            "id"                : By.ID ,
            "name"              : By.NAME,
            "xpath"             : By.XPATH,
            "link_text"         : By.LINK_TEXT,
            "partial_link_text" : By.PARTIAL_LINK_TEXT,
            "tag_name"          : By.TAG_NAME,
            "class_name"        : By.CLASS_NAME,
            "css_selector"      : By.CSS_SELECTOR
        }
        
        pass
    


    #------------------------------------------------------------------
    def setNewURL( self , set_new_url ):
        self.driver.get( set_new_url ) #Carregando uma nova  pagina web 

        pass

    #-----------------------------------------------------------------------------------------------------------------
    # Função para elementos que funcionam com eventos keys.ENTER .
    def setPresenceLocatedElementEventENTER( self ,  element_web = "txt" ,  type_by = "css_selector" ):

        set_presenc_element_enter = self.wait.until(
            EC.presence_of_element_located(( self.modls_by[ type_by ] , element_web ))
        )

        self.actions.move_to_element( set_presenc_element_enter ).perform()

        
        set_presenc_element_enter.send_keys( Keys.ENTER )

        return set_presenc_element_enter


    #-----------------------------------------------------------------------------------------------------------------
    # Função para elementos que funcionam com eventos Click
    def setPresenceLocatedElementEventCLICK( self , element_web = "txt" ,  type_by = "css_selector"  ):

        set_presenc_element_click = self.wait.until(
            EC.presence_of_element_located(( self.modls_by[ type_by ] , element_web ))
        )

        self.actions.move_to_element( set_presenc_element_click ).perform()

        set_presenc_element_click.click()


        return set_presenc_element_click
    