from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import emailer as mail

# Input login
username = "millerklugmanb"
password = "#Bp02052"

# Enter first CRN Schedule
CRN1 = "22480"
CRN2 = ""
CRN3 = ""
CRN4 = ""
CRN5 = ""
CRN6 = ""

# Enter seceond set
second_CRN1 = "22480"
second_CRN2 = ""
second_CRN3 = ""
second_CRN4 = ""
second_CRN5 = ""
second_CRN6 = ""

# Enter 3rd schedule is applicable
third_CRN1 = "22480"
third_CRN2 = ""
third_CRN3 = ""
third_CRN4 = ""
third_CRN5 = ""
third_CRN6 = ""

#Initialize counter variables
schedule1 = 1
schedule2 = 1
schedule3=1

#Create driver
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(chrome_options=chrome_options)

#navigate to leopardweb
driver.get("https://leopardweb.wit.edu")
#Startup console message
print("Headless Driver Started")
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

# Navigate to registration
schedstudent_button = driver.find_element_by_link_text('Registration').click()

# Navigate to select term
sub_button = driver.find_element_by_link_text('Select Term').click()

# Submit select term option
button_button = driver.find_element_by_xpath("/html/body/div[3]/form/input[2]").click()

# Navigate to Add Drop
student_button = driver.find_element_by_link_text('Add or Drop Classes').click()

#Loop to find first schedule
while schedule1 <= 3:
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
        schedule1 = schedule1 + 1
        print("Schedule 1 has failed")

if schedule1 >= 3:
    print("Schedule 1 has failed to many times moving onto schedule 2:")
    while schedule2 <= 3:
        # Enter CRN numbers, adjust keys accordingly
        id_box = driver.find_element_by_id("crn_id1")
        id_box.send_keys(second_CRN1)

        id_box = driver.find_element_by_id("crn_id2")
        id_box.send_keys(second_CRN2)

        id_box = driver.find_element_by_id("crn_id3")
        id_box.send_keys(second_CRN3)

        id_box = driver.find_element_by_id("crn_id4")
        id_box.send_keys(second_CRN4)

        id_box = driver.find_element_by_id("crn_id5")
        id_box.send_keys(second_CRN5)

        id_box = driver.find_element_by_id("crn_id6")
        id_box.send_keys(second_CRN6)
        submit_changes = driver.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()
        if driver.page_source.find("Registration Add Errors"):
            schedule2 = schedule2 + 1
            print("Schedule 2 has failed")
    if schedule2 >= 3:
        print("Schedule 2 has failed to many times moving onto schedule 3:")
        while schedule3 <= 3:
            # Enter CRN numbers, adjust keys accordingly
            id_box = driver.find_element_by_id("crn_id1")
            id_box.send_keys(third_CRN1)

            id_box = driver.find_element_by_id("crn_id2")
            id_box.send_keys(third_CRN2)

            id_box = driver.find_element_by_id("crn_id3")
            id_box.send_keys(third_CRN3)

            id_box = driver.find_element_by_id("crn_id4")
            id_box.send_keys(third_CRN4)

            id_box = driver.find_element_by_id("crn_id5")
            id_box.send_keys(third_CRN5)

            id_box = driver.find_element_by_id("crn_id6")
            id_box.send_keys(third_CRN6)
            submit_changes = driver.find_element_by_xpath("/html/body/div[3]/form/input[19]").click()
            if driver.page_source.find("Registration Add Errors"):
                schedule3 = schedule3 + 1
                print("Schedule 3 has failed")
        if schedule3 >= 3:
            print("ERROR: All schedules have failed, Sending warning email")
            mail.failure()
        else:
            print("Schedule 3 has succeeded")
            mail.success()
    else:
        print("Program has suceeded")
        mail.success()
else:
    print("Program has succeeded")
    mail.success()
driver.close()
