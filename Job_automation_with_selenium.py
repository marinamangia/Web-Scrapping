from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.google.com')
barra_pesquisa = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
barra_pesquisa.send_keys('ciencia de dados vagas\n')

# clicando na pesquisa do linkedin
WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="rso"]/div[3]/div/'
                                                                            'div[1]/div/a/h3'))).click()

descricao = driver.find_element(By.CLASS_NAME,'show-more-less-html__markup')
resultados = driver.find_elements(By.CLASS_NAME,'base-card__full-link')

lista_descricoes=[]
for i in resultados:
    i.click()
    descricao = driver.find_element(By.CLASS_NAME,'show-more-less-html__markup')
    lista_descricoes.append(descricao.text)


