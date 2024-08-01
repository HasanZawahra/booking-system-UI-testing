from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dataAndFunctions.links import links
from pages.home import home

class Setup(home):
    Options = Options()
    Options.headless = True
    # Options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=Options)
    driver.implicitly_wait(10)
    driver.get(links.link)