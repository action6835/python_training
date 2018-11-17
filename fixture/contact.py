from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        # init add new contact
        wd.find_element_by_link_text("add new").click()
        self.fill_form_contact(contact)
        # submit
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.return_to_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.contact_cache = None

    def change_fill_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def modify_first(self, contact):
        wd = self.app.wd
        self.return_to_home_page()
        # edit contact
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        self.fill_form_contact(contact)
        # update
        wd.find_element_by_name("update").click()
        self.return_to_home_page()
        self.contact_cache = None

    def fill_form_contact(self, contact):
        wd = self.app.wd
        # fill form
        self.change_fill_value("firstname", contact.firstname)
        self.change_fill_value("middlename", contact.middlename)
        self.change_fill_value("lastname", contact.lastname)
        self.change_fill_value("nickname", contact.nickname)
        self.change_fill_value("title", contact.title)
        self.change_fill_value("company", contact.company)
        self.change_fill_value("address", contact.address)
        self.change_fill_value("home", contact.home)
        self.change_fill_value("mobile", contact.mobile)
        self.change_fill_value("work", contact.work)
        self.change_fill_value("fax", contact.fax)
        self.change_fill_value("email", contact.email)
        self.change_fill_value("email2", contact.email2)
        self.change_fill_value("email3", contact.email3)
        self.change_fill_value("homepage", contact.homepage)
        self.change_fill_value("address2", contact.address2)
        self.change_fill_value("phone2", contact.phone2)
        self.change_fill_value("notes", contact.notes)

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add"))) > 0:
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.return_to_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.return_to_home_page()
            self.contact_cache = []
            i = 2
            for element in wd.find_elements_by_css_selector('input[name="selected[]"]'):
                id = element.get_attribute("value")
                name1 = "//tr[" + str(i) + "]//td[2]"
                name2 = "//tr[" + str(i) + "]//td[3]"
                text1 = element.find_element_by_xpath(name1).text
                text2 = element.find_element_by_xpath(name2).text
                self.contact_cache.append(Contact(firstname=text2, lastname=text1, id=id))
                i = i + 1
        return list(self.contact_cache)
