from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL_GOOGLE='https://www.google.com'
XPATH_BARRA_PESQUISA='/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'

if __name__=='__main__':
    # Create Google Chrome instance in Selenium
    driver = webdriver.Chrome()
    driver.maximize_window()
    # Get URL Google
    driver.get(URL_GOOGLE)
    # Get Goolge search bar and search
    barra_pesquisa = driver.find_element(By.XPATH, XPATH_BARRA_PESQUISA)
    barra_pesquisa.send_keys('ciencia de dados vagas\n')

    # Click on Linkedin search
    WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rso"]/div[3]/div/'
                                                                                'div[1]/div/a/h3'))).click()
    # Get result list and job descriptions
    resultados = driver.find_elements(By.CLASS_NAME, 'base-card__full-link')
    descricao = driver.find_element(By.CLASS_NAME,'show-more-less-html__markup')

    lista_descricoes=[]
    # Begin loop to get descriptions on a list
    while True:
        for i in resultados[len(lista_descricoes):]:
            sleep(1)
            i.click()
            try:
                descricao = driver.find_element(By.CLASS_NAME,'show-more-less-html__markup')
                lista_descricoes.append(descricao.text)
            except:
                pass
        resultados = driver.find_elements(By.CLASS_NAME, 'base-card__full-link')
        # While loop exit
        if len(lista_descricoes) == len(resultados):
            break
    # Salve descriptions from list together
    salvar_descricao = '\n'.join(lista_descricoes)
    # create a file with all of the descriptions
    with open('descricoes_vagas.txt','w') as f:
        f.write(salvar_descricao)


