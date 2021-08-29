import time
from selenium import webdriver
from selenium.webdriver import support
from selenium .webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

def wait(time_to_wait):
    print("esperando=="+ str(time_to_wait) + "milisegundo")
    time.sleep(int(time_to_wait))


def clickOnElement(xpath,driver):
    wait_web_driver=WebDriverWait(driver,10)  
    help_element = wait_web_driver.until(
    expected_conditions.visibility_of_element_located((By.XPATH,xpath)))
    print(" cicking ==>" + str(xpath))
    help_element.click()


#   //inicializando webdriver

driver=webdriver.Chrome(
    executable_path=r"C:\Driver_Chrome\chromedriver")

URL=str("https://www.bbc.com/mundo/")
print("accesando a la pagina==" + str(URL))
driver.get (URL)
wait(8)


xpath_Ciencia = str("//*[@class='bbc-8u7uv3 e1lim4kn3'][text()='Ciencia']")

clickOnElement(xpath_Ciencia, driver)
#haciendo click  articulo de ciencia

xpath_lee_mas = str("//*[@class='lx-stream-post__header-text gs-u-align-middle'][text()='5 mitos y creencias falsas sobre las alergias y la intolerancia a los alimentos']")
clickOnElement(xpath_lee_mas, driver)

#haciendo click en tecnologia
xpath_Tecnologia = str("//*[@class='bbc-8u7uv3 e1lim4kn3'][text()='Tecnología']")

clickOnElement(xpath_Tecnologia, driver)

#haciendo click en el menu

xpath_menu = str("//*[@class='istats-notrack'][text()='Menú']")

clickOnElement(xpath_menu, driver)

#haciendo click en weather

xpath_Weather = str("//*[@href='https://www.bbc.com/weather']")

clickOnElement(xpath_Weather, driver)


# wait(2)
print("cerrando driver")
driver.close()