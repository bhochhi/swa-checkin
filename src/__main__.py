from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import sys

if __name__ == '__main__':
   confirmationNumber="L7XNQ9"
   passengerFirstName="Rupesh"
   passengerLastName="Bhochhibhoya"
   emailAddress="bhoc***@aol.com"
   phoneNumber="4050000000"

   try:
       driver = webdriver.Chrome('./chromedriver')
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
   except Exception as e:
       print(e)
       print('something went wrong')
       driver.quit()
       sys.exit(1)
   try:
       elem = driver.find_element_by_class_name("air-check-in-review-results--confirmation")
   except NoSuchElementException as e:
       print('unable to continue check-in process'+str(e))
       driver.quit()
       sys.exit(1)
   try:
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
       print("All good!! you will be getting confirmation text")
   except NoSuchElementException as e:
       print('!!'+str(e))
       sys.exit(1)
   except Exception as e:
       print('Not good!! something at last went horribly wrong!!'+str(e))
       sys.exit(1)
   finally:
       driver.quit()