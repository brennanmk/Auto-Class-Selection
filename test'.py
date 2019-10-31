import selenium
from selenium import webdriver

# Change to cromedriver exe location
driver = webdriver.Chrome(executable_path='C:/Users/brenn/OneDrive/Desktop/chromedriver.exe')
driver.get("https://leopardweb.wit.edu")


# Input login and requested CRN numbers
username = "millerklugmanb"
password = "#Bp02052"
CRN1 = "22480"
CRN2 = ""
CRN3 = ""
CRN4 = ""
CRN5 = ""
CRN6 = ""

# Find username and enter username
id_box = driver.find_element_by_name('username')
id_box.send_keys(username)
# Find password and enter password
pass_box = driver.find_element_by_name('password')
pass_box.send_keys(password)
# Submit password
login_button = driver.find_element_by_name('submit').click()

# Navigate to student
student_button = driver.find_element_by_link_text('Student').click()

# Navigate to regristration
student_button = driver.find_element_by_link_text('Registration').click()

# Navigate to select term
sub_button = driver.find_element_by_link_text('Select Term').click()

# Submit select term option
button_button = driver.find_element_by_xpath("/html/body/div[3]/form/input[2]").click()

# Navigate to Add Drop
student_button = driver.find_element_by_link_text('Add or Drop Classes').click()

# Enter CRN numbers, adjust keys accordingly
id_box = driver.find_element_by_id("crn_id1")
id_box.send_keys(CRN1)

id_box = driver.find_element_by_id("crn_id2")
id_box.send_keys(CRN2)

id_box = driver.find_element_by_id("crn_id3")
id_box.send_keys(CRN3)

id_box = driver.find_element_by_id("crn_id4")
id_box.send_keys(CRN4)

id_box = driver.find_element_by_id("crn_id5")
id_box.send_keys(CRN5)

id_box = driver.find_element_by_id("crn_id6")
id_box.send_keys(CRN6)

# Final submit classes
submit_changes = driver.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()
