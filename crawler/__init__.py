from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys
import logging

from selenium.webdriver.chrome.options import Options


def crawl_checkin_page(confirmationNumber, passengerFirstName, passengerLastName, phoneNumber):
    try:
        logging.info('Time to crawl swa checkin for %s:%s for confirmation:%s', passengerFirstName,
                     passengerLastName, confirmationNumber)
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=1920x1080")
        driver = webdriver.Chrome(chrome_options=chrome_options)
        # driver = webdriver.Chrome()
        # driver = webdriver.Chrome(r'./chromedriver', chrome_options=chrome_options)
        driver.get("https://www.southwest.com/air/check-in/")
        driver.implicitly_wait(2)
        elem = driver.find_element_by_id("confirmationNumber")
        elem.clear()
        elem.send_keys(confirmationNumber)
        elem = driver.find_element_by_id("passengerFirstName")
        elem.clear()
        elem.send_keys(passengerFirstName)
        elem = driver.find_element_by_id("passengerLastName")
        elem.clear()
        elem.send_keys(passengerLastName)
        elem = driver.find_element_by_id("form-mixin--submit-button")
        elem.click()
        driver.implicitly_wait(5)
        logging.info('Submitted information to sw for check-in for %s', confirmationNumber)
    except Exception as e:
        logging.error("Encountered exceptions while crawling the first page:", e)
        raise e
    try:
        elem = driver.find_element_by_class_name("air-check-in-review-results--confirmation")
        logging.info('Redirected to confirmation page')
    except NoSuchElementException as e:
        logging.error('unable to continue check-in process, no air-check-in-review-results--confirmation found', e)
        raise e
    try:
        logging.info('entering phoneNumber for boarding pass to be texted')
        elem = driver.find_element_by_class_name("air-check-in-review-results--check-in-button")
        elem.click()
        driver.implicitly_wait(5)
        elem = driver.find_element_by_class_name("boarding-pass-options--button-text")
        elem.click()
        elem = driver.find_element_by_id("textBoardingPass")
        elem.clear()
        elem.send_keys(phoneNumber)
        elem = driver.find_element_by_id("form-mixin--submit-button")
        elem.click()
        logging.info("All good!! you will be getting confirmation text. Customer should get text")
        logging.info("Let's send the email if email address provided.")
        return True
    except NoSuchElementException as e:
        logging.error('Encountered exception while trying to enter phone Number for getting boarding pass', e)
        raise e
    except Exception as e:
        logging.error('Not good!! something at last went horribly wrong!!', e)
        raise e
    finally:
        if driver:
            logging.info('closing the driver')
            driver.quit()


if __name__ == '__main__':
    _confirmationNumber = "L7XNQ9"
    _passengerFirstName = "Rupesh"
    _passengerLastName = "Bhochhibhoya"
    _emailAddress = "bhoc***@aol.com"
    _phoneNumber = "4050000000"
    try:
        crawl_checkin_page(_confirmationNumber, _passengerFirstName, _passengerLastName, _phoneNumber)
    except Exception as e:
        print("send email....")
