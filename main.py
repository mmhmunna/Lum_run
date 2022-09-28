from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome((ChromeDriverManager().install()), options=chrome_options)


#driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
print("ok")
baseurl = "http://207.154.254.191/bikeapi-price-update-by-csv"
driver.get(baseurl)
time.sleep(2)
driver.switch_to.new_window()
driver.get("http://207.154.254.191/bikeapi-genarate-report")
time.sleep(1)
driver.switch_to.new_window()
driver.get("http://207.154.254.191/bikeapi-report")
time.sleep(1)
driver.switch_to.new_window()
driver.get("http://207.154.254.191/bikeapi-missing-product-sync?updated=1")
time.sleep(1)
driver.switch_to.new_window()
driver.get("http://207.154.254.191/b2buhren-product-update-by-csv?updated=1")
time.sleep(1)

confirm = input("Are you want to close:")
if(confirm == 1):
   print("successfull")
else:
   print("Good bye")
