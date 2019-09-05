# Update (HIS) Ticket Script

import time
import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

# Ticket Information

start_time = time.time()

incident_number_input = input("Enter IM Number: ")
update_type = input("\n1. HIS Upgrade\n2. Drive Upgrade\n3. RAM Upgrade\n\nChoice: ")
if int(update_type) == 2:
	drive_size = input("\n1. 256GB\n2. 500GB\n3. 1TB\n\nChoice: ")
	if int(drive_size) == 1:
		drive_size = '256GB'
	elif int(drive_size) == 2:
		drive_size = '500GB'
	elif int(drive_size) == 3:
		drive_size = '1TB'
	else:
		print('Invalid Choice')
		sys.exit(0)
elif int(update_type) == 3:
	ram_size = input("\n1. 16GB\n2. 32GB\n3. 64GB\n\nChoice: ")
	if int(ram_size) == 1:
		ram_size = '16GB'
	elif int(ram_size) == 2:
		ram_size = '32GB'
	elif int(ram_size) == 3:
		ram_size = '64GB'
	else:
		print('Invalid Choice')
		sys.exit(0)

# Open Chrome

print('Opening ITSM')
browser = webdriver.Chrome()
browser.get('http://itsm.mmm.com/sm/index.do')
#browser.minimize_window()
#print('Window Minimized')
browser.set_page_load_timeout(30)

# Goes to Incidents and Enters IM# and Searches
try:
	WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ext-gen-top339"]')))
finally:
	incident_management = browser.find_element_by_xpath('//*[@id="ext-gen-top339"]').click()
time.sleep(1)
search_incidents = browser.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div/div/div[4]/div[2]/div/ul/div/li[2]/div/a/span').click()
time.sleep(1)
frame2 = browser.switch_to.frame(1) # IMPORTANT! Swaps iFrame to input Ticket information
ticket_search = browser.find_element_by_xpath('//*[@id="X11"]').send_keys(incident_number_input, Keys.CONTROL, Keys.SHIFT, Keys.F6)
print('Searching for IM' + incident_number_input)
time.sleep(5)

# Updates Ticket Fields needed for (HIS) Upgrades

update_field = browser.find_element_by_xpath('//*[@id="X163Edit"]')
update_field2 = browser.find_element_by_xpath('//*[@id="X163"]')
status = browser.find_element_by_xpath('//*[@id="X19"]')
assign_group = browser.find_element_by_xpath('//*[@id="X21"]')
assignee = browser.find_element_by_xpath('//*[@id="X25"]')
activity_field = browser.find_element_by_xpath('//*[@id="X151_t"]')

try:
	WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="X151_t"]')))
finally:
	activity_field.click()
#time.sleep(2)
update_field.click()
print('Pending Text Update')
#time.sleep(2)
if int(update_type) == 1:
	update_field2.send_keys('Upgraded RAM 64GB and added 500GB Drive', Keys.ENTER, 'Charging Client', Keys.ENTER, 'Placing in Config', Keys.ENTER, 'Passing to Config.')
	status.click()
	status2 = browser.find_element_by_xpath('//*[@id="X19Popup_5"]') # Dropdown doesn't populate right away, this selects option after clicking box
	status2.click()
	assign_group.click()
	assign_group.clear()
	assign_group.send_keys('US_Winsexpress-Config', Keys.CONTROL, Keys.SHIFT, Keys.F4)
	print('Save Before Config')
	time.sleep(10)
	assignee.select()
	assignee.clear()
	assignee.send_keys('a7hcdzz', Keys.CONTROL, Keys.SHIFT, Keys.F2)
elif int(update_type) == 2:
	update_field2.send_keys('Upgraded ', drive_size, ' Drive', Keys.ENTER, 'Charging Client', Keys.ENTER, 'Placing on Special Pallet', Keys.ENTER, 'Passing to Issues.')
	status.click()
	status2 = browser.find_element_by_xpath('//*[@id="X19Popup_5"]') # Dropdown doesn't populate right away, this selects option after clicking box
	status2.click()
	assign_group.click()
	assign_group.clear()
	assign_group.send_keys('US_Winsexpress-Issues', Keys.CONTROL, Keys.SHIFT, Keys.F4)
	print('Save Before Issues')
	time.sleep(10)
	assignee.click()
	assignee.clear()
	assignee.send_keys(Keys.CONTROL, Keys.SHIFT, Keys.F2)
elif int(update_type) == 3:
	update_field2.send_keys('Upgraded ', ram_size, ' RAM', Keys.ENTER, 'Charging Client', Keys.ENTER, 'Placing in Config', Keys.ENTER, 'Passing to Config.')
	status.click()
	status2 = browser.find_element_by_xpath('//*[@id="X19Popup_5"]') # Dropdown doesn't populate right away, this selects option after clicking box
	status2.click()
	assign_group.click()
	assign_group.clear()
	assign_group.send_keys('US_Winsexpress-Config', Keys.CONTROL, Keys.SHIFT, Keys.F4)
	print('Save Before Config')
	time.sleep(15)
	assignee.click()
	assignee.clear()
	assignee.send_keys('a7hcdzz', Keys.CONTROL, Keys.SHIFT, Keys.F2)
else:
	print('Error with Text Update')
	sys.exit(0)

try:
	WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="X11"]')))
finally:
	activity_field.click()
	browser.close()

time.sleep(15)
end_time = time.time()
end_total = end_time - start_time

#If Statement below prints, Ticket has been Updated and Passed"""

print('Jobs Done\nTime: ', end_total)
sys.exit(0)
