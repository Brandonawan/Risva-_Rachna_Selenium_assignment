import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Set up Chrome WebDriver
chrome_options = Options()
# chrome_options.headless = False # Run Chrome in headless mode (without UI)
chrome_options.add_argument("--window-size=1920,1080")
driver = webdriver.Chrome(options=chrome_options)

# 1. Go to "https://amazon.in"
driver.get("https://www.amazon.in")

# 2. Search for "Wrist Watches" with specific filters
search_query = "Wrist Watches"
search_input = driver.find_element(By.ID, "twotabsearchtextbox")
search_input.send_keys(search_query)
search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

# Apply additional filters
time.sleep(2)
display_filter = driver.find_element(By.XPATH, "//span[text()='Analogue']")
display_filter.click()

time.sleep(2)
material_filter = driver.find_element(By.XPATH, "//span[text()='Leather']")
material_filter.click()

time.sleep(2)
brand_filter = driver.find_element(By.XPATH, "//span[text()='Titan']")
brand_filter.click()

time.sleep(2)
discount_filter = driver.find_element(By.XPATH, "//span[text()='25% Off or more']")
discount_filter.click()

# 3. Get the Fifth Element from the search
time.sleep(2)
search_results = driver.find_elements(By.CSS_SELECTOR, "[data-component-type='s-search-result']")
if len(search_results) >= 5:
    fifth_element = search_results[4]
    print(f"Fifth Element: {fifth_element.text}")
    
     # Capture a screenshot of the fifth element
    screenshot_path = "fifth_element_screenshot.png"
    fifth_element.screenshot(screenshot_path)
    print(f"Screenshot saved: {screenshot_path}")

# Quit the WebDriver
driver.quit()
