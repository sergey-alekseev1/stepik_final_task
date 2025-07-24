from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        print(f">>> Current URL in should_be_login_url: {self.browser.current_url}")
        assert LoginPageLocators.LOGIN_URL in self.browser.current_url, "Login substring is not present in the current URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register is not presented"

    def register_new_user(self, email, password):
        # Check and enter email
        assert self.is_element_present(
            *LoginPageLocators.EMAIL), "Registration email input is not present"
        email_input = self.browser.find_element(*LoginPageLocators.EMAIL)
        email_input.send_keys(email)

        # Check and enter password
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD), "Registration password input is not present"
        password_input = self.browser.find_element(*LoginPageLocators.PASSWORD)
        password_input.send_keys(password)

        # Check and enter password confirmation
        assert self.is_element_present(
            *LoginPageLocators.PASSWORD_CONFIRM), "Password confirmation input is not present"
        confirm_password_input = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRM)
        confirm_password_input.send_keys(password)

        # Check and click register button
        assert self.is_element_present(*LoginPageLocators.BUTTON_REGISTRATION), "Register button is not present"
        register_button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION)
        register_button.click()
