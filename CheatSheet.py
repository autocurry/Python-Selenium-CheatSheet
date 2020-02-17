from selenium import webdriver

driver = webdriver.Chrome("path to chrome.exe file")
driver.get("https:\\www.google.com");

# Scroll using selenium on a webpage
# scroll down the page by pixel
driver.execute_script("window.scrollBy(0,500)", "")

# scroll down the page until the element is found
element = driver.find_element_by_id("")
driver.execute_script("arguments[0].scrollIntoView();", element)

# scroll to end of the page
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
