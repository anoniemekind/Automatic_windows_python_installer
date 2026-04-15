from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Setup driver
driver = webdriver.Chrome()
driver.get("https://ozh.github.io/cookieclicker/")

# Wait for the page to load
time.sleep(5)

# Select language (English)
try:
    lang_select = driver.find_element(By.ID, "langSelect-EN")
    lang_select.click()
except:
    pass

# Wait for game to load
time.sleep(5)

# Find the big cookie
cookie = driver.find_element(By.ID, "bigCookie")

# Click it 100 times
for i in range(100):
    cookie.click()
    time.sleep(0.01)  # small delay so it doesn't break

# Optional: close browser
# driver.quit()
