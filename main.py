from selenium import webdriver
from selenium.webdriver.common.keys import Keys

CHROME_DRIVER_PATH = "/usr/local/bin/chromedriver"
LOA_AUCTION_URL = "https://lostark.game.onstove.com/Auction"


if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(LOA_AUCTION_URL)
    id_el = driver.find_element_by_id("user_id")
    id = input("id : ")
    id_el.send_keys(id)
    pw_el = driver.find_element_by_id("user_pwd")
    pw = input("pw : ")
    pw_el.send_keys(pw)
    pw_el.send_keys(Keys.ENTER)
