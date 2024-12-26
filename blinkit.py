from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def blinkit_data(product_name: str, location: str):
    axis_location = [23.211754, 77.433601]

    chrome_options = Options()
    # Runs Chrome in headless mode (no UI)
    chrome_options.add_argument("--headless")
    # Disables GPU hardware acceleration
    chrome_options.add_argument("--disable-gpu")
    # Disables sandboxing to make it more stable in headless mode
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(
        "user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chromium/91.0.4472.124 Safari/537.36")

    # Initialize the driver with the headless options
    driver = webdriver.Chrome(options=chrome_options)

    driver.set_window_size(1920, 1080)

    # Open Blinkit with the given product and location
    driver.get(
        f'https://blinkit.com/s/?q={product_name}&lat={axis_location[0]}&lon={axis_location[1]}')

    time.sleep(3)  # Allow time for the page to load

    product_data = []

    try:
        if product_name in driver.current_url:
            print("Scraping product details...")

            # Locate all product containers
            product_divs = driver.find_elements(
                By.CSS_SELECTOR, '.Product__UpdatedPlpProductContainer-sc-11dk8zk-0')

            for product in product_divs:
                try:
                    # Extracting image source URL
                    img_src = product.find_element(
                        By.CSS_SELECTOR, '.Imagestyles__ImageContainer-sc-1u3ccmn-0 img').get_attribute('src')
                except Exception as e:
                    img_src = "No image found"

                try:
                    # Extracting product title
                    title = "(Blinkit) " + product.find_element(By.CSS_SELECTOR,
                                                                '.Product__UpdatedTitle-sc-11dk8zk-9').text
                except Exception as e:
                    title = "No title found"

                try:
                    # Extracting product description (quantity)
                    description = product.find_element(
                        By.CSS_SELECTOR, '.plp-product__quantity--box').text
                except Exception as e:
                    description = "Description not found"

                try:
                    # Extracting product price
                    price = product.find_element(
                        By.CSS_SELECTOR, '.Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 .Product__UpdatedPriceAndAtcContainer-sc-11dk8zk-10 div').text
                except Exception as e:
                    price = "No price found"

                # Append extracted data to the list
                product_data.append(
                    {"image": img_src, "title": title, "description": description, "price": price})
                print(title, price, description)
        else:
            print("Failed to navigate to the product search page.")
    finally:
        driver.quit()
        print("Browser closed.")

    return product_data