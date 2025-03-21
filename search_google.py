 from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode

# Set up the Chrome driver
service = Service('/path/to/chromedriver')  # Update the path to your chromedriver
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # Navigate to a website
    driver.get("https://www.example.com")

    # Find an element and perform an action
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("OpenAI")
    search_box.send_keys(Keys.RETURN)

    # Wait for results to load
    time.sleep(3)

    # Print the title of the page
    print(driver.title)

finally:
    # Close the browser
    driver.quit()# You can start using it by creating a file using the (+) button or simply by clicking the compile button.
# You can take a screenshot of the entire input-output area by clicking the snap button.
# You can also install/uninstall modules according to your desires.
# You can delete or rename created files as well.
