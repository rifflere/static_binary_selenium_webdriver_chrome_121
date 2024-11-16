from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
# ChromeDriverManager is used if auto-download is used; ctrl+f ChromeDriverManager(driver_version='121').install()
# from webdriver_manager.chrome import ChromeDriverManager


# https://sdetunicorns.com/blog/setting-up-selenium-python-chromedriver-in-pycharm/
# https://www.youtube.com/watch?v=jQW2fjgUJrY
# https://googlechromelabs.github.io/chrome-for-testing/
# https://pypi.org/project/webdriver-manager/
# https://github.com/orgs/community/discussions/44279
def verify_title():
    # Specify 'options' as details for the Chrome Browser executable
    chrome_browser_binary_path = "binaries\chrome-win64\chrome-win64\chrome.exe"
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = chrome_browser_binary_path

    # Specify 'service' as details for the ChromeDriver executable
    chrome_driver_path = "binaries\chromedriver-win64\chromedriver-win64\chromedriver.exe"
    chrome_service = ChromeService(chrome_driver_path) # https://github.com/orgs/community/discussions/44279

    # Use [chrome_options, chrome_service] in the webdriver constructor
    driver = webdriver.Chrome(service = chrome_service, options=chrome_options)

    # if above fails, you can try: 
    # Automatically download and use the latest ChromeDriver
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version='121').install()), options=options)

    # Navigate to the website
    driver.get("https://sdetunicorns.com")
    # Get the title of the page 
    title = driver.title
    # Verify the title
    expected_title = "Master Software Testing and Automation | SDET Unicorns"
    if title == expected_title:
        print("Title verification successful!")
    else:
        print(f"Title verification failed. Expected '{expected_title}', but got '{title}'.")
    # Close the browser
    driver.quit()


if __name__ == "__main__":
    verify_title()

