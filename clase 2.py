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
    wait_web_driver=WebDriverWait(driver,5)  
    help_element = wait_web_driver.until(
    expected_conditions.visibility_of_element_located((By.XPATH,xpath)))
    print(" cicking ==>" + str(xpath))
    help_element.click()


#   //inicializando webdriver

driver=webdriver.Chrome(
    executable_path=r"C:\Driver_Chrome\chromedriver")

URL=str("https://pypi.org/")
print("accesando a la pagina==" + str(URL))
driver.get (URL)
wait(8)

xpath_help = str("//*[@class='horizontal-menu__link'][text()='Help']")
clickOnElement(xpath_help, driver)

wait(2)

xpath_login = str("//*[@class='horizontal-menu__link'][text()='Log in']")

clickOnElement(xpath_login, driver)

# wait(2)


print("cerrando driver")
driver.close()