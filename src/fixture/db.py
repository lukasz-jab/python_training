import pymysql.cursors

from src.model.contact import Contact
from src.model.group import Group


class DbFixture:
    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=self.host, database=self.name, user=self.user, password=self.password,
                                          autocommit=True)

    def destroy(self):
        self.connection.close()

    def get_groups_list(self):
        groups = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT group_id, group_name, group_header, group_footer FROM group_list")
            for row in cursor:
                (id, name, header, footer) = row
                groups.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return groups

    def get_contacts_list(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT id, firstname, lastname, address, home, mobile, work, email, notes FROM addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, notes) = row
                contacts.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                        homephone=home, mobilephone=mobile, workphone=work, email_1=email,
                                        notes=notes))
        finally:
            cursor.close()
        return contacts

    def get_last_added_contact(self):
        contacts = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "SELECT id, firstname, lastname, address, home, mobile, work, email, notes FROM addressbook where deprecated = '0000-00-00 00:00:00' ORDER BY created DESC LIMIT 1")
            for row in cursor:
                (id, firstname, lastname, address, home, mobile, work, email, notes) = row
                contacts.append(Contact(id=str(id), firstname=firstname, lastname=lastname, address=address,
                                        homephone=home, mobilephone=mobile, workphone=work, email_1=email,
                                        notes=notes))
        finally:
            cursor.close()
        return contacts[0]