import requests
from datetime import date
import json
import time
from selenium import webdriver
from selenium.webdriver import ActionChains, firefox
from selenium.webdriver.firefox.options import Options
from pysimplegui_crawler import telainicial


# i=0
# n_of_prod = int(input("entre com a quantidade de equipamentos a cadastrar: "))
# product_type = input("ENTRE COM O NOME DO PRODUTO: ")
# while i < n_of_prod:
class CrawlerProject(telainicial):
    user = telainicial.tela.values['user']
    password = telainicial.tela.values['password']
    tipo_produtdo = telainicial.tela.values['tp_equipamento']
    qntd = int(telainicial.tela.values['qntd'])
    value = telainicial.tela.values['value']
    count = 0

    url = "https://synsuite.cleannet.com.br/materials/operational_dashboard#maintenance-objects"
    options = Options()
    options.headless = True
    driver = webdriver.Firefox(executable_path="/Users/noc03/PycharmProjects/crawler_project/geckodriver")
    driver.get(url)
    # login
    usuario = driver.find_element_by_xpath("//*[@id='UserLogin']")
    pswrd = driver.find_element_by_xpath("//*[@id='UserPassword2']")
    # TODO -- Criar função para pegar o login atravéz da interface
    usuario.send_keys(user)
    pswrd.send_keys(password)
    driver.find_element_by_xpath("/html/body/section/div[2]/form/button").click()  # Login Button Interaction

    # adicionar produto
    time.sleep(5)
    driver.find_element_by_id("maintenance-objects").click()
    time.sleep(5)
    while count < qntd:
        driver.find_element_by_class_name("action-new").click()
        time.sleep(5)
        driver.find_element_by_id("searchProduct").click()
        time.sleep(5)
        # select product
        # TODO --criação da interface enviará dados do roteador
        driver.find_element_by_xpath("/html/body/div[6]/div[2]/div/div[1]/div[1]/label/input").send_keys("keo")
        time.sleep(5)
        source = driver.find_element_by_id("2549")
        target = driver.find_element_by_id("2549")
        ActionChains(driver).drag_and_drop(source, target).perform()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[6]/div[3]/div/button[1]").click()  # confirm

        # select Company
        driver.find_element_by_id("UserCompaniesPlaceList").click()
        time.sleep(5)
        source = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]")
        target = driver.find_element_by_xpath("/html/body/div[7]/div[2]/div/div[2]/div[2]/table/tbody/tr[1]/td[1]")
        ActionChains(driver).drag_and_drop(source, target).perform()
        driver.find_element_by_xpath("/html/body/div[7]/div[3]/div/button[1]").click()

        # select type
        driver.find_element_by_id("PatrimonyTypeList").click()
        time.sleep(3)
        # todo - criar variavel que recebe valor de acordo com o produto
        driver.find_element_by_xpath("/html/body/div[9]/div[2]/div/div[1]/div[1]/label/input").send_keys("roteador")
        source = driver.find_element_by_id("1")
        target = driver.find_element_by_id("1")
        ActionChains(driver).drag_and_drop(source, target).perform()
        driver.find_element_by_xpath("/html/body/div[9]/div[3]/div/button[1]/span").click()

        # serie number input
        nserie = telainicial.tela.Nserie()  # todo - criar interface de pop up para receber o input numero de serie
        print(nserie)
        driver.find_element_by_id("PatrimonySerialNumber").click()
        driver.find_element_by_id("PatrimonySerialNumber").send_keys(nserie)

        # Patrimony number
        npatrimonio = telainicial.tela.Patrimonio()  # todo - criar interface de pop up para receber o input patrimonio
        driver.find_element_by_id("PatrimonyTagNumber").send_keys(npatrimonio)

        # date
        driver.find_element_by_id("PatrimonyPurchaseDate").click()
        driver.find_element_by_xpath("/html/body/div[8]/table/tbody/tr[4]/td[2]").click()

        # product value
        driver.find_element_by_id("PatrimonyPurchaseAmount").send_keys(value)

        #  api integration to consult if it's a real mac
        confir = False

        while confir == False:

            macaddress = telainicial.tela.Mac()

            ismac = requests.get(url="http://api.macvendors.com/%s" % macaddress)
            if ismac.status_code == 200:
                driver.find_element_by_id("PatrimonyMac").send_keys(macaddress)
                confir = True
            else:
                telainicial.tela.MacErrada()
                macaddress = telainicial.tela.Mac()

        # APENAS DESCOMENTAR LINHA DEPOIS DE CRIAR INTERFACE GRAFICA
        # driver.find_element_by_xpath("/html/body/div[4]/div[3]/div/button[1]/span")

        count = count + 1
