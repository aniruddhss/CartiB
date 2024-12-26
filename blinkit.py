from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def blinkit_data(product_name: str, location: str):
    # Setup Chrome options
    chrome_options = Options()
    # Comment the next line during debugging
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"
    )
    driver = webdriver.Chrome(options=chrome_options)

    product_data = []

    try:
        print("Opening Blinkit homepage...")
        driver.get("https://blinkit.com/")
        wait = WebDriverWait(driver, 15)

        # Select delivery location
        try:
            print("Waiting for location input field...")
            location_input = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "[placeholder='search delivery location']")
            ))
            print("Location input field found.")
            location_input.click()
            location_input.send_keys(location)
            time.sleep(2)

            # Trigger suggestions
            print("Triggering location suggestions...")
            location_input.send_keys(Keys.SPACE)
            time.sleep(2)

            # Select the first suggestion
            first_suggestion = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div.LocationSearchList__LocationLabel-sc-93rfr7-2.FUlwF")
            ))
            print("Selecting the first suggestion...")
            first_suggestion.click()
            time.sleep(2)
        except Exception as e:
            print("Error selecting location:", e)
            return product_data

        # Search for the product
        print(f"Searching for product: {product_name}...")
        driver.get(f"https://blinkit.com/s/?q={product_name}")
        time.sleep(3)

        # Scrape product details
        if product_name in driver.current_url:
            print("Scraping product details...")
            product_divs = driver.find_elements(
                By.CSS_SELECTOR, 'div.Product__UpdatedPlpProductContainer-sc-11dk8zk-0')
            for product in product_divs:
                try:
                    img_src = product.find_element(
                        By.CSS_SELECTOR, 'div.Imagestyles__ImageContainer-sc-1u3ccmn-0 img').get_attribute('src')
                except:
                    img_src = "No image found"
                try:
                    title = "(Blinkit) " + product.find_element(By.CSS_SELECTOR,
                                                                'div.Product__UpdatedTitle-sc-11dk8zk-9').text
                except:
                    title = "No title found"
                try:
                    description = product.find_element(
                        By.CSS_SELECTOR, 'div.plp-product__quantity--box').text
                except:
                    description = "Description not found"
                try:
                    price = product.find_element(
                        By.CSS_SELECTOR, 'div.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 div[style*="font-weight: 600"]').text
                except:
                    price = "No price found"
                product_data.append(
                    {"image": img_src, "title": title, "description": description, "price": price})
                print(title, price, description)
        else:
            print("Failed to navigate to the product search page.")
    finally:
        driver.quit()
        print("Browser closed.")

    return product_data
