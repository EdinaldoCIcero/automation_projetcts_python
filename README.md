# 🧪 Selenium MTG Deck Automation (Study Project)

Este projeto é um **script de automação em Python usando Selenium**, criado como **estudo prático**, com o objetivo de automatizar um fluxo entre dois sites de Magic: The Gathering:

- 🔎 **Moxfield** – buscar um deck e copiar a lista de cartas em formato texto  
- 🖨️ **MTGPrint** – colar a lista de cartas e gerar um PDF pronto para impressão  

Tudo isso é feito de forma automática, simulando interações reais do usuário no navegador.

---

## 🚀 O que esse script faz

1. Abre o site **Moxfield**
2. Pesquisa por um deck (ex: `Abzan`)
3. Entra no primeiro deck listado
4. Abre o modal de download
5. Copia a lista de cartas em formato texto
6. Abre o site **MTGPrint**
7. Cola automaticamente a lista copiada
8. Envia o formulário
9. Gera o PDF para impressão das cartas

---

## 🛠️ Tecnologias utilizadas

- Python 3
- Selenium
- Google Chrome / ChromeDriver
- pyperclip
- ActionChains (Selenium)
- winotify


---

## 📦 Requisitos

- Python 3.9 ou superior
- Google Chrome atualizado
- ChromeDriver compatível com a versão do Chrome

ChromeDriver:
https://googlechromelabs.github.io/chrome-for-testing/

---

## 📚 Instalação das dependências

```bash
pip install -r requirements.txt
```

---

## ▶️ Como executar

```bash
python main.py
```

O navegador será aberto automaticamente e o fluxo será executado.

---

## ⚠️ Observações

- O script utiliza **CSS Selectors**, que podem quebrar se os sites mudarem o HTML
- Alguns `time.sleep()` foram usados apenas para estudo
- Projeto com foco educacional para aprendizado de Selenium

---

## 🎯 Objetivo

Projeto criado para praticar:
- Automação web com Selenium
- Esperas explícitas (`WebDriverWait`)
- Interação com inputs, botões, links, modais e textarea
- Automação entre múltiplos sites

---

## 🤝 Autor

Projeto de estudo — Edinaldo Cicero / ÁtomoGames
