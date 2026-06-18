from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Step 1: Open Chrome browser
driver = webdriver.Chrome()

# Step 2: Go to Google
driver.get("https://duckduckgo.com")

# Step 3: Find the search box and type
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Selenium Python")

# Step 4: Press Enter to search
search_box.send_keys(Keys.RETURN)

# Step 5: Wait 2 seconds for results to load
time.sleep(2)

# Step 6: Print the page title
print("Title:", driver.title)
print("URL:", driver.current_url)

# Step 7: Close the browser
driver.quit()
