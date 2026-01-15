from playwright.sync_api import sync_playwright
from winotify import Notification, audio
import pyperclip
import time


#--------------------------------------------------------

URL_LIST_OF_SITES = [ 
    "https://moxfield.com/", # 0 - Site 1
    "https://mtgprint.net/", # 1 - Site 2

]


#-------------------------------------------------------

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context( accept_downloads = True ) # permitir downloads normalmente
    page    = context.new_page()


    #-------------------------------------------------
    # Passos do processo da automação ----------------


    # --- Site 1: Moxfield ---
    page.goto( URL_LIST_OF_SITES[0] )

    # input de busca no modo decks cards magic
    page.fill("input[type='search']", "Abzan")
    page.press("input[type='search']", "Enter")

    # espera os resultados
    page.wait_for_selector("div.browse-ad-layout-content a")

    # clica no primeiro deck da lista de cards da pagina
    page.locator("div.browse-ad-layout-content a").first.click()

    # espera a página de decks carregear 
    page.wait_for_selector("div.deck-dnd-wrapper")

    # hover no card do primeiro deck
    page.hover("div.deck-dnd-wrapper")

    # abre modal de download
    page.locator("a", has_text="Download").click()


    # clica no botão de copiar lista usando diretamente o .clik
    page.wait_for_selector( "body > div.modal.zoom.show.d-block > div > div > div.modal-body > div > div.d-flex.flex-row.flex-nowrap.gap-3 > div.flex-shrink-1.d-inline-flex.flex-column.flex-wrap.gap-2.align-items-stretch > button:nth-child(4)" ).click()



    # pega texto do clipboard
    texto_cartas = pyperclip.paste()

    # --- Site 2: MTGPrint ---
    page.goto( URL_LIST_OF_SITES[1] )


    page.fill("#paste-deck", texto_cartas)

    page.locator("button", has_text="Submit").click()


    # garante que o botão existe
    page.wait_for_selector("button:has-text('Print')")

    # agora sim: espera o download E clica
    with page.expect_download() as download_info:
        page.wait_for_selector( "div > div > div > div > div.columns.is-desktop.is-flex-reversed.is-multiline.is-vcentered > div.column.is-narrow > button" ).click()
        #page.locator("button", has_text="Print").first.click() essa forma sunciona também, pegando o primeiro button com o texto print


    download = download_info.value

    download.save_as("temp/" + download.suggested_filename )



    notification_end = Notification(
                        app_id      = "MTG Automation",
                        title       = "Processo finalizado 🎉",
                        msg         = "O PDF das cartas foi gerado com sucesso!",
                        duration    = "short"
                        )


    
    time.sleep( 1 )
    notification_end.set_audio( audio.Default , loop = False )
    notification_end.show()
    
    input("Pressione ENTER para fechar o programa ok :) ...")
    browser.close()

