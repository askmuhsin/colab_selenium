from selenium_profiles.driver import driver as mydriver
from selenium_profiles.profiles import profiles
from selenium.webdriver.common.by import By
from selenium_profiles.utils.colab_utils import display, showscreen, show_html

from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    chromedriver_path = ChromeDriverManager(version="90.0.4430.24").install()

    md = mydriver()
    dis = display()

    dis.start_display()

    profile = profiles.Windows() # or .Android
    profile["cdp"]["cores"] = None # Chrome 90 doesn't allow emulating cores :(
    driver = md.start(profile, uc_driver=False, executable_path=chromedriver_path)
    return driver
