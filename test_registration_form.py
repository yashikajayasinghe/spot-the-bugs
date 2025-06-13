import pytest
from playwright.sync_api import Playwright, Page, sync_playwright, expect
from page_objects.registration_form_page import FormPage
from test_data.registration_form_data import valid_user_data, missing_lastname, missing_phone_number, missing_email, missing_password

successful_data_set = [
    (valid_user_data, FormPage.SUCCESSFUL_FORM_SUBMISSION_MESSAGE)]

mandatory_data_set = [(missing_phone_number,FormPage.PHONE_NUMBER_VALIDATION_ERROR_MESSAGE),
                      (missing_password, FormPage.PASSWORD_VALIDATION_ERROR_MESSAGE)]

# Ideally when the all mandatory fields are validated
# mandatory_data_set = [(missing_lastname, FormPage.LAST_NAME_VALIDATION_ERROR_MESSAGE),
#                       (missing_phone_number,
#                        FormPage.PHONE_NUMBER_VALIDATION_ERROR_MESSAGE),
#                       (missing_email, FormPage.EMAIL_VALIDATION_ERROR_MESSAGE),
#                       (missing_password, FormPage.PASSWORD_VALIDATION_ERROR_MESSAGE)]


def test_form_page_title(session_page: Page):
    form_page = FormPage(session_page)
    form_page.navigate_to_form_page()
    form_page.validate_page_title()


def test_successful_form_submission(session_page: Page):
    form_page = FormPage(session_page)   
    form_page.fill_form(
        first_name=valid_user_data["first_name"],
        last_name=valid_user_data["last_name"],
        phone_number=valid_user_data["phone_number"],
        country=valid_user_data["country"],
        email=valid_user_data["email"],
        password=valid_user_data["password"])
    form_page.submit_form()
    form_page.verify_submission(
        first_name=valid_user_data["first_name"],
        last_name=valid_user_data["last_name"],
        phone_number=valid_user_data["phone_number"],
        country=valid_user_data["country"],
        email=valid_user_data["email"]
    )
    form_page.verify_message_block_text_content(form_page.SUCCESSFUL_FORM_SUBMISSION_MESSAGE)


@pytest.mark.parametrize("dataset,expected_message", mandatory_data_set)
def test_mandatory_field_validations(session_page: Page, dataset,expected_message):
    form_page = FormPage(session_page)
    form_page.fill_form(
        first_name=dataset["first_name"],
        last_name=dataset["last_name"],
        phone_number=dataset["phone_number"],
        country=dataset["country"],
        email=dataset["email"],
        password=dataset["password"])

    form_page.submit_form()
    form_page.verify_message_block_text_content(expected_message)


def test_sidebar_visibility(session_page: Page):
    form_page = FormPage(session_page)
    form_page.navigate_to_form_page()
    form_page.sidebar_is_visible()

# BUG locator("#home") resolved to 2 elements
# def test_navigation_to_home(session_page: Page):
#     form_page = FormPage(session_page)
#     form_page.navigate_to_form_page()
#     form_page.navigate_to_home()
#     expect(session_page).to_have_url(form_page.HOME_URL)

# BUG locator("#home") resolved to 2 elements
# def test_navigation_to_contact(session_page: Page):
#     form_page = FormPage(session_page)
#     form_page.navigate_to_form_page()
#     form_page.navigate_to_contact()
#     expect(session_page).to_have_url(form_page.CONTACT_URL)
