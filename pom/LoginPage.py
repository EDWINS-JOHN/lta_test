from selenium.webdriver.common.by import By



class LoginPage:
    
       input_email_id ="input-login"
       input_password_id="input-Password"
       login_button_xpath="//span[normalize-space()='Sign In']"
      
      
       
       def __init__(self,driver):
              self.driver=driver
              
              
              
       def get_email(self,phone):
              self.driver.find_element(By.ID,self.input_email_id).clear()
              self.driver.find_element(By.ID,self.input_email_id).send_keys(phone)
              
       def get_password(self,password):
              self.driver.find_element(By.ID,self.input_password_id).clear()
              self.driver.find_element(By.ID,self.input_password_id).send_keys(password)
              
              
       def click_login(self):
              self.driver.find_element(By.XPATH,self.login_button_xpath).click()
              
  