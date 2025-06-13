
1. The Home and Contact navigation links share the same id attribute, which violates HTML standards. (Identified using element locator.)
2. The label for the phone number input field is incorrectly spelled as "Phone nunber" instead of "Phone number".

3. The phone number field allows entry of alphabetic characters, which should be restricted to numeric input only.

4. Although the form indicates that the phone number must be at least 10 digits, this validation is not enforced upon submission.

5. The checkbox to accept terms and conditions is permanently disabled, preventing users from proceeding.

6. Incorrect Password Length Validation:The form expects passwords to be between 6 and 20 characters, but currently accepts only 6 to 19 characters.

7. Incorrect Password Label Text: The instructional text below the password field uses the abbreviation "Psw", which should be replaced with "Password" for clarity.

8. Mandatory Fields Accept Empty Input: Fields marked as required (e.g., Last Name and Email Address) still allow form submission when left empty.

9. JavaScript Console Error: A console error is logged due to a missing module in bugs-form.js at line 71.

10. Email Format Not Validated: The email address field does not validate input against a standard email format (i.e. su.salmon@example.com).

11. The note "Note: All fields marked with * are mandatory" is currently placed at the bottom of the form. It should be moved to the top for better visibility.

12. Placeholder Value Treated as Valid Input: If the user does not select a country, the form still accepts the placeholder value "Select a Country..." as valid input.

13. Value entered to the last name field is printed without the last character i.e if last name is `Baker` it prints only `Bake`

14. Last digit of the phone number gets incremented by +1 and if it is not a number gets `NAN`(the field accepts alpha numeric)

15. ?