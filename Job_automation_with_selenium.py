from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

get_google = driver.get('https://www.google.com')
barra_pesquisa = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
barra_pesquisa.send_keys('ciencia de dados vagas\n')

# clicando na pesquisa do linkedin
resultado_linkedin = driver.find_element(By.CLASS_NAME,'LC20lb MBeuO DKV0Md')
resultado_linkedin.click()

