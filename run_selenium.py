from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from secret import SITE_URL


def clickable(path, driver):
    driver.implicitly_wait(10)
    clk = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    clk.click()


def textable(path, driver):
    driver.implicitly_wait(10)
    clk = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    return clk.text


def sendable(path, keys, driver):
    driver.implicitly_wait(10)
    send = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, path)))
    send.send_keys(keys)


def make_list(pan):
    return_val = []
    for i in pan:
        return_val.append(i)
    return return_val


def target_sel(user_agent, email, wallet_id):
    EMAIL_REGISTER_PATH = "/html/body/div[1]/div/div[2]/form/input[1]"
    WALLET_RESISTER_PATH = "/html/body/div[1]/div/div[2]/form/input[2]"
    REGISTER_BUTTON_PATH = "/html/body/div[1]/div/div[2]/form/input[4]"

    # set browser launch options
    options = webdriver.ChromeOptions()
    options.add_extension('./plugin.zip')
    options.add_argument("user-agent=" + user_agent)
    options.add_argument('--lang=en')
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    options.add_argument("--incognito")

    browser = webdriver.Chrome(ChromeDriverManager().install(), options=options)

    browser.get(SITE_URL)

    wallet_box = browser.find_element(By.XPATH, WALLET_RESISTER_PATH)
    actions = ActionChains(browser)
    actions.move_to_element(wallet_box)
    actions.perform()

    sendable(EMAIL_REGISTER_PATH, email, browser)
    sendable(WALLET_RESISTER_PATH, wallet_id, browser)

    WebDriverWait(browser, 120).until(
        lambda x: x.find_element_by_css_selector('.antigate_solver.solved'))

    # press submit button
    clickable(REGISTER_BUTTON_PATH, browser)
    browser.quit()
