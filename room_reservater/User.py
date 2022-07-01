from selenium.webdriver.common.by import By
import settings
import config

class User:
  def __init__(self, num):
    self.id = config.USERS_INFO[num]['id']
    self.pw = config.USERS_INFO[num]['pw']
    self.get_driver()
    self.login()
    print(self.id, '로그인 완료')
  
  def get_driver(self):
    self.driver = settings.get_driver(settings.check_driver())

  def login(self):
    url = config.Url.login
    self.driver.get(url)
    self.driver.implicitly_wait(10)

    self.driver.find_element(By.CSS_SELECTOR, 'input#id').send_keys(self.id)
    self.driver.find_element(By.CSS_SELECTOR, 'input#password').send_keys(self.pw)
    self.driver.find_element(By.CSS_SELECTOR, 'input.btn_login').click()
    self.driver.implicitly_wait(10)
  
  def __del__(self):
    self.driver.quit()