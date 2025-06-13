from playwright.sync_api import Page, expect

class FormPage:


    PHONE_NUMBER_VALIDATION_ERROR_MESSAGE = "The phone number should contain at least 10 characters!"
    PASSWORD_VALIDATION_ERROR_MESSAGE = "The password should contain between [6,20] characters!"
    # Suggested changes when all mandatory fields are validated
    # LAST_NAME_VALIDATION_ERROR_MESSAGE = "The last name should not be empty!"
    # EMAIL_VALIDATION_ERROR_MESSAGE = "The email address should not be empty!"
    SUCCESSFUL_FORM_SUBMISSION_MESSAGE = "Successfully registered the following information"
    HOME_URL = "https://qa-practice.netlify.app"
    CONTACT_URL = f"{HOME_URL}/contact-us"
    FORM_URL = f"{HOME_URL}/bugs-form"

    def __init__(self, page: Page):
        self.page = page
        self.first_name_input = page.locator("#firstName")
        self.last_name_input =  page.locator("#lastName")
        self.phone_number_input =  page.locator("#phone")
        self.country_dropdown = page.locator("#countries_dropdown_menu")
        self.email_input =  page.locator("#emailAddress")
        self.password_input =  page.locator("#password")
        self.tandc_checkbox = page.locator("#exampleCheck1")
        self.register_button =  page.locator("#registerBtn")
        self.message_block = page.locator("#message")
        self.result_firstname = page.locator("#resultFn")
        self.result_lastname = page.locator("#resultLn") 
        self.result_phone = page.locator("#resultPhone")
        self.result_country = page.locator("#country")
        self.result_email = page.locator("#resultEmail")
        self.sidebar = page.locator("#sidebar")
        self.header_home_link = page.locator("#home")
        # self.header_contact_link = page.locator("#contact") #bug same id as home link


    def navigate_to_form_page(self):
        self.page.goto(self.FORM_URL)
    
    def validate_page_title(self): 
        expect(self.page).to_have_title("QA Practice | Learn with RV")
    
    def fill_form(self, first_name: str, last_name: str, phone_number: str, country: str, email: str, password: str):
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.phone_number_input.fill(phone_number)
        self.country_dropdown.select_option(country)
        self.email_input.fill(email)
        self.password_input.fill(password)
        # self.tandc_checkbox.check() # bug
        self.page.wait_for_timeout(1000)

    def submit_form(self):
        expect(self.register_button).to_be_enabled()
        self.register_button.click()

    def verify_submission(self, first_name: str, last_name: str, phone_number: str, country: str, email: str):
        expect(self.result_firstname).to_have_text(f"First Name: {first_name}")
        # expect(self.result_lastname).to_have_text(f"Last Name: {last_name}") #Bug Not printing the whole string
        # expect(self.result_phone).to_have_text(f"Phone Number: {phone_number}") #Bug last digit gets incremented by +1 and if not a number gets `NAN`
        expect(self.result_country).to_have_text(f"Country: {country}")
        expect(self.result_email).to_have_text(f"Email: {email}")
    
    def submit_form(self):
        expect(self.register_button).to_be_enabled()
        self.register_button.click()
    
    def verify_message_block_text_content(self, message: str):
        expect(self.message_block).to_have_text(message)
    
    def sidebar_is_visible(self):
        
        expect(self.sidebar).to_be_visible()
    
    def navigate_to_home(self):
        self.header_home_link.click()
        expect(self.page).to_have_url(self.HOME_URL)


    # BUG Needs fixing duplicate ids
    # def navigate_to_contact(self):
        
    #     self.header_contact_link.click()
    #     expect(self.page).to_have_url(self.CONTACT_URL)
        
    # would be great to have a reset button
    # There's an issue here, can't investigate as I cannot run this on headed in my home network
    def clear_form(self):
        self.first_name_input.fill("")
        self.last_name_input.fill("")
        self.phone_number_input.fill("")
        self.country_dropdown.select_option(index=0) #issue
        self.email_input.fill("")
        self.password_input.fill("")
        # self.tandc_checkbox.uncheck() # tandc checkbox needs enabling

    


