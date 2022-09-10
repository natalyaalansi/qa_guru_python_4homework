def open_browser(browser_name):
    print_name_and_arguments(open_browser, browser_name)

def go_to_companyname_homepage(page_url):
    print_name_and_arguments(go_to_companyname_homepage, page_url)

def find_registration_button_on_login_page(page_url, button_text):
    print_name_and_arguments(find_registration_button_on_login_page, page_url, button_text)

def print_name_and_arguments(func, *args):
    func = func.__name__.capitalize().replace("_", " ")
    print(func, *args)

open_browser("Chrome")
go_to_companyname_homepage("https://labcorp.com")
find_registration_button_on_login_page("https://patient.labcorp.com", "Create an Account")