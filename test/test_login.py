from pom.LoginPage import LoginPage
from config import BASE_URL, EMAIL, PASSWORD
import time


class Test_001_Login:

    def test_login(self, driver, logger):
        logger.info("******************** Test_login ************")
        logger.info("******************** Started login test ************")
        driver.get(BASE_URL)
        time.sleep(2)
        login = LoginPage(driver)
        login.get_email(EMAIL)
        login.get_password(PASSWORD)
        login.click_login()
        actual_title = driver.title

        if actual_title == "Lori Transporter App":
            assert True
            time.sleep(2)
            driver.save_screenshot(".../Screenshots/"+"login_title.png")
            driver.close()
            logger.info("******************** login test passed ************")
        else:
            time.sleep(2)
            driver.save_screenshot(".../Screenshots/"+"login_title.png")
            driver.close()
            logger.info("******************** login test Failed ************")
            assert False