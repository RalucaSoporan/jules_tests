from browser import Browser
from pages.login_page import LoginPage
from pages.home_page import HomePage



def before_all(context):
    context.browser = Browser()
    context.login_page_object = LoginPage()
    context.home_page_object = HomePage()

def after_all(context):
    context.browser.close()