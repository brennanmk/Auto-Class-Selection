from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import emailer as mail

# Change to cromedriver exe location
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get("https://leopardweb.wit.edu")
print("Headless Driver Started")
counter = 1

# Input login
username = "millerklugmanb"
password = "#Bp02052"

#Enter first CRN Schedule
CRN1 = "22480"
CRN2 = ""
CRN3 = ""
CRN4 = ""
CRN5 = ""
CRN6 = ""

#Enter seceond set
2CRN1 = "22480"
2CRN2 = ""
2CRN3 = ""
2CRN4 = ""
2CRN5 = ""
2CRN6 = ""  

#Enter 3rd schedule is applicable
3CRN1 = "22480"
3CRN2 = ""
3CRN3 = ""
3CRN4 = ""
3CRN5 = ""
3CRN6 = ""

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


while counter <= 3:
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
    if driver.page_source.find("Registration Add Errors"):
        counter = counter+1
        print("script has failed")

if counter >= 3:
    print("Program has failed 3 times")
    mail.failure()
else:
    print("Program has succeeded")
    mail.success()
driver.close()
