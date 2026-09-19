import allure
import pytest
from faker import Faker

from Utilities.Logger import log_generator_class  # user define class import
from pageObjects.Login_Page import Login_Page_Class # user define class import
from pageObjects.Registration_Page import Registration_Page_Class  # user define class import
from Utilities.Read_Config import ReadConfigClass  # user define class import

@pytest.mark.usefixtures("browser_setup") # new
class Test_User_Profile:
    driver = None # new
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    home_page_url = ReadConfigClass.get_login_url()
    registration_url = ReadConfigClass.get_registration_url()
    login_url = ReadConfigClass.get_login_url()
    log = log_generator_class.loggen_method()


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify Application Url")
    @allure.description("This test case is to validate credkart title functionality ")
    @allure.link(home_page_url)
    @allure.story("Story 1")
    @allure.epic("Epic 1")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns = 1 , reruns_delay = 1)
    @pytest.mark.dependency(name="test_Credkart_URL_001")
    def test_Credkart_URL_001(self):
        # self.log.info("This is info")
        # self.log.warning("This is warning")
        # self.log.error("This is error")
        # self.log.critical("This is critical")
        self.log.info("Testcase test_Credkart_URL_001 is started")
        self.driver.get(self.home_page_url)
        self.log.info(f"Opening Browser and landing on {self.home_page_url}")
        self.log.info(f"Checking page title")
        if self.driver.title == "CredKart":

            self.log.info(f"Page title is correct and landed on correct url -->{self.driver.title}")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_pass.png")
            allure.attach.file(".\\Screenshots\\CredKart_Home_Page_pass.png", name = "CredKart_Home_Page_pass", attachment_type= allure.attachment_type.PNG )
            self.log.info("Testcase test_Credkart_URL_001 is pass")
        else :
            self.log.info(f"Page title is incorrect and landed on url -->{self.driver.title}")
            self.log.info("Taking screenshot")
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_fail.png")
            allure.attach.file(".\\Screenshots\\CredKart_Home_Page_fail.png", name="CredKart_Home_Page_fail",
                               attachment_type=allure.attachment_type.PNG
                               )
            self.log.info("Testcase test_Credkart_URL_001 is Fail")
            assert False
        self.log.info("Testcase test_Credkart_URL_001 is completed")


    @allure.severity(allure.severity_level.CRITICAL)
    @allure.title("Verify User Login")
    @allure.description("This test case is to validate credkart user login functionality ")
    @allure.link(login_url)
    @allure.story("Story 2")
    @allure.epic("Epic 1")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.user_profile
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    #@pytest.mark.dependency(depends =["test_Credkart_URL_001"])
    def test_Credkart_login_002(self):
        self.log.info("Testcase test_Credkart_login_002 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and landing on {self.login_url}")
        self.lp = Login_Page_Class(self.driver) # Object

        # Enter Email

        # email = self.driver.find_element(By.ID, "email")
        # email.send_keys("CredenceTest_5005@credence.in")
        self.log.info(f"Entering email: {self.email}")
        self.lp.enter_email(self.email)

        # Enter Password

        # password = self.driver.find_element(By.ID, "password")
        # password.send_keys("Password@123")
        self.log.info(f"Entering password: {self.password}")
        self.lp.enter_password(self.password)

        # Click on login button
        # login_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        # login_button.click()
        self.log.info(f"Clicking on login button")
        self.lp.click_submit()

        # Verify Login
        # try:
        #     # time.sleep(5)
        #     # Wait to load menu button
        #     WebDriverWait(self.driver, 5).until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']"))
        #         )
        #     self.driver.save_screenshot(".\\Screenshots\\Login_success_screenshot.png")
        #     # Click on menu Button
        #     self.driver.find_element(By.XPATH, "//a[@role='button']").click()
        #     # Click on Logout link
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
        #     print("Login Success")
        # except:
        #     self.driver.save_screenshot(".\\Screenshots\\Login_failure_screenshot.png")
        #     print("Login Failure")
        #     assert False
        self.log.info(f"Checking login status")
        if self.lp.verify_menu()== "Pass":
            self.log.info(f"login pass")
            self.log.info(f"Click on menu button")
            self.lp.click_menu()
            self.log.info(f"Click on logout button")
            self.lp.click_logout()
            self.log.info(f"Taking screenshot for login pass")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_pass.png")
            allure.attach.file(".\\Screenshots\\User_Login_pass.png", name="User_Login_pass",
                               attachment_type=allure.attachment_type.PNG
                               )
            self.log.info("Testcase test_Credkart_login_002 is passed")
        else:
            self.log.info(f"login fail")
            self.log.info(f"Taking screenshot for login fail")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_fail.png")
            self.log.info("Testcase test_Credkart_login_002 is failed")
            assert False
        self.log.info("Testcase test_Credkart_login_002 is completed")

    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify User Registration")
    @allure.description("This test case is to validate credkart user registration functionality ")
    @allure.link(registration_url)
    @allure.story("Story 2")
    @allure.epic("Epic 1")
    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.user_profile
    @pytest.mark.flaky(reruns=1, reruns_delay=1)
    #@pytest.mark.dependency(depends =["test_Credkart_URL_001"])
    def test_Credkart_Registration_003(self):
        self.log.info("Testcase test_Credkart_Registration_003 is started")
        self.driver.get(self.registration_url)
        self.log.info(f"Opening Browser and landing on {self.registration_url}")
        name_data = Faker().name()
        print(f"name_data-->{name_data}")

        email_data = Faker().email()
        print(f"email_data-->{email_data}")

        self.rp = Registration_Page_Class(self.driver)
        self.lp = Login_Page_Class(self.driver)

        # Enter Name
        #self.driver.find_element(By.ID, "name").send_keys(name_data)
        self.log.info(f"Entering name: {name_data}")
        self.rp.enter_name(name_data)

        # Enter Email
       #self.driver.find_element(By.ID, "email").send_keys(email_data)

        self.log.info(f"Entering email: {email_data}")
        self.lp.enter_email(email_data)

        # Enter Password
        #self.driver.find_element(By.ID, "password").send_keys("Password@123")
        self.log.info(f"Entering password")
        self.lp.enter_password("Password@123")

        # Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("Password@123")
        self.log.info(f"Entering confirm password")
        self.rp.enter_confirm_password("Password@123")

        # Click Register Button
        #self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        self.log.info(f"Click on register button")
        self.lp.click_submit()

        # Verify Registration
        # try:
        #     # time.sleep(5)
        #     self.driver.save_screenshot(".\\Screenshots\\Registration_success_screenshot.png")
        #     # Click on menu Button
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/a").click()
        #     # Click on Logout link
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
        #     print("Registration Success")
        # except:
        #     self.driver.save_screenshot(".\\Screenshots\\Registration_failure_screenshot.png")
        #     print("Registration Failure")
        #     assert False

        self.log.info(f"Checking registration status")
        if self.lp.verify_menu()== "Pass":
            self.log.info(f"registration pass")
            self.log.info(f"Click on menu button")
            self.lp.click_menu()
            self.log.info(f"Click on logout button")
            self.lp.click_logout()
            self.log.info(f"Taking screenshot for registration pass")
            self.driver.save_screenshot(".\\Screenshots\\User_registration_pass.png")
            allure.attach.file(".\\Screenshots\\User_registration_pass.png", name="User_registration_pass",
                               attachment_type=allure.attachment_type.PNG
                               )
            self.log.info("Testcase test_Credkart_Registration_003 is passed")
        else:
            self.log.info(f"registration fail")
            self.log.info(f"Taking screenshot for registration fail")
            self.driver.save_screenshot(".\\Screenshots\\User_registration_fail.png")
            self.log.info("Testcase test_Credkart_Registration_003 is failed")
            assert False
        self.log.info("Testcase test_Credkart_Registration_003 is completed")

# pytest -v -s -n auto --html=HTMLReports/my_report.html --browser chrome
# pytest -v -s -n auto --alluredir="AllureReports" --browser chrome
# allure serve "AllureReports"