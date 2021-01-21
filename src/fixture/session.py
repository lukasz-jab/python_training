class SessionHelper:
    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.navigation.open_home_page()
        wd.find_element_by_css_selector("input[name = user]").send_keys(username)
        wd.find_element_by_css_selector("input[name = pass]").send_keys(password)
        wd.find_element_by_css_selector("input[type = submit][value = Login]").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[@onclick='document.logout.submit();']").click()
