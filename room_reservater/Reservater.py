from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
import datetime
import config

class Reservater:
	def __init__(self, user):
		self.user = user

	def input_user_info(self):
		self.user.driver.find_element(By.CSS_SELECTOR, 'input[name=belong]').send_keys(config.InputData.belong)
		self.user.driver.find_element(By.CSS_SELECTOR, 'input[name=people]').send_keys(config.InputData.people)
		self.user.driver.find_element(By.CSS_SELECTOR, 'input[name=purpose]').send_keys(config.InputData.purpose)

	def input_date(self, date):
		self.user.driver.find_element(By.CSS_SELECTOR, 'input[name=reservation_date]').click()
		select = Select(self.user.driver.find_element(By.CSS_SELECTOR, 'select.ui-datepicker-year'))
		select.select_by_visible_text(str(date.year))
		select = Select(self.user.driver.find_element(By.CSS_SELECTOR, 'select.ui-datepicker-month'))
		select.select_by_value(str(date.month - 1))
		self.user.driver.find_element(By.LINK_TEXT, str(date.day)).click()

	def check_checkbox(self):
		for checkbox in self.user.driver.find_elements(By.CSS_SELECTOR, 'div.designCheck'):
			if checkbox.find_element(By.CSS_SELECTOR, 'input').get_attribute('disabled') == None:
				checkbox.click()
			else:
				label = checkbox.find_element(By.CSS_SELECTOR, 'label').text
				print(label + ' 체크 실패', end = ' ')
		
	def booking(self, room_num, date = datetime.datetime.now()):
		url = config.Url.reservate + str(room_num)
		self.user.driver.get(url)
		self.user.driver.implicitly_wait(10)
		self.user.driver.find_element(By.CSS_SELECTOR, 'a.red').click()
		self.user.driver.implicitly_wait(10)

		self.input_user_info()
		self.user.driver.implicitly_wait(10)
		self.input_date(date)
		self.user.driver.implicitly_wait(10)
		self.check_checkbox()
		self.user.driver.implicitly_wait(10)

		name = self.user.driver.find_element(By.CSS_SELECTOR, 'input[name=name]').get_attribute('value')

		self.user.driver.find_element(By.CSS_SELECTOR, 'button.lg').click()
		result = self.user.driver.switch_to.alert
		print(result.text)
		result.accept()
		
		return name