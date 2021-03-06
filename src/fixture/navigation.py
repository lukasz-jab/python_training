from selenium.webdriver.common.by import By


class NavigationHelper:
    def __init__(self, app):
        self.app = app

    def open_groups(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/group.php") and len(
                wd.find_elements_by_css_selector("div#container div#content input[name = new]")) > 0):
            wd.find_element_by_xpath("//a[contains(@href, 'group.php')]").click()

    def open_home(self):
        wd = self.app.wd
        base_url = self.app.base_url
        wd.get(base_url)

    def open_contacts(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(
                wd.find_elements_by_css_selector("div#container div#content form[name='theform']")) > 0):
            wd.find_element_by_xpath("//a[contains(@href,'edit.php')]").click()
            # I have app in version 9.0
            if (self.app.is_element_present(By.CSS_SELECTOR, ("input[type=submit][name=quickadd]"))):
                wd.find_element_by_css_selector("input[type=submit][name=quickadd]").click()

    def return_to_groups(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@class='msgbox']//a[contains(@href, 'group.php')]").click()
