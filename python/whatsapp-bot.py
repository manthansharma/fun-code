import time

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

''' WhatsApp Web Bot to send message
Requirements:
beautifulsoup4==4.4.1
requests==2.10.0
selenium==2.53.6

Note: Need ChromeDriver - WebDriver for Chrome Link : `https://sites.google.com/a/chromium.org/chromedriver/downloads`
'''

driver = webdriver.Chrome()  # Specify location of ChromeDriver
name_arr = []  # Define all contact in array format

# name_arr_rev for error handling and return the remaining contact
name_arr_rev = name_arr.copy()
name_arr_rev.reverse()

msg_arr = []  # Define all message in array format
group = True  # Define above contact array is group or not

try:
	driver.get('http://web.whatsapp.com')
	input("Press c when load complete :> ")  # Wait program to proceed till load complete

	for name in name_arr:
		if not group:
			# Click on contact button if group set to false
			contact_btn = driver.find_element_by_class_name('icon-chat')
			contact_btn.click()

		# Fill the Search Input with the contact name
		time.sleep(1)
		search_input = driver.find_element_by_class_name('input-search')
		search_input.send_keys(name)

		# Click on contact to open chat
		time.sleep(1)
		contact = driver.find_element_by_xpath('//span[contains(text(),"' + name + '")]')
		contact.click()

		for msg in msg_arr:
			msg_input = driver.find_element_by_xpath("//div[@data-tab='1'][@spellcheck='true'][@class='input']")
			for msg_elem in msg.split('\n'):
				# Write Message in chat Box
				msg_input.send_keys(msg_elem)
				# Shift + Enter for new line
				ActionChains(driver).move_to_element(msg_input) \
					.key_down(Keys.SHIFT) \
					.key_down(Keys.ENTER) \
					.key_up(Keys.ENTER) \
					.key_up(Keys.SHIFT) \
					.perform()
			msg_input.send_keys("_-Send by Python Bot!! Hail J.A.R.V.I.S.")
			driver.find_element_by_class_name('send-container').click()  # Click on send Button

			print("Message sent to Name :> " + name + ", Message:> " + msg)
		time.sleep(10)
		name_arr_rev.pop()
except Exception as e:
	print(e)
	print("Remaining Name :> " + name_arr_rev)
finally:
	input("Exit> ")
	driver.quit()
