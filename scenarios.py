from time import sleep

def first_retrieval(driver, url, email, password_txt):
    driver.get(url)
    sleep(5)
    
    elem = driver.find_element_by_css_selector(".overlay-signup__btn")
    elem.click()
    sleep(2)

    mail = driver.find_element_by_id("email")
    mail.send_keys(email)
    sleep(0.4)
    password = driver.find_element_by_id("password")
    password.send_keys(password_txt)
    sleep(0.6)
    submit = driver.find_element_by_css_selector(".signup__submit")
    submit.click()
    sleep(8)

    export = driver.find_element_by_css_selector(".board-top-left-panel__export")
    export.click()
    sleep(1)
    to_pdf = driver.find_element_by_css_selector(".AT__export--BOARD_EXPORT_PDF")
    to_pdf.click()
    sleep(1)
    download = driver.find_element_by_css_selector('button[hm-tap="modal.download()"]')
    download.click()
    sleep(3)

def retrieval(driver, url):
    driver.get(url)
    sleep(8)

    export = driver.find_element_by_css_selector(".board-top-left-panel__export")
    export.click()
    sleep(1)
    to_pdf = driver.find_element_by_css_selector(".AT__export--BOARD_EXPORT_PDF")
    to_pdf.click()
    sleep(1)
    download = driver.find_element_by_css_selector('button[hm-tap="modal.download()"]')
    download.click()
    sleep(3)
