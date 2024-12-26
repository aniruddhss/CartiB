from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def blinkit_data(product_name: str, location: str):

    axis_location = [23.211754, 77.433601]

    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--use-gl=swiftshader") 
    chrome_options.add_argument("--disable-software-rasterizer")

    chrome_options.add_argument("user-agent= Chromium/91.0.4472.124")


    driver = webdriver.Chrome(options=chrome_options)
    driver.set_window_size(1920, 1080)

    # Open the webpage with dynamic product search and axis_location
    driver.get(f'https://blinkit.com/s/?q={product_name}&lat={axis_location[0]}&lon={axis_location[1]}')
    driver.execute_script("document.body.style.zoom='40%'")
    time.sleep(3) 

    product_containers = driver.find_elements(By.CSS_SELECTOR, '.Product__UpdatedPlpProductContainer-sc-11dk8zk-0')
    product_data = []

    for product in product_containers:
        try:
            img_src = product.find_element(By.CSS_SELECTOR, '.Imagestyles__ImageContainer-sc-1u3ccmn-0 img').get_attribute('src')
        except Exception as e:
            img_src = "No image found"

        try:
            title = "(Blinkit) " + product.find_element(By.CSS_SELECTOR,'.Product__UpdatedTitle-sc-11dk8zk-9').text
        except Exception as e:
            title = "No title found"

        try:
            description = product.find_element(By.CSS_SELECTOR, '.plp-product__quantity--box').text
        except Exception as e:
            description = "Description not found"

        try:
            price = product.find_element(By.CSS_SELECTOR, '.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 .Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 div').text
        except Exception as e:
            price = "No price found"

        product_data.append({"image": img_src, "title": title, "description": description, "price": price})
        print(title, price, description)

    driver.quit()
    print("Browser closed.")

    return product_data

# blinkit_data("dahi", "indrapuri")
