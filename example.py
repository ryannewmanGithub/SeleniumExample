from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() # This opens up the Chrome test browser.

driver.get("https://example.com") # This opens the website example.com

                                # Find all <a></a> elements
elements = driver.find_elements(By.Tag_NAME, 'a')

for e in elements:
    print(e.text)
    if e.text == "More information...":
        e.click() # After click the "More information..." element, it is a link, so the
                  # website should be redirected to the linked website.
                  
        # 5 ways to interact with elements: can click, send keys, clear, submit, and select.
        print("Successfully clicked.")

