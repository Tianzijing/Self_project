from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def Chrome_flash():
    chromeOpitons = Options()
    prefs = {
        "profile.managed_default_content_settings.images": 1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player": 1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player": 1,
    }
    chromeOpitons.add_experimental_option('prefs', prefs)
    driver = webdriver.Chrome(chrome_options=chromeOpitons)
    return driver
