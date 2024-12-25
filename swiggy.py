from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
# selenium 4
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.os_manager import ChromeType


def swiggy_data(product_name: str, location: str):

    axis_location = [23.211754, 77.433601]

    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")  # Required for headless mode on Windows
    chrome_options.add_argument("--no-sandbox")  # Recommended for containerized environments
    chrome_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems

    # driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome(service=ChromiumService(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()))      
    # driver = webdriver.Chrome(service=Service(ChromeDriverManager(version="131.0.6778.204").install()), options=chrome_options)
    # service = Service("/usr/bin/chromium-driver")  # Path to chromium driver
    # driver = webdriver.Chrome(service=service, options=chrome_options)

    driver.set_window_size(1920, 1080)

    # Open the webpage with dynamic product search and axis_location
    driver.get(f"https://www.swiggy.com/instamart/search?custom_back=true&query={product_name}&lat={axis_location[0]}&lng={axis_location[1]}")

    # Zoom out to 40%
    driver.execute_script("document.body.style.zoom='40%'")
    time.sleep(3)

    # Locate product containers
    product_containers = driver.find_elements(
        By.CSS_SELECTOR, "div[data-testid='default_container_ux4']")

    product_data = []

    # Extract information from each product container
    for product in product_containers:
        data = {}
        try:
            data["image"] = product.find_element(
                By.CSS_SELECTOR, "img[class='sc-dcJsrY ibghhT _1NxA5']").get_attribute("src")
        except:
            data["image"] = "No image found"

        try:
            data["title"] = "(Swiggy) " + product.find_element(
                By.CSS_SELECTOR, "div.novMV").text
        except:
            data["title"] = "No title found"
        try:
            data["price"] = product.find_element(
                By.CSS_SELECTOR, "div[data-testid='itemOfferPrice']").text
        except:
            data["price"] = "No price found"

        try:
            data["description"] = product.find_element(
                By.CSS_SELECTOR, "div[aria-label]").text
        except:
            data["description"] = "No weight found"

        product_data.append(data)
    # Close the browser
    driver.quit()

    return product_data
