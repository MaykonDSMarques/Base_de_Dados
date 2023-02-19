from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd

#Inicio da pesquisa de Cotações
navegador = webdriver.Chrome()

navegador.get("https://www.google.com/")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação dólar')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_dolar = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_dolar)

navegador.get("https://www.google.com/")
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('cotação euro')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
cotacao_euro = navegador.find_element('xpath', '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')
print(cotacao_euro)

navegador.get("https://www.melhorcambio.com/ouro-hoje")
cotacao_Ouro = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
cotacao_Ouro = cotacao_Ouro.replace(',', '.')
print(cotacao_Ouro)
#Fim da pesquisa de Cotações

#Abrindo Arquivo
tabela = pd.read_excel("Produtos.xlsx")
print(tabela)

#Alterando valores
tabela.loc[tabela["Moeda"] == "Dólar", "Cotação" ] = float(cotacao_dolar)
tabela.loc[tabela["Moeda"] == "Euro", "Cotação" ] = float(cotacao_euro)
tabela.loc[tabela["Moeda"] == "Ouro", "Cotação" ] = float(cotacao_Ouro)
tabela["Preço de Compra"] = tabela["Cotação"] * tabela["Preço Original"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]
print(tabela)

#criação do arquivo atualizado
tabela.to_excel("Produtos_Atualizados.xlsx", index=False)