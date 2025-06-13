valid_user_data = {
    "first_name": "Sussie",
    "last_name": "Salmon",
    "phone_number": "1234567890",
    "country": "New Zealand",
    "email": "su.salmon@example.com",
    "password": "mypassword111"
}
missing_lastname = {**valid_user_data, "last_name": ""}
missing_phone_number = {**valid_user_data, "phone_number": ""}  
missing_email = {**valid_user_data, "email": ""}
missing_password = {**valid_user_data, "password": ""}
invalid_email = {**valid_user_data, "email": "invalid-email.com"}
invalid_phone_number = {**valid_user_data, "phone_number": "sahdjsdh"} 
short_phone_number = {**valid_user_data,  "phone_number": "123"} 
short_password = {**valid_user_data, "password": "123"}