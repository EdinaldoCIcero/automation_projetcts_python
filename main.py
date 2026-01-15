
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import csv

import pyperclip
#---------------------------------------------------------------------

URL_LIST_OF_SITES = [ 
    "https://moxfield.com/", # 0 - Site 1
    "https://mtgprint.net/", # 1 - Site 2

]




#------------------------------------------------------------------------

driver = webdriver.Chrome()
wait   = WebDriverWait(driver, 15) # esperando um tempo para a pagina carregar e ai sim ter os elementos para pegar

driver.get( URL_LIST_OF_SITES[0] ) #Carregando a primeira pagina 

# adquado pra algumas ações, uma delas que estou usando ele é para selecionar em focus um elemento antes de 
# Clicar nele ou usar p Keys.ENTER blz
actions = ActionChains(driver)


#------------
input_busca = wait.until( EC.presence_of_element_located( ( By.CSS_SELECTOR, "input[type='search']") ) )
input_busca.send_keys("Abzan")
time.sleep( 2 )
input_busca.send_keys( Keys.ENTER )



#---------- estou usando o Sleep mais nõa é muito recomendando segundo minhas pesquisas kkk :)
# ---- mais me dá um tempo tá... sacou kkkk ?!
time.sleep( 1 )
card_deck_one = wait.until( EC.presence_of_element_located( ( By.CSS_SELECTOR, "div.browse-ad-layout-content div > a" ) ) )

actions.move_to_element( card_deck_one ).perform()


card_deck_one.click()




#------------ apertando com ENTER no link download para abrir o modal de seleção de downloads 
open_modal_downloads_link = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div.deck-dnd-wrapper > div.mb-3 > div > div > div > div.col-auto.d-flex > span:nth-child(4) > a" ))
)

actions.move_to_element( open_modal_downloads_link ).perform()

open_modal_downloads_link.send_keys( Keys.ENTER )






#------------ clicando no button de copiar o txt list dso nomes das cartas 
button_copy_text_list_cards_names = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "body > div.modal.zoom.show.d-block > div > div > div.modal-body > div > div.d-flex.flex-row.flex-nowrap.gap-3 > div.flex-shrink-1.d-inline-flex.flex-column.flex-wrap.gap-2.align-items-stretch > button:nth-child(4)" ))
)

actions.move_to_element( button_copy_text_list_cards_names ).perform()

button_copy_text_list_cards_names.click()


#----- abrindo o segundo site para usar o text copiado dos nomes das cartas no MTG PRINT para fazer o PDF das cartas

driver.get( URL_LIST_OF_SITES[1] ) #Carregando a segunda  pagina da lista 



#------------
text_area_mtg_print = wait.until(
    EC.presence_of_element_located((By.ID, "paste-deck" ))
)

actions.move_to_element( text_area_mtg_print ).perform()


coping_text_cards_names = pyperclip.paste()
text_area_mtg_print.send_keys( coping_text_cards_names )


# depois de colar o texto com os nomes das cartas agora é apertar o button submit e depois em pinti pra gerar o PDF

#------------
button_submit_load_names_cards = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div > div > div > div > div.buttons > button" ))
)

actions.move_to_element( button_submit_load_names_cards ).perform()

button_submit_load_names_cards.click()



#input("Pressione ENTER para continuar caso não queira mudar algo...")


#------------ button_print
button_to_print_maker_pdf = wait.until(
    EC.presence_of_element_located((By.CSS_SELECTOR, "div > div > div > div > div.columns.is-desktop.is-flex-reversed.is-multiline.is-vcentered > div.column.is-narrow > button" ))
)

actions.move_to_element( button_to_print_maker_pdf ).perform()

button_to_print_maker_pdf.send_keys( Keys.ENTER )



#input("Pressione ENTER para fechar o programa ok :) ...")

driver.quit()
