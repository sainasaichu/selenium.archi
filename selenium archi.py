from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up the WebDriver (make sure to have the appropriate driver installed, e.g., chromedriver)
driver = webdriver.Chrome()

try:
    # Navigate to the website
    driver.get("https://labour.gov.in/")

    # Wait until the "Documents" menu is available and hover over it
    documents_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Documents"))
    )

    ActionChains(driver).move_to_element(documents_menu).perform()

    # Wait for the dropdown to appear and find the link to the monthly progress report
    monthly_progress_report_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Monthly Progress Report"))
    )

    # Click the link to download the report
    monthly_progress_report_link.click()

    # Add any additional steps if required to handle the download
    # For instance, handling a new window or confirming the download

finally:
    # Close the driver
    driver.quit()
