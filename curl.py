from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()
driver.get('https://animekaizoku.com/anime/series/hinomaruzumou-720p-eng-sub-x265/')

time.sleep(6)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#glist-65 > tbody"))
    )
    print(element)
finally:
    driver.quit()


