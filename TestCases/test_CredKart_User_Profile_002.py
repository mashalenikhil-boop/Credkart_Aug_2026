import allure
import pytest
from faker import Faker

from Utilities import Excel_Utils
from Utilities.Logger import log_generator_class  # user define class import
from pageObjects.Login_Page import Login_Page_Class # user define class import
from pageObjects.Registration_Page import Registration_Page_Class  # user define class import
from Utilities.Read_Config import ReadConfigClass  # user define class import

@pytest.mark.usefixtures("browser_setup") # new
class Test_User_Login_002:
    driver = None # new
    home_page_url = ReadConfigClass.get_login_url()
    registration_url = ReadConfigClass.get_registration_url()
    login_url = ReadConfigClass.get_login_url()
    log = log_generator_class.loggen_method()


    @allure.severity(allure.severity_level.BLOCKER)
    @allure.title("Verify User login with DDT")
    @allure.description("This test case is to validate credkart user login functionality with DDT")
    @allure.link(login_url)
    @allure.story("Story 2")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    def test_Credkart_login_params_004(self,credkart_login_data):
        self.log.info("Testcase test_Credkart_login_params_004 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and landing on {self.login_url}")
        self.lp = Login_Page_Class(self.driver) # Object

        self.email = credkart_login_data[0]
        self.password = credkart_login_data[1]
        self.expected_result = credkart_login_data[2]

        # Enter Email

        self.log.info(f"Entering email: {self.email}")
        self.lp.enter_email(self.email)

        # Enter Password

        self.log.info(f"Entering password: {self.password}")
        self.lp.enter_password(self.password)

        # Click on login button
        self.log.info(f"Clicking on login button")
        self.lp.click_submit()

        self.log.info(f"Checking login status")
        if self.lp.verify_menu()== "Pass":
            self.log.info(f"login pass")
            self.log.info(f"Click on menu button")
            self.lp.click_menu()
            self.log.info(f"Click on logout button")
            self.lp.click_logout()
            self.log.info(f"Taking screenshot for login pass")
            self.driver.save_screenshot(f".\\Screenshots\\User_Login_pass_{self.email}.png")
            self.log.info("Testcase test_Credkart_login_params_004 is passed")
            actual_result = 'login_pass'
        else:
            self.log.info(f"login fail")
            self.log.info(f"Taking screenshot for login fail")
            self.driver.save_screenshot(f".\\Screenshots\\User_Login_fail_{self.email}.png")
            self.log.info("Testcase test_Credkart_login_params_004 is failed")
            actual_result = 'login_fail'

        assert actual_result == self.expected_result, f"{actual_result} != {self.expected_result}"
        self.log.info("Testcase test_Credkart_login_params_004 is completed")


    @allure.severity(allure.severity_level.NORMAL)
    @allure.title("Verify User login with DDT excel")
    @allure.description("This test case is to validate credkart user login functionality with DDT excel")
    @allure.link(login_url)
    @allure.story("Story 2")
    @allure.epic("Epic 1")
    @pytest.mark.regression
    @pytest.mark.user_profile
    def test_Credkart_login_excel_005(self):
        excel_path = ".\\TestData\\Test_Data.xlsx"
        sheet_name = "Login_Data"
        self.log.info("Testcase test_Credkart_login_excel_005 is started")

        self.lp = Login_Page_Class(self.driver) # Object
        self.rows = Excel_Utils.get_row_count(excel_path,sheet_name)
        print(f"Number of rows in excel sheet: {self.rows}")
        result_list = []
        for i in range(2, self.rows+1):
            self.driver.get(self.login_url)
            self.log.info(f"Opening Browser and landing on {self.login_url}")

            self.email = Excel_Utils.read_data(excel_path,sheet_name,i,2)
            self.password = Excel_Utils.read_data(excel_path,sheet_name,i,3)
            self.expected_result = Excel_Utils.read_data(excel_path,sheet_name,i,4)


            # Enter Email

            self.log.info(f"Entering email: {self.email}")
            self.lp.enter_email(self.email)

            # Enter Password

            self.log.info(f"Entering password: {self.password}")
            self.lp.enter_password(self.password)

            # Click on login button
            self.log.info(f"Clicking on login button")
            self.lp.click_submit()

            self.log.info(f"Checking login status")
            if self.lp.verify_menu()== "Pass":
                self.log.info(f"login pass")
                self.log.info(f"Click on menu button")
                self.lp.click_menu()
                self.log.info(f"Click on logout button")
                self.lp.click_logout()
                self.log.info(f"Taking screenshot for login pass")
                self.driver.save_screenshot(f".\\Screenshots\\User_Login_pass_{self.email}.png")
                actual_result = 'login_pass'
            else:
                self.log.info(f"login fail")
                self.log.info(f"Taking screenshot for login fail")
                self.driver.save_screenshot(f".\\Screenshots\\User_Login_fail_{self.email}.png")
                actual_result = 'login_fail'

            self.log.info(f"Writing data into excel file")
            Excel_Utils.write_data(excel_path, sheet_name, i, 5, actual_result)

            if self.expected_result == actual_result:
                test_case_stauts = 'Pass'
            else:
                test_case_stauts = 'Fail'
            result_list.append(test_case_stauts)
            Excel_Utils.write_data(excel_path, sheet_name, i, 6, test_case_stauts)

        if "Fail" not in result_list:
            self.log.info(f"All Testcases are passed")
            self.log.info("Testcase test_Credkart_login_excel_005 is passed")
            assert True
        else:
            self.log.info(f"Some testcases are failed")
            self.log.info("Testcase test_Credkart_login_excel_005 is failed")
            assert False


        self.log.info("Testcase test_Credkart_login_params_004 is completed")



# pytest -v -s -n auto --html=HTMLReports/my_report.html --browser chrome
# pytest -v -s -n auto --html=HTMLReports/my_report.html --browser chrome -k "test_Credkart_login_excel_005"