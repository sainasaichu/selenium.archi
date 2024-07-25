import os
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()


# Function to download an image from a URL
def download_image(image_url, folder_path, image_number):
    response = requests.get(image_url, stream=True)
    if response.status_code == 200:
        with open(os.path.join(folder_path, f"image_{image_number}.jpg"), 'wb') as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
    else:
        print(f"Failed to download image {image_number} from {image_url}")


try:
    # Navigate to the website
    driver.get("https://labour.gov.in/")

    # Wait until the "Media" menu is available and hover over it
    media_menu = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Media"))
    )
    ActionChains(driver).move_to_element(media_menu).perform()

    # Wait for the "Photo Gallery" sub-menu and click it
    photo_gallery_link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Photo Gallery"))
    )
    photo_gallery_link.click()

    # Wait until the images are loaded
    images = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    # Create a folder to store the images
    folder_path = "downloaded_images"
    os.makedirs(folder_path, exist_ok=True)

    # Download the first 10 images
    for i in range(min(10, len(images))):
        image_url = images[i].get_attribute("src")
        download_image(image_url, folder_path, i + 1)

finally:
    # Close the driver
    driver.quit()
