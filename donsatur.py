import json
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager # pip install webdriver-manager

opts = Options()
opts.add_argument("user-agent=Mozilla/5.0  Chrome/122.0.6261.128")
opts.add_argument("--headless")

# Alternativamente:
# driver = webdriver.Chrome(
#     service=Service('./chromedriver'),
#     options=opts
# )

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=opts
)

driver.get('https://www.donsatur.com.ar/#product')

sleep(3)

product_data = []
card_path = driver.find_elements(By.XPATH, '//div[contains(@class,"image_with_text")]')
for card in card_path:
    image_url = card.find_element(By.TAG_NAME, 'img').get_attribute('src')
    don_satur_product = card.text.strip()
    product_data.append({'image_url': image_url, 'don_satur_product': don_satur_product})

if product_data:
    with open('donsaturProducts.json', 'w') as outfile:
        json.dump(product_data, outfile, indent=4)
    print("Product information saved to products.json")
else:
    print("No product information found.")
