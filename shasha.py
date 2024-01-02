from selenium import webdriver
from time import sleep

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import threading

def open_browser():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU (sometimes necessary)

    # Initialize the Chrome WebDriver with options
    driver = webdriver.Chrome(options=chrome_options)
    driver.get('https://www.shasha.com/watch/316297321423064&title=%D8%A8%D9%88%D8%AF%D9%83%D8%A7%D8%B3%D8%AA-%D8%B9%D9%85%D8%A7%D8%B1')
    sleep(5)
    driver.find_element(By.XPATH,'/html/body/div/div[4]/div[1]/div[1]/div/div[5]/div[2]/div/div/div/div[2]/div[2]/div[1]/button[1]').click()
    sleep(3)
    driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div[1]/div[4]/div/button').click()
    sleep(30)
    driver.quit()

# Create 5 threads for opening browsers
threads = []
for i in range(100000):
    for i in range(5):
        t = threading.Thread(target=open_browser)
        t.start()
        threads.append(t)
        print(i)

    # Wait for all threads to complete
    for t in threads:
        t.join()

